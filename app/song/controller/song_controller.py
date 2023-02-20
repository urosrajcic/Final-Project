from fastapi import HTTPException, Response, status
from app.song.exceptions import *
from app.song.services import SongServices


class SongController:
    @staticmethod
    def create_song(name: str, length: int, date_of_release: str):
        try:
            song = SongServices.create_song(name, length, date_of_release)
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
    def update_song(id: str, name=None, length=None, date_of_release=None, items_sold=None, lyrics=None,
                    ratings=None, explicit=None):
        try:
            song = SongServices.update_song(id, name, length, date_of_release, items_sold, lyrics, ratings,
                                            explicit)
            return song
        except SongNotFoundException as _e:
            raise HTTPException(status_code=_e.code, detail=_e.message)
        except Exception as _e:
            raise _e

    @staticmethod
    def add_artist_to_song(song_id: str, artist_id: str):
        try:
            song = SongServices.add_artist_to_song(song_id, artist_id)
            if song:
                return song
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Song with provided id: "
                                                                                f"{song_id}, does not exist.")
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))

    @staticmethod
    def add_album_to_song(song_id: str, album_id: str):
        try:
            song = SongServices.add_album_to_song(song_id, album_id)
            if song:
                return song
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Song with provided id: "
                                                                                f"{song_id}, does not exist.")
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))

    @staticmethod
    def add_award_to_song(song_id: str, award_id: str):
        try:
            song = SongServices.add_award_to_song(song_id, award_id)
            if song:
                return song
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Song with provided id: "
                                                                                f"{song_id}, does not exist.")
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))

    @staticmethod
    def add_genre_to_song(song_id: str, genre_name: str):
        try:
            song = SongServices.add_genre_to_song(song_id, genre_name)
            if song:
                return song
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Song with provided id: "
                                                                                f"{song_id}, does not exist.")
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))
