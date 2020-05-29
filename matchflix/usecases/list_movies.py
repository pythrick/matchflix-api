from matchflix.extensions.db import database
from matchflix.models.movie import Movie


async def list_movies():
    rows = await database.fetch_all(query="SELECT * FROM movies")
    result = [
        Movie(
            id=row["id"],
            cover=row["cover"],
            title=row["title"],
            description=row["description"],
            tmdb_id=row["tmdb_id"]
        )
        for row in rows
    ]
    return result
