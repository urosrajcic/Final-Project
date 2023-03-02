from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship

from app.db import Base


class GroupComments(Base):
    __tablename__ = "group_comments"

    artist_id = Column(String(50), ForeignKey("group.id"), primary_key=True)
    comment_id = Column(String(50), ForeignKey("comment.id"), primary_key=True)

    group = relationship("Group", backref="group_comments")
    comment = relationship("Comment", backref="group_comments")
