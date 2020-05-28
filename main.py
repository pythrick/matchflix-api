from dynaconf import settings
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from matchflix.api.api_v1.api import api_router
from matchflix.db.session import database

app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json"
)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


# f"https://api.themoviedb.org/3/movie/671/recommendations?api_key={settings.TMDB_API_KEY}&language=en-US&page=1"
# f"https://api.themoviedb.org/3/movie/448665/similar?api_key={settings.TMDB_API_KEY}&language=en-US&page=1"

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(api_router, prefix=settings.API_V1_STR)
