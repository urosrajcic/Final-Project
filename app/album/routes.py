from fastapi import APIRouter
from app.album.controller import AlbumController
from app.album.schemas import *

album_router = APIRouter(tags=["albums"], prefix="/mdb/albums")


@album_router.post("/add-new-album", response_model=AlbumSchema)
def create_album(album: AlbumSchemaIn):
    return AlbumController.create_album(album.name, album.date_of_release, album.song_id, album.artist_id)


@album_router.get("/get-album-by-id", response_model=AlbumSchema)
def get_album_by_id(id: str):
    return AlbumController.get_album_by_id(id)


@album_router.get("/get-albums-by-name", response_model=list[AlbumSchema])
def get_albums_by_name(name: str):
    return AlbumController.get_album_by_name(name)


@album_router.get("/get-albums-by-artist", response_model=list[AlbumSchema])
def get_albums_by_name(artist_id: str):
    return AlbumController.get_albums_by_artist(artist_id)


@album_router.get("/get-all-albums", response_model=list[AlbumSchema])
def get_all_albums():
    return AlbumController.get_all_albums()


@album_router.delete("/delete-album-by-id")
def delete_album_by_id(id: str):
    return AlbumController.delete_album_by_id(id)


@album_router.put("/update-album-by-id", response_model=AlbumSchema)
def update_album(id: str, name=None, length=None, date_of_release=None, items_sold=None, ratings=None,
                 explicit=None, lp=None, ep=None, single=None, mixtape=None, song_id=None, artis_id=None,
                 genre_name=None, award_id=None):
    return AlbumController.update_album(id, name, length, date_of_release, items_sold, ratings, explicit, lp, ep,
                                        single, mixtape, song_id, artis_id, genre_name, award_id)
