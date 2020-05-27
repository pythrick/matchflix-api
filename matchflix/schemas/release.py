from typing import TYPE_CHECKING
from uuid import UUID

from pydantic import BaseModel

if TYPE_CHECKING:
    from .answer import Answer  # noqa: F401


# Shared properties
class ReleaseBase(BaseModel):
    cover: str
    title: str
    description: str


# Properties to receive on release creation
class ReleaseCreate(ReleaseBase):
    pass


# Properties to receive on releae update
class ReleaseUpdate(ReleaseBase):
    pass


# Properties shared by models stored in DB
class ReleaseInDBBase(ReleaseBase):
    id: UUID


# Properties to retun to client
class Release(ReleaseInDBBase):
    pass


# Properties stored in DB
class ReleaseInDB(ReleaseInDBBase):
    pass
