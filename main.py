from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from uuid import UUID
import dataset
import enum

app = FastAPI()


class Action(enum.Enum):
    LEFT = "LEFT"
    RIGHT = "RIGHT"
    DID_NOT_WATCH = "DID_NOT_WATCH"


class Answer(BaseModel):
    release_id: int
    action: Action


class UserAnswer(BaseModel):
    email: str
    answers: List[Answer]


@app.get("/releases")
def list_releases():
    db = dataset.connect('sqlite:///db.sqlite3')
    result = db.query('SELECT * FROM releases LIMIT 50')
    result = [
        {
            "cover": r["image"],
            "title": r["title"],
            "id": r["id"],
            "description": r["description"]
        }
        for r in result
    ]
    return result 


@app.post("/users-answers", status_code=201)
def create_user_answers(user_answer: UserAnswer):
    db = dataset.connect('sqlite:///db.sqlite3')
    user_table = db["user"]

    user_id = user_table.upsert(dict(email=user_answer.email), ["email"])
    answers_table = db["answers"]

    for answer in user_answer.answers:
        answers_table.insert({
            "release_id": answer.release_id,
            "action": answer.action.value,
            "user_id": user_id
        })

    return {
        "message": "Success!"
    }
