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
    def get_song_by_id(id: str):
        try:
            with SessionLocal() as db:
                song_repository = SongRepository(db)
                return song_repository.get_song_by_id(id)
        except Exception as e:
            raise e

    @staticmethod
    def calculate_average_rating_for_song(id: str):
        try:
            with SessionLocal() as db:
                song_repository = SongRepository(db)
                return song_repository.calculate_average_rating_for_song(id)
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
    def get_songs_by_rating():
        try:
            with SessionLocal() as db:
                song_repository = SongRepository(db)
                return song_repository.get_songs_by_rating()
        except Exception as e:
            raise e

    @staticmethod
    def get_best_songs_from_year(year: str):
        try:
            with SessionLocal() as db:
                song_repository = SongRepository(db)
                return song_repository.get_best_songs_from_year(year)
        except Exception as e:
            raise e

    @staticmethod
    def get_song_with_most_awards():
        try:
            with SessionLocal() as db:
                song_repository = SongRepository(db)
                return song_repository.get_song_with_most_awards()
        except Exception as e:
            raise e

    @staticmethod
    def get_songs_by_genre(genre: str):
        try:
            with SessionLocal() as db:
                song_repository = SongRepository(db)
                return song_repository.get_songs_by_genre(genre)
        except Exception as e:
            raise e

    @staticmethod
    def get_all_comments_about_song(id: str):
        try:
            with SessionLocal() as db:
                song_repository = SongRepository(db)
                return song_repository.get_all_comments_about_song(id)
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
                    ratings=None, explicit=None):
        try:
            with SessionLocal() as db:
                song_repository = SongRepository(db)
                return song_repository.update_song(id, name, length, date_of_release, items_sold, lyrics, ratings,
                                                   explicit)
        except Exception as e:
            raise e

    @staticmethod
    def add_artist_to_song(song_id: str, artist_id: str):
        try:
            with SessionLocal() as db:
                song_repository = SongRepository(db)
                return song_repository.add_group_to_song(song_id, artist_id)
        except Exception as e:
            raise e

    @staticmethod
    def add_group_to_song(song_id: str, group_id: str):
        try:
            with SessionLocal() as db:
                song_repository = SongRepository(db)
                return song_repository.add_group_to_song(song_id, group_id)
        except Exception as e:
            raise e

    @staticmethod
    def add_album_to_song(song_id: str, album_id: str):
        try:
            with SessionLocal() as db:
                song_repository = SongRepository(db)
                return song_repository.add_album_to_song(song_id, album_id)
        except Exception as e:
            raise e

    @staticmethod
    def add_award_to_song(song_id: str, award_id: str):
        try:
            with SessionLocal() as db:
                song_repository = SongRepository(db)
                return song_repository.add_award_to_song(song_id, award_id)
        except Exception as e:
            raise e

    @staticmethod
    def add_genre_to_song(song_id: str, genre_name: str):
        try:
            with SessionLocal() as db:
                song_repository = SongRepository(db)
                return song_repository.add_genre_to_song(song_id, genre_name)
        except Exception as e:
            raise e

    @staticmethod
    def add_comment_to_song(song_id: str, comment_id: str):
        try:
            with SessionLocal() as db:
                song_repository = SongRepository(db)
                return song_repository.add_comment_to_song(song_id, comment_id)
        except Exception as e:
            raise e

    @staticmethod
    def remove_artist_from_song(song_id: str, artist_id: str):
        try:
            with SessionLocal() as db:
                song_repository = SongRepository(db)
                return song_repository.remove_group_from_song(song_id, artist_id)
        except Exception as e:
            raise e

    @staticmethod
    def remove_group_from_song(song_id: str, group_id: str):
        try:
            with SessionLocal() as db:
                song_repository = SongRepository(db)
                return song_repository.remove_group_from_song(song_id, group_id)
        except Exception as e:
            raise e

    @staticmethod
    def remove_album_from_song(song_id: str, album_id: str):
        try:
            with SessionLocal() as db:
                song_repository = SongRepository(db)
                return song_repository.remove_album_from_song(song_id, album_id)
        except Exception as e:
            raise e

    @staticmethod
    def remove_award_from_song(song_id: str, award_id: str):
        try:
            with SessionLocal() as db:
                song_repository = SongRepository(db)
                return song_repository.remove_award_from_song(song_id, award_id)
        except Exception as e:
            raise e

    @staticmethod
    def remove_genre_from_song(song_id: str, genre_name: str):
        try:
            with SessionLocal() as db:
                song_repository = SongRepository(db)
                return song_repository.remove_genre_from_song(song_id, genre_name)
        except Exception as e:
            raise e

    @staticmethod
    def remove_comment_from_song(song_id: str, comment_id: str):
        try:
            with SessionLocal() as db:
                song_repository = SongRepository(db)
                return song_repository.remove_comment_from_song(song_id, comment_id)
        except Exception as e:
            raise e
