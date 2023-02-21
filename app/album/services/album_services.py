from app.db.database import SessionLocal
from app.album.repository.album_repository import AlbumRepository


class AlbumServices:
    @staticmethod
    def create_album(name: str, length: int, date_of_release: str):
        try:
            with SessionLocal() as db:
                album_repository = AlbumRepository(db)
                return album_repository.create_album(name, length, date_of_release)
        except Exception as e:
            raise e

    @staticmethod
    def calculate_average_rating_for_album(id: str):
        try:
            with SessionLocal() as db:
                album_repository = AlbumRepository(db)
                return album_repository.calculate_average_rating_for_album(id)
        except Exception as e:
            raise e

    @staticmethod
    def get_album_by_id(id: str):
        try:
            with SessionLocal() as db:
                album_repository = AlbumRepository(db)
                return album_repository.get_album_by_id(id)
        except Exception as e:
            raise e

    @staticmethod
    def get_album_by_name(name: str):
        try:
            with SessionLocal() as db:
                album_repository = AlbumRepository(db)
                return album_repository.get_album_by_name(name)
        except Exception as e:
            raise e

    @staticmethod
    def get_all_albums():
        try:
            with SessionLocal() as db:
                album_repository = AlbumRepository(db)
                return album_repository.get_all_albums()
        except Exception as e:
            raise e

    @staticmethod
    def get_albums_by_rating():
        try:
            with SessionLocal() as db:
                album_repository = AlbumRepository(db)
                return album_repository.get_albums_by_rating()
        except Exception as e:
            raise e

    @staticmethod
    def delete_album_by_id(id: str):
        try:
            with SessionLocal() as db:
                album_repository = AlbumRepository(db)
                return album_repository.delete_album_by_id(id)
        except Exception as e:
            raise e

    @staticmethod
    def update_album(id: str, name=None, length=None, date_of_release=None, items_sold=None, ratings=None,
                     explicit=None, lp=None, ep=None, single=None, mixtape=None):
        try:
            with SessionLocal() as db:
                album_repository = AlbumRepository(db)
                return album_repository.update_album(id, name, length, date_of_release, items_sold, ratings,
                                                     explicit, lp, ep, single, mixtape)
        except Exception as e:
            raise e

    @staticmethod
    def add_artist_to_album(album_id: str, artist_id: str):
        try:
            with SessionLocal() as db:
                album_repository = AlbumRepository(db)
                return album_repository.add_artist_to_album(album_id, artist_id)
        except Exception as e:
            raise e

    @staticmethod
    def add_song_to_album(album_id: str, song_id: str):
        try:
            with SessionLocal() as db:
                album_repository = AlbumRepository(db)
                return album_repository.add_song_to_album(album_id, song_id)
        except Exception as e:
            raise e

    @staticmethod
    def add_award_to_album(album_id: str, award_id: str):
        try:
            with SessionLocal() as db:
                album_repository = AlbumRepository(db)
                return album_repository.add_award_to_album(album_id, award_id)
        except Exception as e:
            raise e

    @staticmethod
    def add_genre_to_album(album_id: str, genre_name: str):
        try:
            with SessionLocal() as db:
                album_repository = AlbumRepository(db)
                return album_repository.add_genre_to_album(album_id, genre_name)
        except Exception as e:
            raise e

    @staticmethod
    def add_comment_to_album(album_id: str, comment_id: str):
        try:
            with SessionLocal() as db:
                album_repository = AlbumRepository(db)
                return album_repository.add_comment_to_album(album_id, comment_id)
        except Exception as e:
            raise e

    @staticmethod
    def remove_artist_from_album(album_id: str, artist_id: str):
        try:
            with SessionLocal() as db:
                album_repository = AlbumRepository(db)
                return album_repository.remove_artist_from_album(album_id, artist_id)
        except Exception as e:
            raise e

    @staticmethod
    def remove_song_from_album(album_id: str, song_id: str):
        try:
            with SessionLocal() as db:
                album_repository = AlbumRepository(db)
                return album_repository.remove_song_from_album(album_id, song_id)
        except Exception as e:
            raise e

    @staticmethod
    def remove_award_from_album(album_id: str, award_id: str):
        try:
            with SessionLocal() as db:
                album_repository = AlbumRepository(db)
                return album_repository.remove_award_from_album(album_id, award_id)
        except Exception as e:
            raise e

    @staticmethod
    def remove_genre_from_album(album_id: str, genre_name: str):
        try:
            with SessionLocal() as db:
                album_repository = AlbumRepository(db)
                return album_repository.remove_genre_from_album(album_id, genre_name)
        except Exception as e:
            raise e

    @staticmethod
    def remove_comment_from_album(album_id: str, comment_id: str):
        try:
            with SessionLocal() as db:
                album_repository = AlbumRepository(db)
                return album_repository.remove_comment_from_album(album_id, comment_id)
        except Exception as e:
            raise e
