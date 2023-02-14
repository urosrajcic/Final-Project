from fastapi import APIRouter
from app.genre.controller import GenreController
from app.genre.schemas import *

genre_router = APIRouter(tags=["genres"], prefix="/mdb/genres")


@genre_router.post("/add-new-genre", response_model=GenreSchema)
def create_genre(genre: GenreSchemaIn):
    return GenreController.create_genre(genre.name)


@genre_router.get("/get-genres-by-characters", response_model=list[GenreSchema])
def get_genres_by_characters(characters: str):
    return GenreController.get_genres_by_characters(characters)


@genre_router.get("/get-all-genres", response_model=list[GenreSchema])
def get_all_genres():
    return GenreController.get_all_genres()


@genre_router.delete("/delete-genre-by-name")
def delete_genre_by_name(name: str):
    return GenreController.delete_genre_by_name(name)


@genre_router.put("/update-genre-by-name", response_model=GenreSchema)
def update_genre(name: str, song_id=None, artist_id=None, album_id=None):
    return GenreController.update_genre(name, song_id, artist_id, album_id)
