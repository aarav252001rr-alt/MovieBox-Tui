from fastapi import APIRouter
router = APIRouter(tags=["Streams"])

@router.get("/formats/{item_id}")
def formats(item_id: str):
    return {
        "item_id": item_id,
        "formats": [],
        "configured": False,
        "message": "Format listing depends on an implemented provider adapter."
    }

@router.get("/stream/{item_id}")
def stream_info(item_id: str):
    return {
        "item_id": item_id,
        "stream_url": None,
        "configured": False,
        "message": "No stream URL is generated until a compatible provider adapter is configured."
    }
