from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship

from app.db import Base


class GroupGenres(Base):
    __tablename__ = "group_genres"

    group_id = Column(String(50), ForeignKey("group.id"), primary_key=True)
    genre_name = Column(String(50), ForeignKey("genre.name"), primary_key=True)

    group = relationship("Group", backref="group_genres")
    genre = relationship("Genre", backref="group_genres")
