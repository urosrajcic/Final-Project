from uuid import uuid4
from app.db.database import Base
from sqlalchemy import Column, String, Date


class Award(Base):
    __tablename__ = "award"
    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    name = Column(String(50))
    category = Column(String(50))
    award_date = Column(Date, nullable=True)

    def __init__(self, name: str, category: str, award_date: str):
        self.name = name
        self.category = category
        self.award_date = award_date.strftime("%Y-%m-%d")
