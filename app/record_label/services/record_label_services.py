from app.db.database import SessionLocal
from app.record_label.repository.record_label_repository import RecordLabelRepository


class RecordLabelServices:
    @staticmethod
    def create_record_label(name: str, address: str, date_founded: str, ratings: float, biography: str,
                            ceo: str, country_name: str):
        try:
            with SessionLocal() as db:
                record_label_repository = RecordLabelRepository(db)
                return record_label_repository.create_record_label(name, address, date_founded, ratings, biography,
                                                                   ceo, country_name)
        except Exception as e:
            raise e

    @staticmethod
    def get_record_label_by_id(id: str):
        try:
            with SessionLocal() as db:
                record_label_repository = RecordLabelRepository(db)
                return record_label_repository.get_record_label_by_id(id)
        except Exception as e:
            raise e

    @staticmethod
    def get_record_labels_by_characters(characters: str):
        try:
            with SessionLocal() as db:
                record_label_repository = RecordLabelRepository(db)
                return record_label_repository.get_record_labels_by_characters(characters)
        except Exception as e:
            raise e

    @staticmethod
    def get_all_record_labels():
        try:
            with SessionLocal() as db:
                record_label_repository = RecordLabelRepository(db)
                return record_label_repository.get_all_record_labels()
        except Exception as e:
            raise e

    @staticmethod
    def delete_record_label_by_id(id: str):
        try:
            with SessionLocal() as db:
                record_label_repository = RecordLabelRepository(db)
                return record_label_repository.delete_record_label_by_id(id)
        except Exception as e:
            raise e

    @staticmethod
    def update_record_label(id: str, name=None, address=None, date_founded=None, ratings=None, biography=None, ceo=None,
                            country_name=None):
        try:
            with SessionLocal() as db:
                record_label_repository = RecordLabelRepository(db)
                return record_label_repository.update_record_label(id, name, address, date_founded, ratings, biography,
                                                                   ceo, country_name)
        except Exception as e:
            raise e
        