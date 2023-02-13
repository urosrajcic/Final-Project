from app.db.database import SessionLocal
from app.genre.repository.genre_repository import GenreRepository


class GenreServices:
    @staticmethod
    def create_genre(name: str):
        try:
            with SessionLocal() as db:
                genre_repository = GenreRepository(db)
                return genre_repository.create_genre(name)
        except Exception as e:
            raise e

    @staticmethod
    def get_genre_by_characters(characters: str):
        try:
            with SessionLocal() as db:
                genre_repository = GenreRepository(db)
                return genre_repository.get_genre_by_characters(characters)
        except Exception as e:
            raise e

    @staticmethod
    def get_all_genres():
        try:
            with SessionLocal() as db:
                genre_repository = GenreRepository(db)
                return genre_repository.get_all_genres()
        except Exception as e:
            raise e

    @staticmethod
    def delete_genre_by_name(name: str):
        try:
            with SessionLocal() as db:
                genre_repository = GenreRepository(db)
                return genre_repository.delete_genre_by_name(name)
        except Exception as e:
            raise e

    @staticmethod
    def update_genre(name: str, song_id=None, artist_id=None, album_id=None):
        try:
            with SessionLocal() as db:
                genre_repository = GenreRepository(db)
                return genre_repository.update_genre(name, song_id, artist_id, album_id)
        except Exception as e:
            raise e
