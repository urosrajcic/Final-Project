from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.country.model import Country
from app.country.exceptions import CountryNotFoundException


class CountryRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_country(self, name: str):
        try:
            country = Country(name)
            self.db.add(country)
            self.db.commit()
            self.db.refresh(country)
            return country
        except IntegrityError as e:
            raise e

    def get_countries_by_characters(self, characters: str):
        countries = self.db.query(Country).filter(Country.name.like(characters + "%")).all()
        return countries

    def get_all_countries(self):
        countries = self.db.query(Country).all()
        return countries

    def delete_country_by_name(self, name: str):
        try:
            country = self.db.query(Country).filter(Country.name == name).first()
            if country is None:
                raise CountryNotFoundException(f"Country with provided name: {name} not found.", 400)
            self.db.delete(country)
            self.db.commit()
            return True
        except Exception as e:
            raise e
