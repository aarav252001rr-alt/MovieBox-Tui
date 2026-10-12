from fastapi import APIRouter
router = APIRouter(prefix="/subtitles", tags=["Subtitles"])

@router.get("/{item_id}")
def subtitles(item_id: str):
    return {
        "item_id": item_id,
        "subtitles": [],
        "configured": False
    }
