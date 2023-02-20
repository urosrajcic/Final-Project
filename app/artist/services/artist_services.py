from app.db.database import SessionLocal
from app.artist.repository.artist_repository import ArtistRepository


class ArtistServices:
    @staticmethod
    def create_artist(name: str, country_name: str, date_of_birth: str):
        try:
            with SessionLocal() as db:
                artist_repository = ArtistRepository(db)
                return artist_repository.create_artist(name, country_name, date_of_birth)
        except Exception as e:
            raise e

    @staticmethod
    def get_artist_by_id(id: str):
        try:
            with SessionLocal() as db:
                artist_repository = ArtistRepository(db)
                return artist_repository.get_artist_by_id(id)
        except Exception as e:
            raise e

    @staticmethod
    def get_artist_by_name(name: str):
        try:
            with SessionLocal() as db:
                artist_repository = ArtistRepository(db)
                return artist_repository.get_artists_by_name(name)
        except Exception as e:
            raise e

    @staticmethod
    def get_all_artists():
        try:
            with SessionLocal() as db:
                artist_repository = ArtistRepository(db)
                return artist_repository.get_all_artists()
        except Exception as e:
            raise e

    @staticmethod
    def delete_artist_by_id(id: str):
        try:
            with SessionLocal() as db:
                artist_repository = ArtistRepository(db)
                return artist_repository.delete_artis_by_id(id)
        except Exception as e:
            raise e

    @staticmethod
    def update_artist(id: str, name=None, date_of_birth=None, date_of_death=None, vocalist=None,
                      musician=None, producer=None, writer=None, engineer=None, biography=None,
                      genre_name=None, award_id=None, country_name=None, record_label_id=None):
        try:
            with SessionLocal() as db:
                artist_repository = ArtistRepository(db)
                return artist_repository.update_artist(id, name, date_of_birth, date_of_death,vocalist,
                                                       musician, producer, writer, engineer, biography,
                                                       genre_name, award_id, country_name, record_label_id)
        except Exception as e:
            raise e

    @staticmethod
    def add_song_to_artist(artist_id: str, song_id: str):
        try:
            with SessionLocal() as db:
                artist_repository = ArtistRepository(db)
                return artist_repository.add_song_to_artist(artist_id, song_id)
        except Exception as e:
            raise e

    @staticmethod
    def add_album_to_artist(artist_id: str, album_id: str):
        try:
            with SessionLocal() as db:
                artist_repository = ArtistRepository(db)
                return artist_repository.add_album_to_artist(artist_id, album_id)
        except Exception as e:
            raise e
