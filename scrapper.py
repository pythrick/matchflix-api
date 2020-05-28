from uuid import uuid4

import dataset
import requests
from dynaconf import settings

url = f"https://api.themoviedb.org/3/movie/top_rated?api_key={settings.TMDB_API_KEY}&language=en-US&page=1"
response = requests.get(url)
results = response.json()["results"]

db = dataset.connect("sqlite:///db.sqlite3")
table = db["release"]
for item in results:
    table.insert(
        {
            "id": str(uuid4()),
            "title": item["title"],
            "description¨": item["overview"],
            "cover": f"https://image.tmdb.org/t/p/w600_and_h900_bestv2{item['poster_path']}",
            "tmdb_id": item["id"],
        }
    )
