from fastapi import APIRouter, Depends
from app.record_label.controller import RecordLabelController
from app.record_label.schemas import *
from app.user.controller import JWTBearer

record_label_router = APIRouter(tags=["Record Labels"], prefix="/mdb/record labels")


@record_label_router.post("/add-new-record-label", response_model=RecordLabelSchema,
                          dependencies=[Depends(JWTBearer("super_user"))])
def create_record_label(record_label: RecordLabelSchemaIn):
    return RecordLabelController.create_record_label(name=record_label.name, address=record_label.address,
                                                     date_founded=record_label.date_founded, ceo=record_label.ceo,
                                                     country_name=record_label.country_name)


@record_label_router.get("/get-record-label-by-id", response_model=RecordLabelSchema)
def get_record_label_by_id(id: str):
    return RecordLabelController.get_record_label_by_id(id=id)


@record_label_router.get("/get-record-labels-by-characters", response_model=list[RecordLabelSchema])
def get_record_labels_by_characters(characters: str):
    return RecordLabelController.get_record_labels_by_characters(characters=characters)


@record_label_router.get("/get-all-record-labels", response_model=list[RecordLabelSchema])
def get_all_record_labels():
    return RecordLabelController.get_all_record_labels()


@record_label_router.delete("/delete-record_label-by-id", dependencies=[Depends(JWTBearer("super_user"))])
def delete_record_label_by_id(id: str):
    return RecordLabelController.delete_record_label_by_id(id=id)


@record_label_router.put("/update-record-label", response_model=RecordLabelSchema,
                         dependencies=[Depends(JWTBearer("super_user"))])
def update_record_label(record_label: RecordLabelSchema):
    return RecordLabelController.update_record_label(id=record_label.id.__str__(), name=record_label.name,
                                                     address=record_label.address,
                                                     date_founded=record_label.date_founded, ceo=record_label.ceo,
                                                     country_name=record_label.country_name,
                                                     ratings=record_label.ratings, biography=record_label.biography)
