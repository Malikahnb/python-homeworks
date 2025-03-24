import requests
import random

API_KEY = "a6d24eca851a31cef45907343a95d86d"

# Base URLs
GENRE_URL = f"https://api.themoviedb.org/3/genre/movie/list?api_key={API_KEY}&language=en-US"
MOVIE_URL = "https://api.themoviedb.org/3/discover/movie"


def get_genre_id(genre_name):
    response = requests.get(GENRE_URL)
    if response.status_code == 200:
        genres = response.json()["genres"]
        for genre in genres:
            if genre_name.lower() == genre["name"].lower():
                return genre["id"]
    return None


def get_random_movie(genre_id):
    """Fetch random movie from a given genre"""
    params = {
        "api_key": API_KEY,
        "with_genres": genre_id,
        "language": "en-US",
        "sort_by": "popularity.desc"
    }
    response = requests.get(MOVIE_URL, params=params)
    if response.status_code == 200:
        movies = response.json()["results"]
        if movies:
            movie = random.choice(movies)
            return movie["title"], movie["overview"]
    return None, None


# Ask user for genre input
genre_name = input("Enter a movie genre (e.g., Action, Comedy, Drama): ")
genre_id = get_genre_id(genre_name)

if genre_id:
    movie_title, movie_overview = get_random_movie(genre_id)
    if movie_title:
        print(f"\n🎬 Recommended Movie: {movie_title}")
        print(f"📖 Overview: {movie_overview}")
    else:
        print("No movies found in this genre.")
else:
    print("Invalid genre. Please try again.")
