from app.db.database import SessionLocal
from app.country.repository.country_repository import CountryRepository


class CountryServices:
    @staticmethod
    def create_country(name: str):
        try:
            with SessionLocal() as db:
                country_repository = CountryRepository(db)
                return country_repository.create_country(name)
        except Exception as e:
            raise e

    @staticmethod
    def get_countries_by_characters(characters: str):
        try:
            with SessionLocal() as db:
                country_repository = CountryRepository(db)
                return country_repository.get_countries_by_characters(characters)
        except Exception as e:
            raise e

    @staticmethod
    def get_all_countries():
        try:
            with SessionLocal() as db:
                country_repository = CountryRepository(db)
                return country_repository.get_all_countries()
        except Exception as e:
            raise e

    @staticmethod
    def delete_country_by_name(name: str):
        try:
            with SessionLocal() as db:
                country_repository = CountryRepository(db)
                return country_repository.delete_country_by_name(name)
        except Exception as e:
            raise e
