from datetime import date
from fastapi import HTTPException, Response, status
from app.record_label.exceptions import *
from app.record_label.services import RecordLabelServices


class RecordLabelController:
    @staticmethod
    def create_record_label(name: str, address: str, date_founded: date, country_name: str, ceo_id: str):
        try:
            record_label = RecordLabelServices.create_record_label(name, address, date_founded, country_name, ceo_id)
            return record_label
        except RecordLabelNotFoundException as _e:
            raise HTTPException(status_code=_e.code, detail=_e.message)
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))

    @staticmethod
    def get_record_label_by_id(id: str):
        try:
            record_label = RecordLabelServices.get_record_label_by_id(id)
            if record_label:
                return record_label
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Record label with provided id: "
                                                                                f"{id}, does not exist.")
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))

    @staticmethod
    def get_record_labels_by_characters(characters: str):
        try:
            record_labels = RecordLabelServices.get_record_labels_by_characters(characters)
            if record_labels:
                return record_labels
        except RecordLabelNotFoundException as _e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Record labels with provided "
                                                                                f"characters: {characters},"
                                                                                f" do not exist.")
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))

    @staticmethod
    def get_all_record_labels():
        record_labels = RecordLabelServices.get_all_record_labels()
        return record_labels

    @staticmethod
    def delete_record_label_by_id(id: str):
        try:
            RecordLabelServices.delete_record_label_by_id(id)
            return Response(content=f"Record label with provided id: {id} is deleted.")
        except RecordLabelNotFoundException as _e:
            raise HTTPException(status_code=_e.code, detail=_e.message)
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))

    @staticmethod
    def update_record_label(id: str, name=None, address=None, date_founded=None, ratings=None, biography=None,
                            country_name=None, ceo_id=None):
        try:
            record_label = RecordLabelServices.update_record_label(id, name, address, date_founded, ratings, biography,
                                                                   country_name, ceo_id)
            return record_label
        except RecordLabelNotFoundException as _e:
            raise HTTPException(status_code=_e.code, detail=_e.message)
        except Exception as _e:
            raise _e
