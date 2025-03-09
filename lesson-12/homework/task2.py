import requests
from bs4 import BeautifulSoup
import sqlite3
import csv

# Scrape job listings from the website
def scrape_job_listings(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    jobs = []

    for job_elem in soup.find_all('div', class_='card-content'):
        title_elem = job_elem.find('h2', class_='title')
        company_elem = job_elem.find('h3', class_='subtitle')
        location_elem = job_elem.find('p', class_='location')
        description_elem = job_elem.find('div', class_='content')
        link_elem = job_elem.find('a', text='Apply')

        if None in (title_elem, company_elem, location_elem, description_elem, link_elem):
            continue

        job = {
            'title': title_elem.text.strip(),
            'company': company_elem.text.strip(),
            'location': location_elem.text.strip(),
            'description': description_elem.text.strip(),
            'application_link': link_elem['href']
        }
        jobs.append(job)

    return jobs

# Setting up the database
def setup_database(db_name='jobs.db'):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            company TEXT,
            location TEXT,
            description TEXT,
            application_link TEXT,
            UNIQUE(title, company, location)
        )
    ''')
    conn.commit()
    return conn, cursor


# Filling and updating the db
def insert_or_update_job(cursor, job):
    cursor.execute('''
        INSERT INTO jobs (title, company, location, description, application_link)
        VALUES (?, ?, ?, ?, ?)
        ON CONFLICT(title, company, location) DO UPDATE SET
            description=excluded.description,
            application_link=excluded.application_link
    ''', (job['title'], job['company'], job['location'], job['description'], job['application_link']))


# Filtering the jobs
def filter_jobs(filter_by, value, db_name='jobs.db'):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    query = f"SELECT * FROM jobs WHERE {filter_by} LIKE ?"
    cursor.execute(query, ('%' + value + '%',))
    results = cursor.fetchall()
    conn.close()
    return results

# Write to csv file
def export_to_csv(jobs, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['id', 'title', 'company', 'location', 'description', 'application_link']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for job in jobs:
            writer.writerow({
                'id': job[0],
                'title': job[1],
                'company': job[2],
                'location': job[3],
                'description': job[4],
                'application_link': job[5]
            })

def main():
    url = 'https://realpython.github.io/fake-jobs'
    jobs = scrape_job_listings(url)
    conn, cursor = setup_database()

    for job in jobs:
        insert_or_update_job(cursor, job)

    conn.commit()
    conn.close()

if __name__ == '__main__':
    main()
    filtered_jobs = filter_jobs('location', 'New York')
    export_to_csv(filtered_jobs, 'filtered_jobs.csv')

