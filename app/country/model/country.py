from app.db.database import Base
from sqlalchemy import Column, String


class Country(Base):
    __tablename__ = "country"
    name = Column(String(50), primary_key=True, autoincrement=False)

    def __init__(self, name):
        self.name = name
