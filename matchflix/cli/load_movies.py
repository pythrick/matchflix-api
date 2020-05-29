from uuid import uuid4

import dataset
import requests
from dynaconf import settings


def list_movies_from_tmdb():
    url = f"https://api.themoviedb.org/3/movie/top_rated?api_key={settings.TMDB_API_KEY}&language=en-US&page=1"
    response = requests.get(url)
    return response.json()["results"]


def insert_movies_in_db(db, movies):
    table = db["movies"]
    for item in movies:
        table.insert(
            {
                "id": str(uuid4()),
                "title": item["title"],
                "description": item["overview"],
                "cover": f"https://image.tmdb.org/t/p/w600_and_h900_bestv2{item['poster_path']}",
                "tmdb_id": item["id"],
            }
        )


def main():
    movies = list_movies_from_tmdb()
    db = dataset.connect(settings.DATABASE_DSN)
    insert_movies_in_db(db, movies)


if __name__ == '__main__':
    main()
