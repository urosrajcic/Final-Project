from fastapi import APIRouter
from app.artist.controller import ArtistController
from app.artist.schemas import *

artist_router = APIRouter(tags=["artists"], prefix="/mdb/artists")


@artist_router.post("/add-new-artist", response_model=ArtistSchema)
def create_artist(artist: ArtistSchemaIn):
    return ArtistController.create_artist(artist.name)


@artist_router.get("/get-artist-by-id", response_model=ArtistSchema)
def get_artist_by_id(id: str):
    return ArtistController.get_artist_by_id(id)


@artist_router.get("/get-artists-by-name", response_model=list[ArtistSchema])
def get_artists_by_name(name: str):
    return ArtistController.get_artist_by_name(name)


@artist_router.get("/get-all-artists", response_model=list[ArtistSchema])
def get_all_artists():
    return ArtistController.get_all_artists()


@artist_router.delete("/delete-artist-by-id")
def delete_artist_by_id(id: str):
    return ArtistController.delete_artist_by_id(id)


@artist_router.put("/update-artist-by-id", response_model=ArtistSchema)
def update_artist(id: str, name=None, date_of_birth=None, date_of_death=None, ratings=None, vocalist=None,
                  musician=None, producer=None, writer=None, engineer=None, biography=None, album_id=None,
                  song_id=None, genre_name=None, award_id=None, country_name=None, user_username=None,
                  record_label_id=None):
    return ArtistController.update_artist(id, name, date_of_birth, date_of_death, ratings, vocalist,
                                          musician, producer, writer, engineer, biography, album_id,
                                          song_id, genre_name, award_id, country_name, user_username,
                                          record_label_id)
