from datetime import date
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.ceo.exceptions import CEONotFoundException
from app.ceo.model import CEO


class CEORepository:
    def __init__(self, db: Session):
        self.db = db

    def create_ceo(self, name: str, surname: str, date_of_birth: date, from_date: date):
        try:
            ceo = CEO(name, surname, date_of_birth, from_date)
            self.db.add(ceo)
            self.db.commit()
            self.db.refresh(ceo)
            return ceo
        except IntegrityError as e:
            raise e

    def get_ceo_by_id(self, id: str):
        ceo = self.db.query(CEO).filter(CEO.id == id).first()
        if ceo is None:
            raise CEONotFoundException(f"Song with provided id: {id} not found.", 400)
        return ceo

    def get_ceos_by_name(self, characters_name: str):
        ceos = self.db.query(CEO).filter(CEO.name.like(characters_name + "%")).all()
        if ceos is None:
            raise CEONotFoundException(f"CEOs with provided name characters: {characters_name} not found.", 400)
        return ceos

    def get_all_ceos(self):
        ceos = self.db.query(CEO).all()
        return ceos

    def delete_ceo_by_id(self, id: str):
        try:
            ceo = self.db.query(CEO).filter(CEO.id == id).first()
            if ceo is None:
                raise CEONotFoundException(f"CEO with provided id: {id} not found.", 400)
            self.db.delete(ceo)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def update_ceo(self, id: str, name=None, surname=None, date_of_birth=None,
                   from_date=None, too_date=None, active=None):
        try:
            ceo = self.db.query(CEO).filter(CEO.id == id).first()
            if ceo is None:
                raise CEONotFoundException(f"CEO with provided id: {id} not found.", 400)
            if name is not None:
                ceo.name = name
            if surname is not None:
                ceo.surname = surname
            if date_of_birth is not None:
                ceo.date_of_birth = date_of_birth
            if from_date is not None:
                ceo.from_date = from_date
            if too_date is not None:
                ceo.too_date = too_date
            if active is not None:
                ceo.active = active
            self.db.add(ceo)
            self.db.commit()
            self.db.refresh(ceo)
            return ceo
        except Exception as e:
            raise e
