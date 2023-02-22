from app.db.database import SessionLocal
from app.comment.repository.comment_repository import CommentRepository


class CommentServices:

    @staticmethod
    def create_comment(header: str, text: str, user_username: str):
        try:
            with SessionLocal() as db:
                comment_repository = CommentRepository(db)
                return comment_repository.create_comment(header, text, user_username)
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
    def get_news():
        try:
            with SessionLocal() as db:
                comment_repository = CommentRepository(db)
                return comment_repository.get_news()
        except Exception as e:
            raise e

    @staticmethod
    def get_album_reviews(album_id: str):
        try:
            with SessionLocal() as db:
                comment_repository = CommentRepository(db)
                return comment_repository.get_album_reviews(album_id)
        except Exception as e:
            raise e

    @staticmethod
    def get_artist_reviews(artists_id: str):
        try:
            with SessionLocal() as db:
                comment_repository = CommentRepository(db)
                return comment_repository.get_artist_reviews(artists_id)
        except Exception as e:
            raise e

    @staticmethod
    def get_song_reviews(song_id: str):
        try:
            with SessionLocal() as db:
                comment_repository = CommentRepository(db)
                return comment_repository.get_song_reviews(song_id)
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
    def delete_comment_by_id(id: str):
        try:
            with SessionLocal() as db:
                comment_repository = CommentRepository(db)
                return comment_repository.delete_comment_by_id(id)
        except Exception as e:
            raise e

    @staticmethod
    def update_comment(id: str, header=None, text=None):
        try:
            with SessionLocal() as db:
                comment_repository = CommentRepository(db)
                return comment_repository.update_comment(id, header, text)
        except Exception as e:
            raise e
