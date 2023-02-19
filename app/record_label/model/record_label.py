from typing import Optional
from uuid import uuid4
from sqlalchemy.orm import relationship
from app.db.database import Base
from sqlalchemy import Column, String, ForeignKey, Date, Float, Text


class RecordLabel(Base):
    __tablename__ = "record_label"
    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    name = Column(String(50))
    address = Column(String(50))
    date_founded = Column(Date)
    ceo = Column(String(50))
    ratings = Column(Float, nullable=True)
    biography = Column(Text, nullable=True)

    country_name = Column(String(25), ForeignKey("country.name"), nullable=False, index=True)
    country = relationship("Country", lazy="subquery")

    def __init__(self, name: str,
                 address: str,
                 date_founded: str,
                 ceo: str = ceo,
                 country_name: str = country_name,
                 ratings: Optional[float] = 0,
                 biography: Optional[str] = ""):
        self.name = name
        self.address = address
        self.date_founded = date_founded.strftime("%Y-%m-%d")
        self.ceo = ceo
        self.country_name = country_name
        self.ratings = ratings
        self.biography = biography

