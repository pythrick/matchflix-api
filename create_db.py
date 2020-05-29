from matchflix.extensions.db import database as db
import os
import asyncio


async def main():
    await db.connect()
    if os.path.exists("db.sqlite3"):
        os.remove("db.sqlite3")
    query = """CREATE TABLE movies ( 
        id VARCHAR(32)  NOT NULL PRIMARY KEY, 
        title VARCHAR(50)  NOT NULL,
        description VARCHAR(1000)  NOT NULL,
        cover VARCHAR(200)  NOT NULL,
        tmdb_id INTEGER NOT NULL
    ); """
    await db.execute(query)

    query = """CREATE TABLE users ( 
            id VARCHAR(32)  NOT NULL PRIMARY KEY, 
            email VARCHAR(200)  NOT NULL
        ); """
    await db.execute(query)

    query = """CREATE TABLE user_movies ( 
            id VARCHAR(32)  NOT NULL PRIMARY KEY, 
            movie_id VARCHAR(32)  NOT NULL,
            user_id VARCHAR(32)  NOT NULL,
            action VARCHAR(10)  NOT NULL
        ); """
    await db.execute(query)


if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    result = loop.run_until_complete(main())
