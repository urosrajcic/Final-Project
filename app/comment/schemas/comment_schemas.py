from datetime import datetime
from typing import Optional

from pydantic import BaseModel, UUID4

from app.user.schemas import UserSchema


class CommentSchema(BaseModel):
    id: UUID4
    header: str
    text: str
    date_time: datetime
    ratings: Optional[float]

    user_username: str
    user: UserSchema

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


class CommentSchemaIn(BaseModel):
    header: str
    text: str
    date_time: datetime
    user_username: str

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True
