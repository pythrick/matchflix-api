from typing import List

from fastapi import FastAPI

from matchflix.extensions.db import database
from matchflix.models import Movie, UserMovies
from matchflix import usecases

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get("/movies", response_model=List[Movie])
async def list_movies():
    return await usecases.list_movies()


@app.post("/user-movies", status_code=201)
async def create_user_movies(user_movies: UserMovies):
    return await usecases.register_user_movies(user_movies)
