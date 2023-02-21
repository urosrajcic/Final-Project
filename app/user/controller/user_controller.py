from fastapi import HTTPException, Response, status

from app.album.services import AlbumServices
from app.artist.services import ArtistServices
from app.song.services import SongServices
from app.user.exceptions import *
from app.user.services import UserServices


class UserController:
    @staticmethod
    def create_user(username: str, email: str, password: str, name: str, surname: str,
                    date_of_birth: str, country_name: str):
        try:
            user = UserServices.create_user(username, email, password, name, surname, date_of_birth,
                                            country_name)
            return user
        except UserNotFoundException as _e:
            raise HTTPException(status_code=_e.code, detail=_e.message)
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))

    @staticmethod
    def create_critic(username: str, email: str, password: str, name: str, surname: str,
                      date_of_birth: str, country_name: str):
        try:
            critic = UserServices.create_critic(username, email, password, name, surname, date_of_birth,
                                                country_name)
            return critic
        except UserNotFoundException as _e:
            raise HTTPException(status_code=_e.code, detail=_e.message)
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))

    @staticmethod
    def create_writer(username: str, email: str, password: str, name: str, surname: str,
                      date_of_birth: str, country_name: str):
        try:
            writer = UserServices.create_writer(username, email, password, name, surname, date_of_birth,
                                                country_name)
            return writer
        except UserNotFoundException as _e:
            raise HTTPException(status_code=_e.code, detail=_e.message)
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))

    @staticmethod
    def create_writer_and_critic(username: str, email: str, password: str, name: str, surname: str,
                                 date_of_birth: str, country_name: str):
        try:
            user = UserServices.create_writer_and_critic(username, email, password, name, surname, date_of_birth,
                                                         country_name)
            return user
        except UserNotFoundException as _e:
            raise HTTPException(status_code=_e.code, detail=_e.message)
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))

    @staticmethod
    def get_user_by_username(username: str):
        try:
            user = UserServices.get_user_by_username(username)
            if user:
                return user
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"User with provided username: "
                                                                                f"{username}, does not exist.")
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))

    @staticmethod
    def get_user_by_email(email: str):
        try:
            user = UserServices.get_user_by_email(email)
            if user:
                return user
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"User with provided email: "
                                                                                f"{email}, does not exist.")
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))

    @staticmethod
    def get_users_by_characters(characters: str):
        try:
            users = UserServices.get_users_by_characters(characters)
            if users:
                return users
        except UserNotFoundException as _e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Users with provided "
                                                                                f"characters: {characters},"
                                                                                f" do not exist.")
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))

    @staticmethod
    def get_all_users():
        users = UserServices.get_all_users()
        return users

    @staticmethod
    def delete_user_by_username(username: str):
        try:
            UserServices.delete_user_by_username(username)
            return Response(content=f"User with provided username: {username} is deleted.")
        except UserNotFoundException as _e:
            raise HTTPException(status_code=_e.code, detail=_e.message)
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))

    @staticmethod
    def update_user(username: str, password: str = None, name: str = None,
                    surname: str = None, date_of_birth: str = None, country_name: str = None):
        try:
            user = UserServices.update_user(username, password, name, surname, date_of_birth, country_name)
            return user
        except UserNotFoundException as _e:
            raise HTTPException(status_code=_e.code, detail=_e.message)
        except Exception as _e:
            raise _e

    @staticmethod
    def rate_album(username: str, album_id: str, rating: int):
        try:
            user_rating = UserServices.rate_album(username, album_id, rating)
            ratings = AlbumServices.calculate_average_rating_for_album(id=album_id)
            AlbumServices.update_album(id=album_id, ratings=ratings)
            return user_rating
        except UserNotFoundException as _e:
            raise HTTPException(status_code=_e.code, detail=_e.message)
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))

    @staticmethod
    def rate_artist(username: str, artist_id: str, rating: int):
        try:
            user_rating = UserServices.rate_artist(username, artist_id, rating)
            ratings = ArtistServices.calculate_average_rating_for_artist(id=artist_id)
            ArtistServices.update_artist(id=artist_id, ratings=ratings)
            return user_rating
        except UserNotFoundException as _e:
            raise HTTPException(status_code=_e.code, detail=_e.message)
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))

    @staticmethod
    def rate_song(username: str, song_id: str, rating: int):
        try:
            user_rating = UserServices.rate_song(username, song_id, rating)
            ratings = SongServices.calculate_average_rating_for_song(id=song_id)
            SongServices.update_song(id=song_id, ratings=ratings)
            return user_rating
        except UserNotFoundException as _e:
            raise HTTPException(status_code=_e.code, detail=_e.message)
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))
