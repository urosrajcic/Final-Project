import hashlib

from app.db.database import SessionLocal
from app.user.exceptions import UserInvalidPassword
from app.user.repository.user_repository import UserRepository


class UserServices:
    @staticmethod
    def login_user(email: str, password: str):
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                user = user_repository.get_user_by_email(email)
                if hashlib.sha256(bytes(password, "utf-8")).hexdigest() != user.password:
                    raise UserInvalidPassword(message="Invalid password for user", code=401)
                return user
        except Exception as e:
            raise e

    @staticmethod
    def create_user(username: str, email: str, password: str, name: str, surname: str,
                    date_of_birth: str, country_name: str):
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                hashed_password = hashlib.sha256(bytes(password, "utf-8")).hexdigest()
                return user_repository.create_user(username, email, hashed_password, name, surname, date_of_birth,
                                                   country_name)
        except Exception as e:
            raise e

    @staticmethod
    def create_critic(username: str, email: str, password: str, name: str, surname: str,
                      date_of_birth: str, country_name: str):
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                hashed_password = hashlib.sha256(bytes(password, "utf-8")).hexdigest()
                return user_repository.create_critic(username, email, hashed_password, name, surname, date_of_birth,
                                                     country_name)
        except Exception as e:
            raise e

    @staticmethod
    def create_writer(username: str, email: str, password: str, name: str, surname: str,
                      date_of_birth: str, country_name: str):
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                hashed_password = hashlib.sha256(bytes(password, "utf-8")).hexdigest()
                return user_repository.create_writer(username, email, hashed_password, name, surname, date_of_birth,
                                                     country_name)
        except Exception as e:
            raise e

    @staticmethod
    def create_writer_and_critic(username: str, email: str, password: str, name: str, surname: str,
                                 date_of_birth: str, country_name: str):
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                hashed_password = hashlib.sha256(bytes(password, "utf-8")).hexdigest()
                return user_repository.create_writer_and_critic(username, email, hashed_password, name, surname,
                                                                date_of_birth, country_name)
        except Exception as e:
            raise e

    @staticmethod
    def create_super_user(username: str, email: str, password: str, name: str, surname: str,
                          date_of_birth: str, country_name: str):
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                hashed_password = hashlib.sha256(bytes(password, "utf-8")).hexdigest()
                return user_repository.create_super_user(username, email, hashed_password, name, surname, date_of_birth,
                                                         country_name)
        except Exception as e:
            raise e

    @staticmethod
    def get_users_by_characters(characters: str):
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                return user_repository.get_users_by_characters(characters)
        except Exception as e:
            raise e

    @staticmethod
    def get_user_by_email(email: str):
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                return user_repository.get_user_by_email(email)
        except Exception as e:
            raise e

    @staticmethod
    def get_all_users():
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                return user_repository.get_all_users()
        except Exception as e:
            raise e

    @staticmethod
    def delete_user_by_username(username: str):
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                return user_repository.delete_user_by_username(username)
        except Exception as e:
            raise e

    @staticmethod
    def update_user(username: str, password: str = None, name: str = None,
                    surname: str = None, date_of_birth: str = None, country_name: str = None):
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                return user_repository.update_user(username, password, name, surname, date_of_birth, country_name)
        except Exception as e:
            raise e

    @staticmethod
    def rate_album(username: str, album_id: str, rating: int):
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                return user_repository.rate_album(username, album_id, rating)
        except Exception as e:
            raise e

    @staticmethod
    def rate_artist(username: str, artist_id: str, rating: int):
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                return user_repository.rate_artist(username, artist_id, rating)
        except Exception as e:
            raise e

    @staticmethod
    def rate_song(username: str, song_id: str, rating: int):
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                return user_repository.rate_song(username, song_id, rating)
        except Exception as e:
            raise e
