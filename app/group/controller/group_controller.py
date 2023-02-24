from fastapi import HTTPException, Response, status

from app.artist.exceptions import *
from app.artist.services import ArtistServices


class ArtistController:
    @staticmethod
    def create_artist(name: str, country_name: str, date_of_birth: str):
        try:
            artist = ArtistServices.create_artist(name, country_name, date_of_birth)
            return artist
        except ArtistNotFoundException as _e:
            raise HTTPException(status_code=_e.code, detail=_e.message)
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))

    @staticmethod
    def calculate_average_rating_for_artist(id: str):
        try:
            rating = ArtistServices.calculate_average_rating_for_artist(id)
            return rating
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
    def get_artist_by_characters(characters: str):
        artists = ArtistServices.get_artist_by_characters(characters)
        return artists

    @staticmethod
    def get_all_artists():
        artists = ArtistServices.get_all_artists()
        return artists

    @staticmethod
    def get_artists_by_rating():
        artists = ArtistServices.get_artists_by_rating()
        return artists

    @staticmethod
    def get_artists_from_country(country: str):
        artists = ArtistServices.get_artists_from_country(country)
        return artists

    @staticmethod
    def get_artist_with_most_awards():
        try:
            artist = ArtistServices.get_artist_with_most_awards()
            if artist:
                return artist
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="There is no artist in database.")
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))

    @staticmethod
    def get_artist_by_genre(genre: str):
        artists = ArtistServices.get_artists_by_genre(genre)
        return artists

    @staticmethod
    def get_all_comments_about_artist(id: str):
        try:
            comments = ArtistServices.get_all_comments_about_artist(id)
            if comments:
                return comments
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Artist with provided id: "
                                                                                f"{id}, does not exist.")
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))

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
    def update_artist(id: str, name=None, date_of_birth=None, date_of_death=None, vocalist=None,
                      musician=None, producer=None, writer=None, engineer=None, biography=None, ratings=None,
                      country_name=None, record_label_id=None):
        try:
            artist = ArtistServices.update_artist(id, name, date_of_birth, date_of_death, vocalist,
                                                  musician, producer, writer, engineer, biography, ratings,
                                                  country_name, record_label_id)
            return artist
        except ArtistNotFoundException as _e:
            raise HTTPException(status_code=_e.code, detail=_e.message)
        except Exception as _e:
            raise _e

    @staticmethod
    def add_song_to_artist(artist_id: str, song_id: str):
        try:
            artist = ArtistServices.add_song_to_artist(artist_id, song_id)
            if artist:
                return artist
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Artist with provided id: "
                                                                                f"{artist_id}, does not exist.")
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))

    @staticmethod
    def add_album_to_artist(artist_id: str, album_id: str):
        try:
            artist = ArtistServices.add_album_to_artist(artist_id, album_id)
            if artist:
                return artist
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Artist with provided id: "
                                                                                f"{artist_id}, does not exist.")
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))

    @staticmethod
    def add_award_to_artist(artist_id: str, award_id: str):
        try:
            artist = ArtistServices.add_award_to_artist(artist_id, award_id)
            if artist:
                return artist
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Artist with provided id: "
                                                                                f"{artist_id}, does not exist.")
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))

    @staticmethod
    def add_genre_to_artist(artist_id: str, genre_name: str):
        try:
            artist = ArtistServices.add_genre_to_artist(artist_id, genre_name)
            if artist:
                return artist
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Artist with provided id: "
                                                                                f"{artist_id}, does not exist.")
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))

    @staticmethod
    def add_comment_to_artist(artist_id: str, comment_id: str):
        try:
            artist = ArtistServices.add_comment_to_artist(artist_id, comment_id)
            if artist:
                return artist
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Artist with provided id: "
                                                                                f"{artist_id}, does not exist.")
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))

    @staticmethod
    def remove_song_from_artist(artist_id: str, song_id: str):
        try:
            artist = ArtistServices.remove_song_from_artist(artist_id, song_id)
            if artist:
                return artist
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Artist with provided id: "
                                                                                f"{artist_id}, does not exist.")
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))

    @staticmethod
    def remove_album_from_artist(artist_id: str, album_id: str):
        try:
            artist = ArtistServices.remove_album_from_artist(artist_id, album_id)
            if artist:
                return artist
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Artist with provided id: "
                                                                                f"{artist_id}, does not exist.")
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))

    @staticmethod
    def remove_award_from_artist(artist_id: str, award_id: str):
        try:
            artist = ArtistServices.remove_award_from_artist(artist_id, award_id)
            if artist:
                return artist
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Artist with provided id: "
                                                                                f"{artist_id}, does not exist.")
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))

    @staticmethod
    def remove_genre_from_artist(artist_id: str, genre_name: str):
        try:
            artist = ArtistServices.remove_genre_from_artist(artist_id, genre_name)
            if artist:
                return artist
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Artist with provided id: "
                                                                                f"{artist_id}, does not exist.")
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))

    @staticmethod
    def remove_comment_from_artist(artist_id: str, comment_id: str):
        try:
            artist = ArtistServices.remove_comment_from_artist(artist_id, comment_id)
            if artist:
                return artist
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Artist with provided id: "
                                                                                f"{artist_id}, does not exist.")
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))
