from sqlalchemy.orm import relationship
from app.db.database import Base
from sqlalchemy import Column, String, Date, Float, Boolean, ForeignKey
from uuid import uuid4


class Artist(Base):
    __tablename__ = "artist"

    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    name = Column(String(50))
    date_of_birth = Column(Date, nullable=True)
    date_of_death = Column(Date, nullable=True)
    ratings = Column(Float, nullable=True)
    vocalist = Column(Boolean, default=True)
    musician = Column(Boolean, default=True)
    producer = Column(Boolean, default=True)
    writer = Column(Boolean, default=True)
    engineer = Column(Boolean, default=True)
    biography = Column(String(500), nullable=True)

    country_name = Column(String(25), ForeignKey("country.name"), nullable=False)
    country = relationship("Country", lazy="subquery")
    genre_name = Column(String(25), ForeignKey("genre.name"), nullable=True)
    genre = relationship("Genre", lazy="subquery")
    award_id = Column(String(25), ForeignKey("award.id"), nullable=True)
    award = relationship("Award", lazy="subquery")
    record_label_id = Column(String(25), ForeignKey("record_label.id"), nullable=True)
    record_label = relationship("RecordLabel", lazy="subquery")

    def __init__(self, name: str,
                 country_name: str,
                 date_of_birth: str,
                 date_of_death: str = "0000-00-00",
                 ratings: float = 0,
                 vocalist: bool = False,
                 musician: bool = False,
                 producer: bool = False,
                 writer: bool = False,
                 engineer: bool = False,
                 biography: str = "",
                 genre_name: str = "",
                 award_id: str = "",
                 record_label_id: str = ""
                 ):
        self.name = name
        self.country_name = country_name
        self.date_of_birth = date_of_birth
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
