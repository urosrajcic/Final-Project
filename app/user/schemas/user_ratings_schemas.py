from typing import Optional

from pydantic import BaseModel, UUID4


class UserRatingAlbumSchema(BaseModel):
    id: UUID4
    user_username: str
    album_id: Optional[UUID4]
    rating: int

    class Config:
        orm_mode = True


class UserRatingArtistSchema(BaseModel):
    id: UUID4
    user_username: str
    artist_id: Optional[UUID4]
    rating: int

    class Config:
        orm_mode = True


class UserRatingSongSchema(BaseModel):
    id: UUID4
    user_username: str
    song_id: Optional[UUID4]
    rating: int

    class Config:
        orm_mode = True


class UserRatingAlbumSchemaIn(BaseModel):
    user_username: str
    rating: int
    album_id: str

    class Config:
        orm_mode = True


class UserRatingArtistSchemaIn(BaseModel):
    user_username: str
    rating: int
    artist_id: str

    class Config:
        orm_mode = True


class UserRatingSongSchemaIn(BaseModel):
    user_username: str
    rating: int
    song_id: str

    class Config:
        orm_mode = True
