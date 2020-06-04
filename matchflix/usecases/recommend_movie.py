from pprint import pprint

import dataset
import requests
from dynaconf import settings


db = dataset.connect(settings.DATABASE_URL)


def list_user_movies(user_id):
    query = f"""
    SELECT m.tmdb_id AS tmdb_id FROM user_movies AS um
    INNER JOIN movies AS m ON um.movie_id == m.id
    WHERE um.user_id = '{user_id}'
    AND um.action = 'RIGHT'
    """
    return {row["tmdb_id"] for row in db.query(query)}


def get_movie_from_tmdb(tmdb_id):
    url = f"https://api.themoviedb.org/3/movie/{tmdb_id}?api_key={settings.TMDB_API_KEY}&language=en-US&page=1"
    response = requests.get(url).json()
    return response


def recommend_movie(user_id, other_user_id):
    user_movies = list_user_movies(user_id)
    other_user_movies = list_user_movies(other_user_id)

    intersection = user_movies & other_user_movies
    print(intersection)

    recomendations = []
    recomendations_score = []
    for tmdb_id in intersection:
        url = f"https://api.themoviedb.org/3/movie/{tmdb_id}/recommendations?api_key={settings.TMDB_API_KEY}&language=en-US&page=1"
        response = requests.get(url).json()
        for movie in response["results"]:
            recomendations.append(movie["id"])
            recomendations_score.append(
                {"id": movie["id"], "score": movie["vote_average"]}
            )

    set_recomendations = set(recomendations)
    if len(recomendations) == len(set_recomendations):
        # Não tem duplicados
        recommended_movie = max(recomendations_score, key=lambda x: x["score"])["id"]
    else:
        recommended_movie = max(set_recomendations, key=recomendations.count)

    return get_movie_from_tmdb(tmdb_id)
