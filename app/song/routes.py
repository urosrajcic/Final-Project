from fastapi import APIRouter
from app.song.controller import SongController
from app.song.schemas import *

song_router = APIRouter(tags=["songs"], prefix="/mdb/songs")


@song_router.post("/add-new-song", response_model=SongSchema)
def create_song(song: SongSchemaIn):
    return SongController.create_song(song.name, song.length, song.date_of_release, song.artist_id)


@song_router.post("/add-new-explicit-song", response_model=SongSchema)
def create_explicit_song(song: SongSchemaIn):
    return SongController.create_explicit_song(song.name, song.length, song.date_of_release, song.artist_id)


@song_router.get("/get-song-by-id", response_model=SongSchema)
def get_song_by_id(id: str):
    return SongController.get_song_by_id(id)


@song_router.get("/get-songs-by-characters", response_model=list[SongSchema])
def get_songs_by_characters(characters: str):
    return SongController.get_songs_by_characters(characters)


@song_router.get("/get-all-songs", response_model=list[SongSchema])
def get_all_songs():
    return SongController.get_all_songs()


@song_router.delete("/delete-song-by-id")
def delete_song_by_id(id: str):
    return SongController.delete_song_by_id(id)


@song_router.put("/update-song-by-id", response_model=SongSchema)
def update_song(id: str, name=None, length=None, items_sold=None, lyrics=None, date_of_release=None,
                ratings=None, explicit=None, artist_id=None, genre_name=None, award_name=None):
    return SongController.update_song(id, name, length, items_sold, lyrics, date_of_release, ratings,
                                      explicit, artist_id, genre_name, award_name)
