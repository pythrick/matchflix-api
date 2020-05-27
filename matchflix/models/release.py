from typing import TYPE_CHECKING

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from matchflix.db.base_class import Base

if TYPE_CHECKING:
    from .answer import Answer  # noqa: F401


class Release(Base):
    title = Column(String, index=True)
    description = Column(String, index=True)
    cover = Column(String,)
    answers = relationship("Answer", back_populates="release")
