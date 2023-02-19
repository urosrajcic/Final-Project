from datetime import date
from typing import Optional

from sqlalchemy.orm import relationship
from app.db.database import Base
from sqlalchemy import Column, String, Date, Float, Boolean, ForeignKey, Text
from uuid import uuid4


class Artist(Base):
    __tablename__ = "artist"

    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    name = Column(String(50))
    date_of_birth = Column(Date, nullable=True)
    date_of_death = Column(Date, nullable=True)
    ratings = Column(Float, nullable=True)
    vocalist = Column(Boolean, default=False, nullable=True)
    musician = Column(Boolean, default=False, nullable=True)
    producer = Column(Boolean, default=False, nullable=True)
    writer = Column(Boolean, default=False, nullable=True)
    engineer = Column(Boolean, default=False, nullable=True)
    biography = Column(Text, nullable=True)

    country_name = Column(String(25), ForeignKey("country.name"), nullable=False, index=True)
    country = relationship("Country", lazy="subquery")
    genre_name = Column(String(25), ForeignKey("genre.name"), nullable=True, index=True)
    genre = relationship("Genre", lazy="subquery")
    award_id = Column(String(25), ForeignKey("award.id"), nullable=True)
    award = relationship("Award", lazy="subquery")
    record_label_id = Column(String(25), ForeignKey("record_label.id"), nullable=True)
    record_label = relationship("RecordLabel", lazy="subquery")

    def __init__(self, name: str,
                 country_name: str,
                 date_of_birth: str,
                 date_of_death: Optional[date] = None,
                 ratings: Optional[float] = None,
                 vocalist: Optional[bool] = False,
                 musician: Optional[bool] = False,
                 producer: Optional[bool] = False,
                 writer: Optional[bool] = False,
                 engineer: Optional[bool] = False,
                 biography: Optional[str] = None,
                 genre_name: Optional[str] = None,
                 award_id: Optional[str] = None,
                 record_label_id: Optional[str] = None,
                 ):
        self.name = name
        self.country_name = country_name
        self.date_of_birth = date_of_birth.strftime("%Y-%m-%d")
        self.date_of_death = date_of_death
        self.ratings = ratings
        self.vocalist = vocalist
        self.musician = musician
        self.producer = producer
        self.writer = writer
        self.engineer = engineer
        self.biography = biography
        self.genre_name = genre_name
        self.award_id = award_id
        self.record_label_id = record_label_id
