from uuid import uuid4

from sqlalchemy.orm import relationship

from app.db.database import Base
from sqlalchemy import Column, String, Date, UniqueConstraint


class Award(Base):
    __tablename__ = "award"
    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    name = Column(String(50))
    category = Column(String(50))
    award_date = Column(Date, nullable=True)

    artist = relationship("Artist", secondary="artist_awards", lazy="subquery")
    group = relationship("Group", secondary="group_awards", lazy="subquery")
    album = relationship("Album", secondary="album_awards", lazy="subquery")
    song = relationship("Song", secondary="song_awards", lazy="subquery")
    __table_args__ = (UniqueConstraint("name", "category", "award_date", name="award_uc"),)

    def __init__(self, name: str, category: str, award_date: str):
        self.name = name
        self.category = category
        self.award_date = award_date.strftime("%Y-%m-%d")
