from fastapi import APIRouter, Depends
from app.country.controller import CountryController
from app.country.schemas import CountrySchema
from app.user.controller import JWTBearer

country_router = APIRouter(tags=["Countries"], prefix="/mdb/countries")


@country_router.post("/add-new-country", response_model=CountrySchema)
def create_country(country: CountrySchema):
    return CountryController.create_country(name=country.name)


@country_router.get("/get-countries-by-characters", response_model=list[CountrySchema])
def get_countries_by_characters(characters: str):
    return CountryController.get_countries_by_characters(characters=characters)


@country_router.get("/get-all-countries", response_model=list[CountrySchema])
def get_all_countries():
    return CountryController.get_all_countries()


@country_router.delete("/delete-country-by-name", dependencies=[Depends(JWTBearer("super_user"))])
def delete_country_by_name(name: str):
    return CountryController.delete_country_by_name(name=name)
