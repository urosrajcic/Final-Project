from fastapi import APIRouter

from app.artist.controller import ArtistController
from app.artist.schemas import ArtistSchema, ArtistSchemaIn

artist_router = APIRouter(tags=["artists"], prefix="/mdb/artists")


@artist_router.post("/add-new-artist", response_model=ArtistSchema)
def create_artist(artist: ArtistSchemaIn):
    return ArtistController.create_artist(name=artist.name, country_name=artist.country_name,
                                          date_of_birth=artist.date_of_birth)


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
def update_artist(id: str, name=None, date_of_birth=None, date_of_death=None, vocalist=None,
                  musician=None, producer=None, writer=None, engineer=None, biography=None,
                  country_name=None, record_label_id=None):
    return ArtistController.update_artist(id, name, date_of_birth, date_of_death, vocalist,
                                          musician, producer, writer, engineer, biography,
                                          country_name, record_label_id)


@artist_router.put("/add-song-to-artist", response_model=ArtistSchema)
def add_song_to_artist(artist_id: str, song_id: str):
    return ArtistController.add_song_to_artist(artist_id, song_id)


@artist_router.put("/add-album-to-artist", response_model=ArtistSchema)
def add_album_to_artist(artist_id: str, album_id: str):
    return ArtistController.add_album_to_artist(artist_id, album_id)


@artist_router.put("/add-award-to-artist", response_model=ArtistSchema)
def add_award_to_artist(artist_id: str, award_id: str):
    return ArtistController.add_award_to_artist(artist_id, award_id)


@artist_router.put("/add-genre-to-artist", response_model=ArtistSchema)
def add_genre_to_artist(artist_id: str, genre_name: str):
    return ArtistController.add_genre_to_artist(artist_id, genre_name)
