from pydantic import BaseModel, UUID4


class GenreSchemas(BaseModel):
    name: str

    song_id: UUID4
    artist_id: UUID4
    album_id: UUID4

    class Config:
        orm_mode = True


class GenreSchemasIn(BaseModel):
    name: str

    class Config:
        orm_mode = True
