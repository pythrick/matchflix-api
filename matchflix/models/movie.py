from pydantic import BaseModel


class Movie(BaseModel):
    id: str
    title: str
    description: str
    cover: str
    tmdb_id: int
