from app.db.database import Base
from sqlalchemy import Column, String


class Genre(Base):
    __tablename__ = "genre"
    name = Column(String(50), primary_key=True, autoincrement=False)

    def __init__(self, name):
        self.name = name

