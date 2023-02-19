from fastapi import APIRouter

from app.artist.controller import ArtistController
from app.artist.schemas import ArtistSchema, ArtistSchemaIn
from app.song.schemas import SongSchema

artist_router = APIRouter(tags=["artists"], prefix="/mdb/artists")


@artist_router.post("/add-new-artist")
def create_artist(artist: ArtistSchemaIn):
    return ArtistController.create_artist(name=artist.name, country_name=artist.country_name,
                                          date_of_birth=artist.date_of_birth)


@artist_router.get("/get-artist-by-id")
def get_artist_by_id(id: str):
    return ArtistController.get_artist_by_id(id)


@artist_router.get("/get-artists-by-name")
def get_artists_by_name(name: str):
    return ArtistController.get_artist_by_name(name)


@artist_router.get("/get-all-artists")
def get_all_artists():
    return ArtistController.get_all_artists()


@artist_router.delete("/delete-artist-by-id")
def delete_artist_by_id(id: str):
    return ArtistController.delete_artist_by_id(id)


@artist_router.put("/update-artist-by-id")
def update_artist(id: str, name=None, date_of_birth=None, date_of_death=None, ratings=None, vocalist=None,
                  musician=None, producer=None, writer=None, engineer=None, biography=None,
                  genre_name=None, award_id=None, country_name=None, record_label_id=None):
    return ArtistController.update_artist(id, name, date_of_birth, date_of_death, ratings, vocalist,
                                          musician, producer, writer, engineer, biography,
                                          genre_name, award_id, country_name, record_label_id)


@artist_router.put("/add-song-to-artist")
def add_song_to_artist(artist_id: str, song_id: str):
    return ArtistController.add_song_to_artist(artist_id, song_id)
