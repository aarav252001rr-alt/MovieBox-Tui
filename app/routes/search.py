from fastapi import APIRouter, HTTPException, Query
from app.providers.registry import get_provider
router = APIRouter(tags=["Search"])

@router.get("/search")
async def search(q: str = Query(min_length=1), type: str = "all"):
    provider = get_provider()
    if provider is None:
        raise HTTPException(status_code=501, detail="No provider adapter configured yet.")
    return await provider.search(q=q, content_type=type)
