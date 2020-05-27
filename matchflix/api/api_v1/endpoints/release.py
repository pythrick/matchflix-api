from typing import List

from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from matchflix import crud, schemas
from matchflix.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Release])
def list_releases(db: Session = Depends(deps.get_db), skip: int = 0, limit: int = 100):
    """
    List releases.
    """
    releases = crud.release.list(db, skip=skip, limit=limit)
    return jsonable_encoder(releases)
