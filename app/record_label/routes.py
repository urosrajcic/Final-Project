from fastapi import APIRouter
from app.record_label.controller import RecordLabelController
from app.record_label.schemas import *

record_label_router = APIRouter(tags=["record labels"], prefix="/mdb/record labels")


@record_label_router.post("/add-new-record-label", response_model=RecordLabelSchema)
def create_record_label(record_label: RecordLabelSchemaIn):
    return RecordLabelController.create_record_label(record_label.name, record_label.address, record_label.date_founded,
                                                     record_label.ratings, record_label.biography,
                                                     record_label.ceo, record_label.country_name)


@record_label_router.get("/get-record-label-by-id", response_model=RecordLabelSchema)
def get_record_label_by_id(id: str):
    return RecordLabelController.get_record_label_by_id(id)


@record_label_router.get("/get-record-labels-by-characters", response_model=list[RecordLabelSchema])
def get_record_labels_by_characters(characters: str):
    return RecordLabelController.get_record_labels_by_characters(characters)


@record_label_router.get("/get-all-record-labels", response_model=list[RecordLabelSchema])
def get_all_record_labels():
    return RecordLabelController.get_all_record_labels()


@record_label_router.delete("/delete-record_label-by-id")
def delete_record_label_by_id(id: str):
    return RecordLabelController.delete_record_label_by_id(id)


@record_label_router.put("/update-record-label-by-id", response_model=RecordLabelSchema)
def update_record_label(id: str, name=None, address=None, date_founded=None, ratings=None, biography=None, ceo=None,
                        country_name=None):
    return RecordLabelController.update_record_label(id, name, address, date_founded, ratings, biography, ceo,
                                                     country_name)
