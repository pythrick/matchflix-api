from pprint import pprint

import dataset
import requests
from dynaconf import settings

db = dataset.connect("sqlite:///db.sqlite3")


release_db = db["release"]


match = {
    "intersection": {
        "36bce7c0-09d4-4b96-8f45-7f75aa1b3b7a",
        "80447895-43cd-4be6-82db-656b038c84ea",
        "9a2784ca-c218-4807-b64b-cf0ca422cf35",
        "b167e1d2-bc7d-4bde-a164-2fe61a2c4cde",
        "ede8622c-9344-453d-b48d-6e6cf952c7e2",
    },
    "match_user": {
        "id": "7f7dd801-79b6-4948-8197-befe3cc4ce6e",
        "email": "justinhawkins@flores-reid.info",
    },
    "score": 0.25,
    "user": {
        "id": "cc0ef760-541b-4883-886f-637e1aa636cb",
        "email": "gabrielle28@gmail.com",
    },
}

releases = [
    release_db.find_one(id=release_id)["tmdb_id"]
    for release_id in match["intersection"]
]

recomendations = []

recomendations_score = []
for release in releases:
    url = f"https://api.themoviedb.org/3/movie/{release}/recommendations?api_key={settings.TMDB_API_KEY}&language=en-US&page=1"
    response = requests.get(url).json()
    for movie in response["results"]:
        recomendations.append(movie["id"])
        recomendations_score.append({"id": movie["id"], "score": movie["vote_average"]})


set_recomendations = set(recomendations)
if len(recomendations) == len(set_recomendations):
    # Não tem duplicados
    movie = max(recomendations_score, key=lambda x: x["score"])["id"]
else:
    movie = max(set_recomendations, key=recomendations.count)

print(movie)
