from datetime import date
from fastapi import HTTPException, Response, status
from app.song.exceptions import *
from app.song.services import SongServices


class SongController:
    @staticmethod
    def create_song(name: str, length: int, date_of_release: date, artist_id: str):
        try:
            song = SongServices.create_song(name, length, date_of_release, artist_id)
            return song
        except SongNotFoundException as _e:
            raise HTTPException(status_code=_e.code, detail=_e.message)
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))

    @staticmethod
    def create_explicit_song(name: str, length: int, date_of_release: date, artist_id: str):
        try:
            song = SongServices.create_song(name, length, date_of_release, artist_id)
            return song
        except SongNotFoundException as _e:
            raise HTTPException(status_code=_e.code, detail=_e.message)
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))

    @staticmethod
    def get_song_by_id(id: str):
        try:
            song = SongServices.get_song_by_id(id)
            if song:
                return song
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Song with provided id: "
                                                                                f"{id}, does not exist.")
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))

    @staticmethod
    def get_songs_by_characters(characters: str):
        try:
            songs = SongServices.get_songs_by_characters(characters)
            if songs:
                return songs
        except SongNotFoundException as _e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Songs with provided "
                                                                                f"characters: {characters},"
                                                                                f" do not exist.")
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))

    @staticmethod
    def get_all_songs():
        songs = SongServices.get_all_songs()
        return songs

    @staticmethod
    def delete_song_by_id(id: str):
        try:
            SongServices.delete_song_by_id(id)
            return Response(content=f"Song with provided id: {id} is deleted.")
        except SongNotFoundException as _e:
            raise HTTPException(status_code=_e.code, detail=_e.message)
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))

    @staticmethod
    def update_song(id: str, name=None, length=None, items_sold=None, lyrics=None, date_of_release=None,
                    ratings=None, explicit=None, artist_id=None, genre_name=None,
                    award_name=None):
        try:
            song = SongServices.update_song(id, name, length, items_sold, lyrics, date_of_release, ratings,
                                            explicit, artist_id, genre_name, award_name)
            return song
        except SongNotFoundException as _e:
            raise HTTPException(status_code=_e.code, detail=_e.message)
        except Exception as _e:
            raise _e
