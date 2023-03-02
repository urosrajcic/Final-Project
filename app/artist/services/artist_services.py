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
    def calculate_average_rating_for_artist(id: str):
        try:
            with SessionLocal() as db:
                artist_repository = ArtistRepository(db)
                return artist_repository.calculate_average_rating_for_artist(id)
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
    def get_artist_by_characters(characters: str):
        try:
            with SessionLocal() as db:
                artist_repository = ArtistRepository(db)
                return artist_repository.get_artists_by_characters(characters)
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
    def get_artists_by_rating():
        try:
            with SessionLocal() as db:
                artist_repository = ArtistRepository(db)
                return artist_repository.get_artists_by_rating()
        except Exception as e:
            raise e

    @staticmethod
    def get_artists_from_country(country: str):
        try:
            with SessionLocal() as db:
                artist_repository = ArtistRepository(db)
                return artist_repository.get_artists_from_country(country)
        except Exception as e:
            raise e

    @staticmethod
    def get_artist_with_most_awards():
        try:
            with SessionLocal() as db:
                artist_repository = ArtistRepository(db)
                return artist_repository.get_artist_with_most_awards()
        except Exception as e:
            raise e

    @staticmethod
    def get_artists_by_genre(genre: str):
        try:
            with SessionLocal() as db:
                artist_repository = ArtistRepository(db)
                return artist_repository.get_artists_by_genre(genre)
        except Exception as e:
            raise e

    @staticmethod
    def get_all_comments_about_artist(id: str):
        try:
            with SessionLocal() as db:
                artist_repository = ArtistRepository(db)
                return artist_repository.get_all_comments_about_artist(id)
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
                      musician=None, producer=None, writer=None, engineer=None, biography=None, ratings=None,
                      country_name=None, record_label_id=None):
        try:
            with SessionLocal() as db:
                artist_repository = ArtistRepository(db)
                return artist_repository.update_artist(id, name, date_of_birth, date_of_death, vocalist,
                                                       musician, producer, writer, engineer, biography, ratings,
                                                       country_name, record_label_id)
        except Exception as e:
            raise e

    @staticmethod
    def add_song_to_artist(artist_id: str, song_id: str):
        try:
            with SessionLocal() as db:
                artist_repository = ArtistRepository(db)
                return artist_repository.add_group_to_artist(artist_id, song_id)
        except Exception as e:
            raise e

    @staticmethod
    def add_group_to_artist(artist_id: str, group_id: str):
        try:
            with SessionLocal() as db:
                artist_repository = ArtistRepository(db)
                return artist_repository.add_group_to_artist(artist_id, group_id)
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

    @staticmethod
    def add_award_to_artist(artist_id: str, award_id: str):
        try:
            with SessionLocal() as db:
                artist_repository = ArtistRepository(db)
                return artist_repository.add_award_to_artist(artist_id, award_id)
        except Exception as e:
            raise e

    @staticmethod
    def add_genre_to_artist(artist_id: str, genre_name: str):
        try:
            with SessionLocal() as db:
                artist_repository = ArtistRepository(db)
                return artist_repository.add_genre_to_artist(artist_id, genre_name)
        except Exception as e:
            raise e

    @staticmethod
    def add_comment_to_artist(artist_id: str, comment_id: str):
        try:
            with SessionLocal() as db:
                artist_repository = ArtistRepository(db)
                return artist_repository.add_comment_to_artist(artist_id, comment_id)
        except Exception as e:
            raise e

    @staticmethod
    def remove_song_from_artist(artist_id: str, song_id: str):
        try:
            with SessionLocal() as db:
                artist_repository = ArtistRepository(db)
                return artist_repository.remove_group_from_artist(artist_id, song_id)
        except Exception as e:
            raise e

    @staticmethod
    def remove_group_from_artist(artist_id: str, group_id: str):
        try:
            with SessionLocal() as db:
                artist_repository = ArtistRepository(db)
                return artist_repository.remove_group_from_artist(artist_id, group_id)
        except Exception as e:
            raise e

    @staticmethod
    def remove_album_from_artist(artist_id: str, album_id: str):
        try:
            with SessionLocal() as db:
                artist_repository = ArtistRepository(db)
                return artist_repository.remove_album_from_artist(artist_id, album_id)
        except Exception as e:
            raise e

    @staticmethod
    def remove_award_from_artist(artist_id: str, award_id: str):
        try:
            with SessionLocal() as db:
                artist_repository = ArtistRepository(db)
                return artist_repository.remove_award_from_artist(artist_id, award_id)
        except Exception as e:
            raise e

    @staticmethod
    def remove_genre_from_artist(artist_id: str, genre_name: str):
        try:
            with SessionLocal() as db:
                artist_repository = ArtistRepository(db)
                return artist_repository.remove_genre_from_artist(artist_id, genre_name)
        except Exception as e:
            raise e

    @staticmethod
    def remove_comment_from_artist(artist_id: str, comment_id: str):
        try:
            with SessionLocal() as db:
                artist_repository = ArtistRepository(db)
                return artist_repository.remove_comment_from_artist(artist_id, comment_id)
        except Exception as e:
            raise e
