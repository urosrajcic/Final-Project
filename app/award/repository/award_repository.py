from datetime import date
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.award.model import Award
from app.award.exceptions import AwardNotFoundException


class AwardRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_award(self, name: str, award_date: date):
        try:
            award = Award(name, award_date)
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

    def get_awards_by_name(self, name: str):
        awards = self.db.query(Award).filter(Award.name.like(name + "%")).all()
        if awards is None:
            raise AwardNotFoundException(f"Awards with provided name: {name} not found.", 400)
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

    def update_award(self, id: str, name=None,  award_date=None, song_id=None, artist_id=None, album_id=None):
        try:
            award = self.db.query(Award).filter(Award.id == id).first()
            if award is None:
                raise AwardNotFoundException(f"Genre with provided id: {id} not found.", 400)
            if name is not None:
                award.name = name
            if award_date is not None:
                award.award_date = award_date
            if song_id is not None:
                award.song_id = song_id
            if artist_id is not None:
                award.artist_id = artist_id
            if album_id is False:
                award.album_id = album_id
            self.db.add(award)
            self.db.commit()
            self.db.refresh(award)
            return award
        except Exception as e:
            raise e