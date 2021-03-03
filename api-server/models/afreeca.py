from typing import List
from datetime import datetime
from pydantic import BaseModel


class Category(BaseModel):
    id: str
    cate_name: str
    cate_no: int


class Broad(BaseModel):
    id: str


class Sns(BaseModel):
    id: str
    sns_name: str
    url: str


class AfreecaList(BaseModel):
    id: str
    bj_id: str
    bj_name: str
    bj_medals: List[str]
    bj_category: List[Category]
    bj_thumbnail: str
    bj_banner: str
    bj_average_view: int
    bj_bookmark_count: int
    bj_cumulative_viewers: int
    bj_max_viewrs: int
    bj_up_count: int
    bj_subscription_count: int
    bj_fan_count: int
    publishedAt: datetime.datetime
    video: List[Broad]
    snses: List[Sns]
    updatedAt: datetime.datetime

    class Config:
        orm_mode = True
