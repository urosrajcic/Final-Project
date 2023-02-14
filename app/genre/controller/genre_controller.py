from fastapi import HTTPException, Response, status
from app.genre.exceptions import *
from app.genre.services import GenreServices


class GenreController:
    @staticmethod
    def create_genre(name: str):
        try:
            genre = GenreServices.create_genre(name)
            return genre
        except GenreNotFoundException as _e:
            raise HTTPException(status_code=_e.code, detail=_e.message)
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))

    @staticmethod
    def get_genres_by_characters(characters: str):
        try:
            genres = GenreServices.get_genre_by_characters(characters)
            if genres:
                return genres
        except GenreNotFoundException as _e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Genres with provided characters: "
                                                                                f"{characters}, does not exist.")
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))

    @staticmethod
    def get_all_genres():
        genres = GenreServices.get_all_genres()
        return genres

    @staticmethod
    def delete_genre_by_name(name: str):
        try:
            GenreServices.delete_genre_by_name(name)
            return Response(content=f"Genre with provided name: {name} is deleted.")
        except GenreNotFoundException as _e:
            raise HTTPException(status_code=_e.code, detail=_e.message)
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))

    @staticmethod
    def update_genre(name: str, song_id=None, artist_id=None, album_id=None):
        try:
            genre = GenreServices.update_genre(name, song_id, artist_id, album_id)
            return genre
        except GenreNotFoundException as _e:
            raise HTTPException(status_code=_e.code, detail=_e.message)
        except Exception as _e:
            raise _e
