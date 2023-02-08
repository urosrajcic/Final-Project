from uuid import uuid4
from app.db.database import Base
from sqlalchemy import Column, String, Date, Boolean


class CEO(Base):
    __table_name__ = "CEO"
    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    name = Column(String(50))
    surname = Column(String(50))
    date_of_birth = Column(Date)
    from_date = Column(Date)
    too_date = Column(Date, nullable=True)
    active = Column(Boolean, default=True)

    def __init__(self, name, surname, date_of_birth, from_date, too_date, active):
        self.name = name
        self.surname = surname
        self.date_of_birth = date_of_birth
        self.from_date = from_date
        self.too_date = too_date
        self.active = active
