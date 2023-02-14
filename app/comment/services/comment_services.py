from datetime import datetime
from app.db.database import SessionLocal
from app.comment.repository.comment_repository import CommentRepository


class CommentServices:
    @staticmethod
    def create_comment(header: str, text: str, date_time: datetime, user_username: str):
        try:
            with SessionLocal() as db:
                comment_repository = CommentRepository(db)
                return comment_repository.create_comment(header, text, date_time, user_username)
        except Exception as e:
            raise e

    @staticmethod
    def get_comment_by_id(id: str):
        try:
            with SessionLocal() as db:
                comment_repository = CommentRepository(db)
                return comment_repository.get_comment_by_id(id)
        except Exception as e:
            raise e

    @staticmethod
    def get_all_comments():
        try:
            with SessionLocal() as db:
                comment_repository = CommentRepository(db)
                return comment_repository.get_all_comments()
        except Exception as e:
            raise e

    @staticmethod
    def get_all_comments_about_artist(artist_id: str):
        try:
            with SessionLocal() as db:
                comment_repository = CommentRepository(db)
                return comment_repository.get_all_comments_about_artist(artist_id)
        except Exception as e:
            raise e

    @staticmethod
    def get_all_comments_about_album(album_id: str):
        try:
            with SessionLocal() as db:
                comment_repository = CommentRepository(db)
                return comment_repository.get_all_comments_about_album(album_id)
        except Exception as e:
            raise e

    @staticmethod
    def get_all_comments_about_song(song_id: str):
        try:
            with SessionLocal() as db:
                comment_repository = CommentRepository(db)
                return comment_repository.get_all_comments_about_song(song_id)
        except Exception as e:
            raise e

    @staticmethod
    def get_all_comments_from_user(user_username: str):
        try:
            with SessionLocal() as db:
                comment_repository = CommentRepository(db)
                return comment_repository.get_all_comments_from_user(user_username)
        except Exception as e:
            raise e

    @staticmethod
    def get_all_comments_about_record_label(record_label_id: str):
        try:
            with SessionLocal() as db:
                comment_repository = CommentRepository(db)
                return comment_repository.get_all_comments_about_record_label(record_label_id)
        except Exception as e:
            raise e

    @staticmethod
    def delete_comment_by_id(id: str):
        try:
            with SessionLocal() as db:
                comment_repository = CommentRepository(db)
                return comment_repository.delete_comment_by_id(id)
        except Exception as e:
            raise e

    @staticmethod
    def update_comment(id: str, header=None, text=None, date_time=None, ratings=None, user_username=None,
                       song_id=None, artist_id=None, album_id=None, record_label_id=None):
        try:
            with SessionLocal() as db:
                comment_repository = CommentRepository(db)
                return comment_repository.update_comment(id, header, text, date_time, ratings, user_username, song_id,
                                                         artist_id, album_id, record_label_id)
        except Exception as e:
            raise e
