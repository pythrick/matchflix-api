from uuid import uuid4

from fastapi.encoders import jsonable_encoder

from matchflix.models import UserMovies
from matchflix.extensions.db import database as db


async def register_user_movies(user_movies: UserMovies):
    query = "SELECT * FROM users WHERE email = :email"
    values = {"email": user_movies.email}
    user = await db.fetch_one(query, values=values)
    if user:
        raise Exception("User already exists.")

    movies_from_answers = [str(a.movie_id) for a in user_movies.answers]

    query = "SELECT * FROM movies"
    movies = await db.fetch_all(query)
    for movie in movies:
        if movie["id"] not in movies_from_answers:
            raise Exception(f"Movie {movie['id']} not informed.")

    query = "INSERT INTO users(id, email) VALUES (:id, :email)"
    values = {"id": str(uuid4()), "email": user_movies.email}
    await db.execute(query, values=values)

    query = "SELECT id FROM users WHERE email = :email"
    values = {"email": user_movies.email}
    result = await db.fetch_one(query, values=values)
    user_id = result["id"]
    for answer in user_movies.answers:
        query = "INSERT INTO user_movies(id, movie_id, user_id, action) VALUES (:id, :movie_id, :user_id, :action)"
        values = {
            "id": str(uuid4()),
            "movie_id": str(answer.movie_id),
            "user_id": user_id,
            "action": answer.action.value,
        }
        await db.execute(query, values=values)
    return user_id
