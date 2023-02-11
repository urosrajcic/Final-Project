from uuid import uuid4
from app.db.database import Base
from sqlalchemy import Column, String, ForeignKey, Date, Float


class RecordLabel(Base):
    __table_name__ = "record_label"
    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    name = Column(String(50))
    address = Column(String(50))
    date_founded = Column(Date)
    ratings = Column(Float)
    biography = Column(String(500))

    country_name = Column(String(25), ForeignKey("country.name"), nullable=False)
    ceo_id = Column(String(50), ForeignKey("ceo.id"), nullable=False)

    def __init__(self, name, address, date_founded, ratings, biography, country_name, ceo_id):
        self.name = name
        self.address = address
        self.date_founded = date_founded
        self.ratings = ratings
        self.biography = biography
        self.country_name = country_name
        self.ceo_id = ceo_id
