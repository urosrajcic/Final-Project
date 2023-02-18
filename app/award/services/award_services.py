from datetime import date
from app.db.database import SessionLocal
from app.award.repository.award_repository import AwardRepository


class AwardServices:
    @staticmethod
    def create_award(name: str, award_date: date):
        try:
            with SessionLocal() as db:
                award_repository = AwardRepository(db)
                return award_repository.create_award(name, award_date)
        except Exception as e:
            raise e

    @staticmethod
    def get_award_by_id(id: str):
        try:
            with SessionLocal() as db:
                award_repository = AwardRepository(db)
                return award_repository.get_award_by_id(id)
        except Exception as e:
            raise e

    @staticmethod
    def get_awards_by_name(name: str):
        try:
            with SessionLocal() as db:
                award_repository = AwardRepository(db)
                return award_repository.get_awards_by_name(name)
        except Exception as e:
            raise e

    @staticmethod
    def get_all_awards():
        try:
            with SessionLocal() as db:
                award_repository = AwardRepository(db)
                return award_repository.get_all_awards()
        except Exception as e:
            raise e

    @staticmethod
    def delete_award_by_id(id: str):
        try:
            with SessionLocal() as db:
                award_repository = AwardRepository(db)
                return award_repository.delete_award_by_id(id)
        except Exception as e:
            raise e

    @staticmethod
    def update_award(id: str, name=None, award_date=None):
        try:
            with SessionLocal() as db:
                award_repository = AwardRepository(db)
                return award_repository.update_award(id, name, award_date)
        except Exception as e:
            raise e
