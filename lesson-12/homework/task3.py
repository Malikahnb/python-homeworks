import requests
from bs4 import BeautifulSoup
import json
import time


def get_page_soup(url):
    response = requests.get(url)
    return BeautifulSoup(response.text, 'html.parser')


def extract_laptop_data(card):
    name = card.find('h4', class_='card-title').text.strip()
    price = card.find('h5').text.strip()
    description = card.find('p', class_='card-text').text.strip()
    return {"name": name, "price": price, "description": description}


def scrape_laptops(base_url):
    laptops = []
    page_number = 1

    while True:
        url = f"{base_url}#page={page_number}"
        soup = get_page_soup(url)
        cards = soup.find_all('div', class_='card h-100')

        if not cards:
            break

        for card in cards:
            laptop = extract_laptop_data(card)
            laptops.append(laptop)

        page_number += 1
        time.sleep(1)  # To avoid overwhelming the server

    return laptops

# Save data to JSON file
def save_to_json(data, filename='laptops.json'):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def main():
    base_url = 'https://www.demoblaze.com/index.html'
    laptops = scrape_laptops(base_url)
    save_to_json(laptops)

if __name__ == '__main__':
    main()
