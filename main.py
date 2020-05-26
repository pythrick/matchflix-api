from fastapi import FastAPI
from pydantic import BaseModel
from uuid import UUID
import enum

app = FastAPI()


class Swipe(enum.Enum):
    LEFT = "LEFT"
    RIGHT = "RIGHT"


class UserAnswer(BaseModel):
    release_id: UUID
    swipe: Swipe


@app.get("/releases")
def list_releases():
    return [
        {
            "cover": "",
            "title": "",
            "id": ""
        },
        {
            "cover": "",
            "title": "",
            "id": ""
        },
        {
            "cover": "",
            "title": "",
            "id": ""
        },
        {
            "cover": "",
            "title": "",
            "id": ""
        }
    ]


@app.post("/users-answers")
def create_user_answers(user_answer: UserAnswer):
    #TODO: Store on database
    return user_answer
