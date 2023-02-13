from datetime import date
from app.db.database import SessionLocal
from app.ceo.repository.ceo_repository import CEORepository


class CEOServices:
    @staticmethod
    def create_ceo(name: str, surname: str, date_of_birth: date, from_date: date):
        try:
            with SessionLocal() as db:
                ceo_repository = CEORepository(db)
                return ceo_repository.create_ceo(name, surname, date_of_birth, from_date)
        except Exception as e:
            raise e

    @staticmethod
    def get_ceo_by_id(id: str):
        try:
            with SessionLocal() as db:
                ceo_repository = CEORepository(db)
                return ceo_repository.get_ceo_by_id(id)
        except Exception as e:
            raise e

    @staticmethod
    def get_ceos_by_name(characters_name: str):
        try:
            with SessionLocal() as db:
                ceo_repository = CEORepository(db)
                return ceo_repository.get_ceos_by_name(characters_name)
        except Exception as e:
            raise e

    @staticmethod
    def get_all_ceos():
        try:
            with SessionLocal() as db:
                ceo_repository = CEORepository(db)
                return ceo_repository.get_all_ceos()
        except Exception as e:
            raise e

    @staticmethod
    def delete_ceo_by_id(id: str):
        try:
            with SessionLocal() as db:
                ceo_repository = CEORepository(db)
                return ceo_repository.delete_ceo_by_id(id)
        except Exception as e:
            raise e

    @staticmethod
    def update_ceo(id: str, name=None, surname=None, date_of_birth=None,
                   from_date=None, too_date=None, active=None):
        try:
            with SessionLocal() as db:
                ceo_repository = CEORepository(db)
                return ceo_repository.update_ceo(id, name, surname, date_of_birth,
                                                 from_date, too_date, active)
        except Exception as e:
            raise e
