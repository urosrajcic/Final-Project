from datetime import date
from fastapi import HTTPException, Response, status
from app.user.exceptions import *
from app.user.services import UserServices


class UserController:
    @staticmethod
    def create_user(username: str, email: str, password: str, name: str, surname: str,
                    date_of_birth: date, country_name: str):
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
                      date_of_birth: date, country_name: str):
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
                      date_of_birth: date, country_name: str):
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
                                 date_of_birth: date, country_name: str):
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
                    surname: str = None, country_name: str = None):
        try:
            user = UserServices.update_user(username, password, name, surname, country_name)
            return user
        except UserNotFoundException as _e:
            raise HTTPException(status_code=_e.code, detail=_e.message)
        except Exception as _e:
            raise _e
