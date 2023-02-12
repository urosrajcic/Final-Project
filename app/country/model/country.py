from app.db.database import Base
from sqlalchemy import Column, String


class Country(Base):
    __table_name__ = "country"
    name = Column(String(50), primary_key=True, autoincrement=False)

    def __init__(self, name):
        self.name = name
