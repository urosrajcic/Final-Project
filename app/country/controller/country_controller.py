from fastapi import HTTPException, Response, status
from app.country.exceptions import *
from app.country.services import CountryServices


class CountryController:
    @staticmethod
    def create_country(name: str):
        try:
            country = CountryServices.create_country(name)
            return country
        except CountryNotFoundException as _e:
            raise HTTPException(status_code=_e.code, detail=_e.message)
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))

    @staticmethod
    def get_countries_by_characters(characters: str):
        countries = CountryServices.get_countries_by_characters(characters)
        return countries

    @staticmethod
    def get_all_countries():
        countries = CountryServices.get_all_countries()
        return countries

    @staticmethod
    def delete_country_by_name(name: str):
        try:
            CountryServices.delete_country_by_name(name)
            return Response(content=f"Country with provided name: {name} is deleted.")
        except CountryNotFoundException as _e:
            raise HTTPException(status_code=_e.code, detail=_e.message)
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))
