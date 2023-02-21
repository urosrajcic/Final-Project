from sqlalchemy.orm import relationship

from app.db.database import Base
from sqlalchemy import Column, String, Boolean, Date, ForeignKey


class User(Base):
    __tablename__ = "user"
    username = Column(String(50), primary_key=True, autoincrement=False)
    email = Column(String(100), unique=True)
    password = Column(String(100))
    name = Column(String(25))
    surname = Column(String(25))
    date_of_birth = Column(Date)
    critic = Column(Boolean, default=False)
    writer = Column(Boolean, default=False)

    country_name = Column(String(25), ForeignKey("country.name"), nullable=False, index=True)
    country = relationship("Country", lazy="subquery")

    def __init__(self, username: str,
                 email: str,
                 password: str,
                 name: str,
                 surname: str,
                 date_of_birth: str,
                 country_name: str,
                 critic: bool = False,
                 writer: bool = False
                 ):
        self.username = username
        self.email = email
        self.password = password
        self.name = name
        self.surname = surname
        self.date_of_birth = date_of_birth.strftime("%Y-%m-%d")
        self.country_name = country_name
        self.critic = critic
        self.writer = writer

    def __repr__(self):
        return f"username: {self.username}," \
               f"name: {self.name}," \
               f"surname: {self.surname}," \
               f"country: {self.country_name}," \
               f"date of birth: {self.date_of_birth}," \
               f"critic: {self.critic}," \
               f"writer: {self.writer}"
