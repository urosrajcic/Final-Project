from datetime import date
from app.db.database import SessionLocal
from app.album.repository.album_repository import AlbumRepository


class AlbumServices:
    @staticmethod
    def create_album(name: str, date_of_release: date, song_id: str, artist_id: str):
        try:
            with SessionLocal() as db:
                album_repository = AlbumRepository(db)
                return album_repository.create_album(name, date_of_release, song_id, artist_id)
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
    def get_albums_by_artist(artist_id: str):
        try:
            with SessionLocal() as db:
                album_repository = AlbumRepository(db)
                return album_repository.get_albums_by_artist(artist_id)
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
    def delete_album_by_id(id: str):
        try:
            with SessionLocal() as db:
                album_repository = AlbumRepository(db)
                return album_repository.delete_album_by_id(id)
        except Exception as e:
            raise e

    @staticmethod
    def update_album(id: str, name=None, length=None, date_of_release=None, items_sold=None, ratings=None,
                     explicit=None, lp=None, ep=None, single=None, mixtape=None, song_id=None, artis_id=None,
                     genre_name=None, award_id=None):
        try:
            with SessionLocal() as db:
                album_repository = AlbumRepository(db)
                return album_repository.update_album(id, name, length, date_of_release, items_sold, ratings,
                                                     explicit, lp, ep, single, mixtape, song_id, artis_id,
                                                     genre_name, award_id)
        except Exception as e:
            raise e
