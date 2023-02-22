from fastapi import HTTPException, Response, status
from app.award.exceptions import *
from app.award.services import AwardServices


class AwardController:
    @staticmethod
    def create_award(name: str, category: str, award_date: str):
        try:
            award = AwardServices.create_award(name, category, award_date)
            return award
        except AwardNotFoundException as _e:
            raise HTTPException(status_code=_e.code, detail=_e.message)
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))

    @staticmethod
    def get_award_by_id(id: str):
        try:
            award = AwardServices.get_award_by_id(id)
            if award:
                return award
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Award with provided id: "
                                                                                f"{id}, does not exist.")
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))

    @staticmethod
    def get_award_by_characters(characters: str):
        award = AwardServices.get_awards_by_characters(characters)
        return award

    @staticmethod
    def get_all_awards():
        awards = AwardServices.get_all_awards()
        return awards

    @staticmethod
    def delete_award_by_id(id: str):
        try:
            AwardServices.delete_award_by_id(id)
            return Response(content=f"Award with provided id: {id} is deleted.")
        except AwardNotFoundException as _e:
            raise HTTPException(status_code=_e.code, detail=_e.message)
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))

    @staticmethod
    def update_award(id: str, name=None, category=None, award_date=None):
        try:
            award = AwardServices.update_award(id, name, category, award_date)
            return award
        except AwardNotFoundException as _e:
            raise HTTPException(status_code=_e.code, detail=_e.message)
        except Exception as _e:
            raise _e
