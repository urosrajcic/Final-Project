from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship

from app.db import Base


class GroupAwards(Base):
    __tablename__ = "group_awards"

    group_id = Column(String(50), ForeignKey("group.id"), primary_key=True)
    award_id = Column(String(50), ForeignKey("award.id"), primary_key=True)

    group = relationship("Group", backref="group_award")
    award = relationship("Award", backref="group_award")
