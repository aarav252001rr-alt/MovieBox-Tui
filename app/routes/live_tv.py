from fastapi import APIRouter
router = APIRouter(prefix="/live-tv", tags=["Live TV"])

@router.get("")
def live_tv_info():
    return {
        "items": [],
        "configured": False,
        "message": "Configure a lawful M3U/IPTV source before using this endpoint."
    }
