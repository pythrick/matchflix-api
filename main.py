from typing import List

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pprint import pprint

from matchflix.extensions.db import database
from matchflix.models import Movie, UserMovies
from matchflix import usecases


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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
    user_id = await usecases.register_user_movies(user_movies)
    # matched_user, score = await usecases.find_match(user_id)
    # movie = usecases.recommend_movie(user_id, matched_user["id"])
    # pprint(movie)
