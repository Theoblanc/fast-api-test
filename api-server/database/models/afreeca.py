from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from database import Base


class AfreecaList(Base):
    __tablename__ = "afreeca"

    id = Column(Integer, primary_key=True, index=True)
    bj_id = Column(String, index=True)
    bj_name = Column(String, index=True)
    bj_medals = relationship("Medal", back_populates="")
    bj_categorys = relationship("Category", back_populates="")
    bj_thumbnail = Column(String)
    bj_banner = Column(String)
    bj_average_view = Column(Integer)
    bj_bookmark_count = Column(Integer)
    bj_cumulative_viewers = Column(Integer)  ##필요?
    bj_max_viewrs = Column(Integer)
    bj_up_count = Column(Integer)
    bj_subscription_count = Column(Integer)
    bj_fan_count = Column(Integer)
    publishedAt = Column(Integer)
    video = relationship("Category", back_populates="")
    snses = relationship("Category", back_populates="")
    updatedAt = DateTime
    deletedAt = DateTime