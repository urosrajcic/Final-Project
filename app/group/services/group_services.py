from app.db.database import SessionLocal
from app.group.repository.group_repository import GroupRepository


class GroupServices:
    @staticmethod
    def create_group(name: str, country_name: str, date_of_forming: str):
        try:
            with SessionLocal() as db:
                group_repository = GroupRepository(db)
                return group_repository.create_group(name, country_name, date_of_forming)
        except Exception as e:
            raise e

    @staticmethod
    def calculate_average_rating_for_group(id: str):
        try:
            with SessionLocal() as db:
                group_repository = GroupRepository(db)
                return group_repository.calculate_average_rating_for_group(id)
        except Exception as e:
            raise e

    @staticmethod
    def get_group_by_id(id: str):
        try:
            with SessionLocal() as db:
                group_repository = GroupRepository(db)
                return group_repository.get_group_by_id(id)
        except Exception as e:
            raise e

    @staticmethod
    def get_groups_by_characters(characters: str):
        try:
            with SessionLocal() as db:
                group_repository = GroupRepository(db)
                return group_repository.get_groups_by_characters(characters)
        except Exception as e:
            raise e

    @staticmethod
    def get_all_groups():
        try:
            with SessionLocal() as db:
                group_repository = GroupRepository(db)
                return group_repository.get_all_groups()
        except Exception as e:
            raise e

    @staticmethod
    def get_groups_by_rating():
        try:
            with SessionLocal() as db:
                group_repository = GroupRepository(db)
                return group_repository.get_groups_by_rating()
        except Exception as e:
            raise e

    @staticmethod
    def get_groups_from_country(country: str):
        try:
            with SessionLocal() as db:
                group_repository = GroupRepository(db)
                return group_repository.get_groups_from_country(country)
        except Exception as e:
            raise e

    @staticmethod
    def get_group_with_most_awards():
        try:
            with SessionLocal() as db:
                group_repository = GroupRepository(db)
                return group_repository.get_group_with_most_awards()
        except Exception as e:
            raise e

    @staticmethod
    def get_groups_by_genre(genre: str):
        try:
            with SessionLocal() as db:
                group_repository = GroupRepository(db)
                return group_repository.get_groups_by_genre(genre)
        except Exception as e:
            raise e

    @staticmethod
    def get_all_comments_about_group(id: str):
        try:
            with SessionLocal() as db:
                group_repository = GroupRepository(db)
                return group_repository.get_all_comments_about_group(id)
        except Exception as e:
            raise e

    @staticmethod
    def delete_group_by_id(id: str):
        try:
            with SessionLocal() as db:
                group_repository = GroupRepository(db)
                return group_repository.delete_group_by_id(id)
        except Exception as e:
            raise e

    @staticmethod
    def update_group(id: str, name=None, date_of_forming=None, date_of_disband=None, vocalist=None,
                     musician=None, producer=None, writer=None, engineer=None, biography=None, ratings=None,
                     country_name=None, record_label_id=None):
        try:
            with SessionLocal() as db:
                group_repository = GroupRepository(db)
                return group_repository.update_group(id, name, date_of_forming, date_of_disband, vocalist,
                                                     musician, producer, writer, engineer, biography, ratings,
                                                     country_name, record_label_id)
        except Exception as e:
            raise e

    @staticmethod
    def add_song_to_group(group_id: str, song_id: str):
        try:
            with SessionLocal() as db:
                group_repository = GroupRepository(db)
                return group_repository.add_song_to_group(group_id, song_id)
        except Exception as e:
            raise e

    @staticmethod
    def add_album_to_group(group_id: str, album_id: str):
        try:
            with SessionLocal() as db:
                group_repository = GroupRepository(db)
                return group_repository.add_album_to_group(group_id, album_id)
        except Exception as e:
            raise e

    @staticmethod
    def add_award_to_group(group_id: str, award_id: str):
        try:
            with SessionLocal() as db:
                group_repository = GroupRepository(db)
                return group_repository.add_award_to_group(group_id, award_id)
        except Exception as e:
            raise e

    @staticmethod
    def add_genre_to_group(group_id: str, genre_name: str):
        try:
            with SessionLocal() as db:
                group_repository = GroupRepository(db)
                return group_repository.add_genre_to_group(group_id, genre_name)
        except Exception as e:
            raise e

    @staticmethod
    def add_comment_to_group(group_id: str, comment_id: str):
        try:
            with SessionLocal() as db:
                group_repository = GroupRepository(db)
                return group_repository.add_comment_to_group(group_id, comment_id)
        except Exception as e:
            raise e

    @staticmethod
    def remove_song_from_group(group_id: str, song_id: str):
        try:
            with SessionLocal() as db:
                group_repository = GroupRepository(db)
                return group_repository.remove_song_from_group(group_id, song_id)
        except Exception as e:
            raise e

    @staticmethod
    def remove_album_from_group(group_id: str, album_id: str):
        try:
            with SessionLocal() as db:
                group_repository = GroupRepository(db)
                return group_repository.remove_album_from_group(group_id, album_id)
        except Exception as e:
            raise e

    @staticmethod
    def remove_award_from_group(group_id: str, award_id: str):
        try:
            with SessionLocal() as db:
                group_repository = GroupRepository(db)
                return group_repository.remove_award_from_group(group_id, award_id)
        except Exception as e:
            raise e

    @staticmethod
    def remove_genre_from_group(group_id: str, genre_name: str):
        try:
            with SessionLocal() as db:
                group_repository = GroupRepository(db)
                return group_repository.remove_genre_from_group(group_id, genre_name)
        except Exception as e:
            raise e

    @staticmethod
    def remove_comment_from_group(group_id: str, comment_id: str):
        try:
            with SessionLocal() as db:
                group_repository = GroupRepository(db)
                return group_repository.remove_comment_from_group(group_id, comment_id)
        except Exception as e:
            raise e
