from fastapi import APIRouter
from app.album.controller import AlbumController
from app.album.schemas import *

album_router = APIRouter(tags=["albums"], prefix="/mdb/albums")


@album_router.post("/add-new-album", response_model=AlbumSchema)
def create_album(album: AlbumSchemaIn):
    return AlbumController.create_album(album.name, album.length, album.date_of_release)


@album_router.get("/get-album-by-id", response_model=AlbumSchema)
def get_album_by_id(id: str):
    return AlbumController.get_album_by_id(id)


@album_router.get("/get-albums-by-name", response_model=list[AlbumSchema])
def get_albums_by_name(name: str):
    return AlbumController.get_album_by_name(name)


@album_router.get("/get-all-albums", response_model=list[AlbumSchema])
def get_all_albums():
    return AlbumController.get_all_albums()


@album_router.get("/get-albums-by-rating", response_model=list[AlbumSchema])
def get_albums_by_rating():
    return AlbumController.get_albums_by_rating()


@album_router.delete("/delete-album-by-id")
def delete_album_by_id(id: str):
    return AlbumController.delete_album_by_id(id)


@album_router.put("/update-album-by-id", response_model=AlbumSchema)
def update_album(id: str, name=None, length=None, date_of_release=None, items_sold=None, ratings=None,
                 explicit=None, lp=None, ep=None, single=None, mixtape=None):
    return AlbumController.update_album(id, name, length, date_of_release, items_sold, ratings, explicit, lp, ep,
                                        single, mixtape)


@album_router.put("/add-artist-to-album", response_model=AlbumSchema)
def add_artist_to_album(album_id: str, artist_id: str):
    return AlbumController.add_artist_to_album(album_id, artist_id)


@album_router.put("/add-song-to-album", response_model=AlbumSchema)
def add_song_to_album(album_id: str, song_id: str):
    return AlbumController.add_song_to_album(album_id, song_id)


@album_router.put("/add-award-to-album", response_model=AlbumSchema)
def add_award_to_album(album_id: str, award_id: str):
    return AlbumController.add_award_to_album(album_id, award_id)


@album_router.put("/add-genre-to-album", response_model=AlbumSchema)
def add_genre_to_album(album_id: str, genre_name: str):
    return AlbumController.add_genre_to_album(album_id, genre_name)


@album_router.put("/add-comment-to-album", response_model=AlbumSchema)
def add_comment_to_album(album_id: str, comment_id: str):
    return AlbumController.add_comment_to_album(album_id, comment_id)


@album_router.put("/remove-artist-from-album", response_model=AlbumSchema)
def remove_artist_from_album(album_id: str, artist_id: str):
    return AlbumController.remove_artist_from_album(album_id, artist_id)


@album_router.put("/remove-song-from-album", response_model=AlbumSchema)
def remove_song_from_album(album_id: str, song_id: str):
    return AlbumController.remove_song_from_album(album_id, song_id)


@album_router.put("/remove-award-from-album", response_model=AlbumSchema)
def remove_award_from_album(album_id: str, award_id: str):
    return AlbumController.remove_award_from_album(album_id, award_id)


@album_router.put("/remove-genre-from-album", response_model=AlbumSchema)
def remove_genre_from_album(album_id: str, genre_name: str):
    return AlbumController.remove_genre_from_album(album_id, genre_name)


@album_router.put("/remove-comment-from-album", response_model=AlbumSchema)
def remove_comment_from_album(album_id: str, comment_id: str):
    return AlbumController.remove_comment_from_album(album_id, comment_id)
