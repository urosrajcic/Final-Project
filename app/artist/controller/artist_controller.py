from fastapi import HTTPException, Response, status
from app.artist.exceptions import *
from app.artist.services import ArtistServices


class ArtistController:
    @staticmethod
    def create_artist(name: str):
        try:
            artist = ArtistServices.create_artist(name)
            return artist
        except ArtistNotFoundException as _e:
            raise HTTPException(status_code=_e.code, detail=_e.message)
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))

    @staticmethod
    def get_artist_by_id(id: str):
        try:
            artist = ArtistServices.get_artist_by_id(id)
            if artist:
                return artist
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Artist with provided id: "
                                                                                f"{id}, does not exist.")
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))

    @staticmethod
    def get_artist_by_name(name: str):
        try:
            artists = ArtistServices.get_artist_by_name(name)
            if artists:
                return artists
        except ArtistNotFoundException as _e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Artists with provided name: "
                                                                                f"{name}, does not exist.")
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))

    @staticmethod
    def get_all_artists():
        artists = ArtistServices.get_all_artists()
        return artists

    @staticmethod
    def delete_artist_by_id(id: str):
        try:
            ArtistServices.delete_artist_by_id(id)
            return Response(content=f"Artist with provided id: {id} is deleted.")
        except ArtistNotFoundException as _e:
            raise HTTPException(status_code=_e.code, detail=_e.message)
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))

    @staticmethod
    def update_artist(id: str, name=None, date_of_birth=None, date_of_death=None, ratings=None, vocalist=None,
                      musician=None, producer=None, writer=None, engineer=None, biography=None, album_id=None,
                      song_id=None, genre_name=None, award_id=None, country_name=None, user_username=None,
                      record_label_id=None):
        try:
            artist = ArtistServices.update_artist(id, name, date_of_birth, date_of_death, ratings, vocalist,
                                                  musician, producer, writer, engineer, biography, album_id,
                                                  song_id, genre_name, award_id, country_name, user_username,
                                                  record_label_id)
            return artist
        except ArtistNotFoundException as _e:
            raise HTTPException(status_code=_e.code, detail=_e.message)
        except Exception as _e:
            raise _e
