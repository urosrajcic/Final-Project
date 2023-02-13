from datetime import date
from app.db.database import SessionLocal
from app.user.repository.user_repository import UserRepository


class UserServices:
    @staticmethod
    def create_user(username: str, email: str, password: str, name: str, surname: str,
                    date_of_birth: date, country_name: str):
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                return user_repository.create_user(username, email, password, name, surname, date_of_birth,
                                                   country_name)
        except Exception as e:
            raise e

    @staticmethod
    def create_critic(username: str, email: str, password: str, name: str, surname: str,
                      date_of_birth: date, country_name: str):
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                return user_repository.create_critic(username, email, password, name, surname, date_of_birth,
                                                     country_name)
        except Exception as e:
            raise e

    @staticmethod
    def create_writer(username: str, email: str, password: str, name: str, surname: str,
                      date_of_birth: date, country_name: str):
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                return user_repository.create_writer(username, email, password, name, surname, date_of_birth,
                                                     country_name)
        except Exception as e:
            raise e

    @staticmethod
    def create_writer_and_critic(username: str, email: str, password: str, name: str, surname: str,
                                 date_of_birth: date, country_name: str):
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                return user_repository.create_writer_and_critic(username, email, password, name, surname, date_of_birth,
                                                                country_name)
        except Exception as e:
            raise e

    @staticmethod
    def get_user_by_username(username: str):
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                return user_repository.get_user_by_username(username)
        except Exception as e:
            raise e

    @staticmethod
    def get_user_by_characters(characters: str):
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                return user_repository.get_user_by_characters(characters)
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
                    surname: str = None, country_name: str = None):
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                return user_repository.update_user(username, password, name, surname, country_name)
        except Exception as e:
            raise e
