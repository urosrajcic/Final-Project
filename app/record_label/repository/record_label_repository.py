from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.record_label.model import RecordLabel
from app.record_label.exceptions import RecordLabelNotFoundException


class RecordLabelRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_record_label(self, name: str, address: str, date_founded: str, ceo: str, country_name: str):
        try:
            record_label = RecordLabel(name, address, date_founded, ceo, country_name)
            self.db.add(record_label)
            self.db.commit()
            self.db.refresh(record_label)
            return record_label
        except IntegrityError as e:
            raise e

    def get_record_label_by_id(self, id: str):
        record_label = self.db.query(RecordLabel).filter(RecordLabel.id == id).first()
        if record_label is None:
            raise RecordLabelNotFoundException(f"Record label with provided id: {id} not found.", 400)
        return record_label

    def get_record_labels_by_characters(self, characters: str):
        record_labels = self.db.query(RecordLabel).filter(RecordLabel.name.like(characters + "%")).all()
        if record_labels is None:
            raise RecordLabelNotFoundException(f"Record label with provided id: {id} not found.", 400)
        return record_labels

    def get_all_record_labels(self):
        record_labels = self.db.query(RecordLabel).all()
        return record_labels

    def delete_record_label_by_id(self, id: str):
        try:
            record_label = self.db.query(RecordLabel).filter(RecordLabel.id == id).first()
            if record_label is None:
                raise RecordLabelNotFoundException(f"Record label with provided id: {id} not found.", 400)
            self.db.delete(record_label)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def update_record_label(self, id: str, name=None, address=None, date_founded=None,
                            ceo=None, country_name=None, ratings=None, biography=None):
        try:
            record_label = self.db.query(RecordLabel).filter(RecordLabel.id == id).first()
            if record_label is None:
                raise RecordLabelNotFoundException(f"Record label with provided id: {id} not found.", 400)
            if name is not None:
                record_label.name = name
            if address is not None:
                record_label.address = address
            if date_founded is not None:
                record_label.date_founded = date_founded
            if ceo is not None:
                record_label.ceo = ceo
            if country_name is not None:
                record_label.country_name = country_name
            if ratings is not None:
                record_label.ratings = ratings
            if biography is not None:
                record_label.biography = biography
            self.db.add(record_label)
            self.db.commit()
            self.db.refresh(record_label)
            return record_label
        except Exception as e:
            raise e
