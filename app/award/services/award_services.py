from app.db.database import SessionLocal
from app.award.repository.award_repository import AwardRepository


class AwardServices:
    @staticmethod
    def create_award(name: str, category: str, award_date: str):
        try:
            with SessionLocal() as db:
                award_repository = AwardRepository(db)
                return award_repository.create_award(name, category, award_date)
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
    def get_awards_by_characters(characters: str):
        try:
            with SessionLocal() as db:
                award_repository = AwardRepository(db)
                return award_repository.get_awards_by_characters(characters)
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
    def update_award(id: str, name=None, category=None, award_date=None):
        try:
            with SessionLocal() as db:
                award_repository = AwardRepository(db)
                return award_repository.update_award(id, name, category, award_date)
        except Exception as e:
            raise e
