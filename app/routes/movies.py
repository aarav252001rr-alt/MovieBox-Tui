from fastapi import APIRouter, HTTPException
from app.providers.registry import get_provider
router = APIRouter(prefix="/movies", tags=["Movies"])

@router.get("/{item_id}")
async def movie_details(item_id: str):
    provider = get_provider()
    if provider is None:
        raise HTTPException(status_code=501, detail="No provider adapter configured yet.")
    return await provider.details(item_id=item_id, content_type="movie")
