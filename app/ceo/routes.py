from fastapi import APIRouter
from app.ceo.controller import CEOController
from app.ceo.schemas import *

ceo_router = APIRouter(tags=["CEOs"], prefix="/mdb/CEOs")


@ceo_router.post("/add-new-CEO", response_model=CEOSchema)
def create_ceo(ceo: CEOSchemaIn):
    return CEOController.create_ceo(ceo.name, ceo.name, ceo.date_of_birth, ceo.from_date)


@ceo_router.get("/get-CEO-by-id", response_model=CEOSchema)
def get_ceo_by_id(id: str):
    return CEOController.get_ceo_by_id(id)


@ceo_router.get("/get-CEOs-by-name", response_model=list[CEOSchema])
def get_ceos_by_name(characters_name: str):
    return CEOController.get_ceos_by_name(characters_name)


@ceo_router.get("/get-all-CEOs", response_model=list[CEOSchema])
def get_all_ceos():
    return CEOController.get_all_ceos()


@ceo_router.delete("/delete-CEO-by-id")
def delete_ceo_by_id(id: str):
    return CEOController.delete_ceo_by_id(id)


@ceo_router.put("/update-CEO-by-id", response_model=CEOSchema)
def update_ceo(id: str, name=None, surname=None, date_of_birth=None,
               from_date=None, too_date=None, active=None):
    return CEOController.update_ceo(id, name, surname, date_of_birth,
                                    from_date, too_date, active)
