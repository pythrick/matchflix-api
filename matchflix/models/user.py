from typing import TYPE_CHECKING

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from matchflix.db.base_class import Base

if TYPE_CHECKING:
    from .answer import Answer  # noqa: F401


class User(Base):
    email = Column(String, index=True, unique=True)
    answers = relationship("Answer", back_populates="owner")
