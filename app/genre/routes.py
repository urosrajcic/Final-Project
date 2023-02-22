from fastapi import APIRouter, Depends
from app.genre.controller import GenreController
from app.genre.schemas import *
from app.user.controller import JWTBearer

genre_router = APIRouter(tags=["Genres"], prefix="/mdb/genres")


@genre_router.post("/add-new-genre", response_model=GenreSchema, dependencies=[Depends(JWTBearer("super_user"))])
def create_genre(genre: GenreSchema):
    return GenreController.create_genre(name=genre.name)


@genre_router.get("/get-genres-by-characters", response_model=list[GenreSchema])
def get_genres_by_characters(characters: str):
    return GenreController.get_genres_by_characters(characters=characters)


@genre_router.get("/get-all-genres", response_model=list[GenreSchema])
def get_all_genres():
    return GenreController.get_all_genres()


@genre_router.delete("/delete-genre-by-name", dependencies=[Depends(JWTBearer("super_user"))])
def delete_genre_by_name(name: str):
    return GenreController.delete_genre_by_name(name=name)
