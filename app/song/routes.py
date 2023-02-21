from fastapi import APIRouter
from app.song.controller import SongController
from app.song.schemas import *

song_router = APIRouter(tags=["songs"], prefix="/mdb/songs")


@song_router.post("/add-new-song", response_model=SongSchema)
def create_song(song: SongSchemaIn):
    return SongController.create_song(song.name, song.length, song.date_of_release)


@song_router.get("/get-song-by-id", response_model=SongSchema)
def get_song_by_id(id: str):
    return SongController.get_song_by_id(id)


@song_router.get("/get-songs-by-characters", response_model=list[SongSchema])
def get_songs_by_characters(characters: str):
    return SongController.get_songs_by_characters(characters)


@song_router.get("/get-all-songs", response_model=list[SongSchema])
def get_all_songs():
    return SongController.get_all_songs()


@song_router.get("/get-songs-by-rating", response_model=list[SongSchema])
def get_songs_by_rating():
    return SongController.get_songs_by_rating()


@song_router.delete("/delete-song-by-id")
def delete_song_by_id(id: str):
    return SongController.delete_song_by_id(id)


@song_router.put("/update-song-by-id", response_model=SongSchema)
def update_song(id: str, name=None, length=None, date_of_release=None, items_sold=None, lyrics=None,
                ratings=None, explicit=None):
    return SongController.update_song(id, name, length, date_of_release, items_sold, lyrics, ratings, explicit)


@song_router.put("/add-artist-to-song", response_model=SongSchema)
def add_artist_to_song(song_id: str, artist_id: str):
    return SongController.add_artist_to_song(song_id, artist_id)


@song_router.put("/add-album-to-song", response_model=SongSchema)
def add_album_to_song(song_id: str, album_id: str):
    return SongController.add_album_to_song(song_id, album_id)


@song_router.put("/add-award-to-song", response_model=SongSchema)
def add_award_to_song(song_id: str, award_id: str):
    return SongController.add_award_to_song(song_id, award_id)


@song_router.put("/add-genre-to-song", response_model=SongSchema)
def add_genre_to_song(song_id: str, genre_name: str):
    return SongController.add_genre_to_song(song_id, genre_name)


@song_router.put("/add-comment-to-song", response_model=SongSchema)
def add_comment_to_song(song_id: str, comment_id: str):
    return SongController.add_comment_to_song(song_id, comment_id)


@song_router.put("/remove-artist-from-song", response_model=SongSchema)
def remove_artist_to_song(song_id: str, artist_id: str):
    return SongController.remove_artist_from_song(song_id, artist_id)


@song_router.put("/remove-album-from-song", response_model=SongSchema)
def remove_album_from_song(song_id: str, album_id: str):
    return SongController.remove_album_from_song(song_id, album_id)


@song_router.put("/remove-award-from-song", response_model=SongSchema)
def remove_award_from_song(song_id: str, award_id: str):
    return SongController.remove_award_from_song(song_id, award_id)


@song_router.put("/remove-genre-from-song", response_model=SongSchema)
def remove_genre_from_song(song_id: str, genre_name: str):
    return SongController.remove_genre_from_song(song_id, genre_name)


@song_router.put("/remove-comment-from-song", response_model=SongSchema)
def remove_comment_from_song(song_id: str, comment_id: str):
    return SongController.remove_comment_from_song(song_id, comment_id)
