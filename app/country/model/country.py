from app.db.database import Base
from sqlalchemy import Column, String


class Country(Base):
    __tablename__ = "country"
    name = Column(String(50), primary_key=True, autoincrement=False, index=True)

    def __init__(self, name: str):
        self.name = name
