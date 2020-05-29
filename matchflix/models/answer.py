from uuid import UUID

from pydantic import BaseModel
from typing import List
from enum import Enum


class Action(str, Enum):
    LEFT = "LEFT"
    RIGHT = "RIGHT"
    DID_NOT_WATCH = "DID_NOT_WATCH"


class Answer(BaseModel):
    movie_id: UUID
    action: Action


class UserMovies(BaseModel):
    email: str
    answers: List[Answer]
