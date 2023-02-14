from fastapi import HTTPException, Response, status
from pydantic.datetime_parse import date
from app.album.exceptions import *
from app.album.services import AlbumServices


class AlbumController:
    @staticmethod
    def create_album(name: str, date_of_release: date, song_id: str, artist_id: str):
        try:
            album = AlbumServices.create_album(name, date_of_release, song_id, artist_id)
            return album
        except AlbumNotFoundException as _e:
            raise HTTPException(status_code=_e.code, detail=_e.message)
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))

    @staticmethod
    def get_album_by_id(id: str):
        try:
            album = AlbumServices.get_album_by_id(id)
            if album:
                return album
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Album with provided id: "
                                                                                f"{id}, does not exist.")
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))

    @staticmethod
    def get_album_by_name(name: str):
        try:
            albums = AlbumServices.get_album_by_name(name)
            if albums:
                return albums
        except AlbumNotFoundException as _e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Album with provided name: "
                                                                                f"{name}, does not exist.")
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))

    @staticmethod
    def get_all_albums():
        albums = AlbumServices.get_all_albums()
        return albums

    @staticmethod
    def delete_album_by_id(id: str):
        try:
            AlbumServices.delete_album_by_id(id)
            return Response(content=f"Album with provided id: {id} is deleted.")
        except AlbumNotFoundException as _e:
            raise HTTPException(status_code=_e.code, detail=_e.message)
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))

    @staticmethod
    def update_album(id: str, name=None, length=None, date_of_release=None, items_sold=None, ratings=None,
                     explicit=None, lp=None, ep=None, single=None, mixtape=None, song_id=None, artis_id=None,
                     genre_name=None, award_id=None, user_username=None, record_label_id=None):
        try:
            album = AlbumServices.update_album(id, name, length, date_of_release, items_sold, ratings, explicit, lp, ep,
                                               single, mixtape, song_id, artis_id, genre_name, award_id, user_username,
                                               record_label_id)
            return album
        except AlbumNotFoundException as _e:
            raise HTTPException(status_code=_e.code, detail=_e.message)
        except Exception as _e:
            raise _e
