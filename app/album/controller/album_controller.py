from fastapi import HTTPException, Response, status
from app.album.exceptions import *
from app.album.services import AlbumServices


class AlbumController:
    @staticmethod
    def create_album(name: str, length: int, date_of_release: str):
        try:
            album = AlbumServices.create_album(name, length, date_of_release)
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
                     explicit=None, lp=None, ep=None, single=None, mixtape=None):
        try:
            album = AlbumServices.update_album(id, name, length, date_of_release, items_sold, ratings, explicit, lp, ep,
                                               single, mixtape)
            return album
        except AlbumNotFoundException as _e:
            raise HTTPException(status_code=_e.code, detail=_e.message)
        except Exception as _e:
            raise _e

    @staticmethod
    def add_artist_to_album(album_id: str, artist_id: str):
        try:
            album = AlbumServices.add_artist_to_album(album_id, artist_id)
            if album:
                return album
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Album with provided id: "
                                                                                f"{album_id}, does not exist.")
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))

    @staticmethod
    def add_song_to_album(album_id: str, song_id: str):
        try:
            album = AlbumServices.add_song_to_album(album_id, song_id)
            if album:
                return album
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Album with provided id: "
                                                                                f"{album_id}, does not exist.")
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))

    @staticmethod
    def add_award_to_album(album_id: str, award_id: str):
        try:
            album = AlbumServices.add_award_to_album(album_id, award_id)
            if album:
                return album
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Album with provided id: "
                                                                                f"{album_id}, does not exist.")
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))

    @staticmethod
    def add_genre_to_album(album_id: str, genre_name: str):
        try:
            album = AlbumServices.add_genre_to_album(album_id, genre_name)
            if album:
                return album
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Album with provided id: "
                                                                                f"{album_id}, does not exist.")
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))
