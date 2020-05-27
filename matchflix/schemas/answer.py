from enum import Enum
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel, EmailStr


class Action(str, Enum):
    LEFT = "LEFT"
    RIGHT = "RIGHT"
    DID_NOT_WATCH = "DID_NOT_WATCH"


# Shared properties
class AnswerBase(BaseModel):
    release_id: Optional[UUID]
    action: Optional[Action]


# Properties to receive on answer creation
class AnswerCreate(AnswerBase):
    release_id: UUID
    action: Action


# Properties to receive on answer update
class AnswerUpdate(AnswerBase):
    pass


class UserAnswersCreate(BaseModel):
    email: EmailStr
    answers: List[AnswerCreate]


# Properties shared by models stored in DB
class AnswerInDBBase(AnswerBase):
    id: UUID


# Properties to retun to client
class Answer(AnswerInDBBase):
    pass


# Properties stored in DB
class AnswerInDB(AnswerInDBBase):
    pass
