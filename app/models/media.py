from pydantic import BaseModel
from typing import Optional

class MediaItem(BaseModel):
    id: str
    title: str
    media_type: str
    year: Optional[int] = None
    poster_url: Optional[str] = None

class StreamFormat(BaseModel):
    id: str
    quality: str
    container: Optional[str] = None
    mime_type: Optional[str] = None
    url: Optional[str] = None
