from pydantic import BaseModel, UUID4
from pydantic.datetime_parse import date
from app.award.schemas import AwardSchema
from app.country.schemas import CountrySchema
from app.genre import GenreSchema
from app.record_label.schemas import RecordLabelSchema


class ArtistSchema(BaseModel):
    id: UUID4
    name: str
    date_of_birth: date
    date_of_death: date
    ratings: float
    vocalist: bool
    musician: bool
    producer: bool
    writer: bool
    engineer: bool
    biography: str

    country_name: str
    country: CountrySchema
    genre_name: str
    genre: GenreSchema
    award_name: str
    award: AwardSchema
    record_label_id: str
    record_label: RecordLabelSchema

    class Config:
        orm_mode = True


class ArtistSchemaIn(BaseModel):
    name: str
    country_name: str
    date_of_birth: str

    class Config:
        orm_mode = True
