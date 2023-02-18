from uuid import uuid4
from app.db.database import Base
from sqlalchemy import Column, String, Date


class Award(Base):
    __tablename__ = "award"
    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    name = Column(String(50))
    award_date = Column(Date, nullable=True)

    def __init__(self, name, award_date):
        self.name = name
        self.award_date = award_date
