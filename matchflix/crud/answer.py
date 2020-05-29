from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from matchflix.crud.base import CRUDBase
from matchflix.db.models import Answer, User, Release
from matchflix.schemas.answer import AnswerCreate, AnswerUpdate, UserAnswersCreate


class CRUDAnswer(CRUDBase[Answer, AnswerCreate, AnswerUpdate]):
    def create_multiple_answers(
        self, db: Session, *, obj_in: UserAnswersCreate
    ) -> User:
        db_user = db.query(User).filter_by(email=obj_in.email).first()
        if db_user:
            raise Exception("User already exists.")

        answers_releases = {a.release_id for a in obj_in.answers}
        db_releases = db.query(Release).all()
        for release in db_releases:
            if release.id not in answers_releases:
                raise Exception("One or more releases not informed.")

        db_user = User(email=obj_in.email)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)

        for answer in obj_in.answers:
            obj_in_data = jsonable_encoder(answer)
            obj_in_data["owner_id"] = db_user.id
            db_obj = self.model(**obj_in_data)  # type: ignore
            db.add(db_obj)
        db.commit()
        db.refresh(db_user)
        return db_user


answer = CRUDAnswer(Answer)
