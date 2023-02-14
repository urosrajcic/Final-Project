from fastapi import APIRouter
from app.award.controller import AwardController
from app.award.schemas import *

award_router = APIRouter(tags=["awards"], prefix="/mdb/awards")


@award_router.post("/add-new-award", response_model=AwardSchema)
def create_award(award: AwardSchemaIn):
    return AwardController.create_award(award.name, award.award_date)


@award_router.get("/get-award-by-id", response_model=AwardSchema)
def get_award_by_id(id: str):
    return AwardController.get_award_by_id(id)


@award_router.get("/get-awards-by-name", response_model=list[AwardSchema])
def get_awards_by_name(name: str):
    return AwardController.get_award_by_name(name)


@award_router.get("/get-all-awards", response_model=list[AwardSchema])
def get_all_awards():
    return AwardController.get_all_awards()


@award_router.delete("/delete-award-by-id")
def delete_award_by_id(id: str):
    return AwardController.delete_award_by_id(id)


@award_router.put("/update-award-by-id", response_model=AwardSchema)
def update_award(iid: str, name=None, award_date=None, song_id=None, artist_id=None, album_id=None):
    return AwardController.update_award(id, name, award_date, song_id, artist_id, album_id)
