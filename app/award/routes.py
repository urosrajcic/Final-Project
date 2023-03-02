from fastapi import APIRouter, Depends

from app.award.controller import AwardController
from app.award.schemas import *
from app.user.controller import JWTBearer

award_router = APIRouter(tags=["Awards"], prefix="/api/awards")


@award_router.post("/add-new-award", response_model=AwardSchema, dependencies=[Depends(JWTBearer("super_user"))])
def create_award(award: AwardSchemaIn):
    return AwardController.create_award(name=award.name, category=award.category, award_date=award.award_date)


@award_router.get("/get-award-by-id", response_model=AwardSchema)
def get_award_by_id(id: str):
    return AwardController.get_award_by_id(id=id)


@award_router.get("/get-awards-by-characters", response_model=list[AwardSchema])
def get_awards_by_characters(characters: str):
    return AwardController.get_award_by_characters(characters=characters)


@award_router.get("/get-all-awards", response_model=list[AwardSchema])
def get_all_awards():
    return AwardController.get_all_awards()


@award_router.delete("/delete-award-by-id", dependencies=[Depends(JWTBearer("super_user"))])
def delete_award_by_id(id: str):
    return AwardController.delete_award_by_id(id=id)


@award_router.put("/update-award", response_model=AwardSchema, dependencies=[Depends(JWTBearer("super_user"))])
def update_award(award: AwardSchema):
    return AwardController.update_award(id=award.id.__str__(), name=award.name, category=award.category,
                                        award_date=award.award_date)
