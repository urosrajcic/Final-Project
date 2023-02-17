from uuid import uuid4

from sqlalchemy.orm import relationship

from app.db.database import Base
from sqlalchemy import Column, String, ForeignKey, Date, Float


class RecordLabel(Base):
    __tablename__ = "record_label"
    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    name = Column(String(50))
    address = Column(String(50))
    date_founded = Column(Date)
    ratings = Column(Float, nullable=True)
    biography = Column(String(500), nullable=True)
    ceo = Column(String(50))

    country_name = Column(String(25), ForeignKey("country.name"), nullable=False)
    country = relationship("Country", lazy="subquery")

    def __init__(self, name, address, date_founded, ratings=None, biography=None, ceo=ceo,
                 country_name=country_name):
        self.name = name
        self.address = address
        self.date_founded = date_founded
        self.ratings = ratings
        self.biography = biography
        self.ceo = ceo
        self.country_name = country_name
