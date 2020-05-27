from typing import Any

from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from matchflix import crud, schemas
from matchflix.api import deps

router = APIRouter()


@router.post("/", response_model=schemas.UserAnswersCreate, status_code=201)
def create_answers(
    *, db: Session = Depends(deps.get_db), answers_in: schemas.UserAnswersCreate
) -> Any:
    """
    Create new answers
    """
    user = crud.answer.create_multiple_answers(db=db, obj_in=answers_in)
    data = jsonable_encoder(user)
    data.update({"answers": jsonable_encoder(user.answers)})
    return data
