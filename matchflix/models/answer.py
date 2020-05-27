import enum
from typing import TYPE_CHECKING

from sqlalchemy import Column, Enum, ForeignKey
from sqlalchemy.orm import relationship

from matchflix.db.base_class import GUID, Base

if TYPE_CHECKING:
    from .user import User  # noqa: F401
    from .release import Release  # noqa: F401


class ActionEnum(enum.Enum):
    LEFT = "LEFT"
    RIGHT = "RIGHT"
    DID_NOT_WATCH = "DID_NOT_WATCH"


class Answer(Base):
    action = Column(Enum(ActionEnum))
    owner_id = Column(GUID, ForeignKey("user.id"))
    owner = relationship("User", back_populates="answers")
    release_id = Column(GUID, ForeignKey("release.id"))
    release = relationship("Release", back_populates="answers")
