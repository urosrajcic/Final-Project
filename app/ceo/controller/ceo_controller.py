from datetime import date
from fastapi import HTTPException, Response, status
from app.ceo.exceptions import *
from app.ceo.services import CEOServices


class CEOController:
    @staticmethod
    def create_ceo(name: str, surname: str, date_of_birth: date, from_date: date):
        try:
            ceo = CEOServices.create_ceo(name, surname, date_of_birth, from_date)
            return ceo
        except CEONotFoundException as _e:
            raise HTTPException(status_code=_e.code, detail=_e.message)
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))

    @staticmethod
    def get_ceo_by_id(id: str):
        try:
            ceo = CEOServices.get_ceo_by_id(id)
            if ceo:
                return ceo
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"CEO with provided id: "
                                                                                f"{id}, does not exist.")
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))

    @staticmethod
    def get_ceos_by_name(characters_name: str):
        try:
            ceos = CEOServices.get_ceos_by_name(characters_name)
            if ceos:
                return ceos
        except CEONotFoundException as _e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"CEO with provided name: "
                                                                                f"{characters_name}, does not exist.")
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))

    @staticmethod
    def get_all_ceos():
        ceos = CEOServices.get_all_ceos()
        return ceos

    @staticmethod
    def delete_ceo_by_id(id: str):
        try:
            CEOServices.delete_ceo_by_id(id)
            return Response(content=f"CEO with provided id: {id} is deleted.")
        except CEONotFoundException as _e:
            raise HTTPException(status_code=_e.code, detail=_e.message)
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))

    @staticmethod
    def update_ceo(id: str, name=None, surname=None, date_of_birth=None,
                   from_date=None, too_date=None, active=None):
        try:
            ceo = CEOServices.update_ceo(id, name, surname, date_of_birth,
                                         from_date, too_date, active)
            return ceo
        except CEONotFoundException as _e:
            raise HTTPException(status_code=_e.code, detail=_e.message)
        except Exception as _e:
            raise _e
