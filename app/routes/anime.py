from fastapi import APIRouter, HTTPException, Query
from app.providers.registry import get_provider
router = APIRouter(prefix="/anime", tags=["Anime"])

@router.get("/search")
async def anime_search(q: str = Query(min_length=1)):
    provider = get_provider()
    if provider is None:
        raise HTTPException(status_code=501, detail="No provider adapter configured yet.")
    return await provider.search(q=q, content_type="anime")
