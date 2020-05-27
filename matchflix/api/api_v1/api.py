from fastapi import APIRouter

from matchflix.api.api_v1.endpoints import answer, release

api_router = APIRouter()
api_router.include_router(release.router, prefix="/releases", tags=["releases"])
api_router.include_router(answer.router, prefix="/answers", tags=["answers"])
