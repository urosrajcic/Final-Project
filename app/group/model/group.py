from uuid import uuid4

from sqlalchemy import Column, String, Date, Float, Text, ForeignKey
from sqlalchemy.orm import relationship

from app.db import Base


class Group(Base):
    __tablename__ = "group"

    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    name = Column(String(50))
    date_of_forming = Column(Date, nullable=True)
    date_of_disband = Column(Date, nullable=True)
    ratings = Column(Float, nullable=True)
    biography = Column(Text, nullable=True)

    country_name = Column(String(25), ForeignKey("country.name"), nullable=False)
    country = relationship("Country", lazy="subquery")
    record_label_id = Column(String(25), ForeignKey("record_label.id"), nullable=True)
    record_label = relationship("RecordLabel", lazy="subquery")

    artists = relationship("Artist", secondary="group_artists", lazy="subquery")
    songs = relationship("Song", secondary="group_song_association", lazy="subquery")
    albums = relationship("Album", secondary="group_album_association", lazy="subquery")
    comments = relationship("Comment", secondary="group_comments", lazy="subquery")
    awards = relationship("Award", secondary="group_awards", lazy="subquery")
    genres = relationship("Genre", secondary="group_genres", lazy="subquery")

    def __init__(self, name: str,
                 country_name: str,
                 date_of_forming: str,
                 ratings: float = None
                 ):
        self.name = name
        self.country_name = country_name
        self.date_of_forming = date_of_forming.strftime("%Y-%m-%d")
        self.ratings = ratings
