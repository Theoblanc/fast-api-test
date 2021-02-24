from typing import Optional
from pydantic import BaseModel


class YoutubeList(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
