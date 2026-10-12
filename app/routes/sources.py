from fastapi import APIRouter, HTTPException
from app.providers.registry import get_provider
router = APIRouter(tags=["Sources"])

@router.get("/sources/{item_id}")
async def sources(item_id: str, type: str = "movie"):
    provider = get_provider()
    if provider is None:
        raise HTTPException(status_code=501, detail="No provider adapter configured yet.")
    return await provider.sources(item_id=item_id, content_type=type)
