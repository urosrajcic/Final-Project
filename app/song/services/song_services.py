from app.db.database import SessionLocal
from app.song.repository.song_repository import SongRepository


class SongServices:
    @staticmethod
    def create_song(name: str, length: int, date_of_release: str):
        try:
            with SessionLocal() as db:
                song_repository = SongRepository(db)
                return song_repository.create_song(name, length, date_of_release)
        except Exception as e:
            raise e

    @staticmethod
    def create_explicit_song(name: str, length: int, date_of_release: str):
        try:
            with SessionLocal() as db:
                song_repository = SongRepository(db)
                return song_repository.create_song(name, length, date_of_release)
        except Exception as e:
            raise e

    @staticmethod
    def get_song_by_id(id: str):
        try:
            with SessionLocal() as db:
                song_repository = SongRepository(db)
                return song_repository.get_song_by_id(id)
        except Exception as e:
            raise e

    @staticmethod
    def get_songs_by_characters(characters: str):
        try:
            with SessionLocal() as db:
                song_repository = SongRepository(db)
                return song_repository.get_songs_by_characters(characters)
        except Exception as e:
            raise e

    @staticmethod
    def get_all_songs():
        try:
            with SessionLocal() as db:
                song_repository = SongRepository(db)
                return song_repository.get_all_songs()
        except Exception as e:
            raise e

    @staticmethod
    def delete_song_by_id(id: str):
        try:
            with SessionLocal() as db:
                song_repository = SongRepository(db)
                return song_repository.delete_song_by_id(id)
        except Exception as e:
            raise e

    @staticmethod
    def update_song(id: str, name=None, length=None, date_of_release=None, items_sold=None, lyrics=None,
                    ratings=None, explicit=None, genre_name=None, award_name=None):
        try:
            with SessionLocal() as db:
                song_repository = SongRepository(db)
                return song_repository.update_song(id, name, length, date_of_release, items_sold, lyrics, ratings,
                                                   explicit, genre_name, award_name)
        except Exception as e:
            raise e

    @staticmethod
    def add_artist_to_song(song_id: str, artist_id: str):
        try:
            with SessionLocal() as db:
                song_repository = SongRepository(db)
                return song_repository.add_artist_to_song(song_id, artist_id)
        except Exception as e:
            raise e
