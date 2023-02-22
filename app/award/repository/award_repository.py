from datetime import date
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.award.model import Award
from app.award.exceptions import AwardNotFoundException


class AwardRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_award(self, name: str, category: str, award_date: str):
        try:
            award = Award(name, category, award_date)
            self.db.add(award)
            self.db.commit()
            self.db.refresh(award)
            return award
        except IntegrityError as e:
            raise e

    def get_award_by_id(self, id: str):
        award = self.db.query(Award).filter(Award.id == id).first()
        if award is None:
            raise AwardNotFoundException(f"Award with provided id: {id} not found.", 400)
        return award

    def get_awards_by_characters(self, characters: str):
        awards = self.db.query(Award).filter(Award.name.like(characters + "%")).all()
        return awards

    def get_all_awards(self):
        awards = self.db.query(Award).all()
        return awards

    def delete_award_by_id(self, id: str):
        try:
            award = self.db.query(Award).filter(Award.id == id).first()
            if award is None:
                raise AwardNotFoundException(f"Award with provided name: {id} not found.", 400)
            self.db.delete(award)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def update_award(self, id: str, name=None, category=None,  award_date=None):
        try:
            award = self.db.query(Award).filter(Award.id == id).first()
            if award is None:
                raise AwardNotFoundException(f"Award with provided id: {id} not found.", 400)
            if name is not None:
                award.name = name
            if category is not None:
                award.category = category
            if award_date is not None:
                award.award_date = award_date
            self.db.add(award)
            self.db.commit()
            self.db.refresh(award)
            return award
        except Exception as e:
            raise e
