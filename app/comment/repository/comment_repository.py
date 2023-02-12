from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.comment.exceptions import CommentNotFoundException
from app.comment.model import Comment


class CommentRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_comment(self, header, text, datetime, user_username):
        try:
            comment = Comment(header, text, datetime, user_username)
            self.db.add(comment)
            self.db.commit()
            self.db.refresh(comment)
            return comment
        except IntegrityError as e:
            raise e

    def get_comment_by_id(self, id: str):
        comment = self.db.query(Comment).filter(Comment.id == id).first()
        if comment is None:
            raise CommentNotFoundException(f"Comment with provided id: {id} not found.", 400)
        return comment

    def get_all_comments(self):
        comments = self.db.query(Comment).all()
        return comments

    def get_all_comments_about_artist(self, artist_id):
        comments = self.db.query(Comment).filter(Comment.artist_id.like(artist_id)).all()
        if comments is None:
            raise CommentNotFoundException(f"Comments with provided artist id: {artist_id} not found.", 400)

    def get_all_comments_about_album(self, album_id):
        comments = self.db.query(Comment).filter(Comment.album_id.like(album_id)).all()
        if comments is None:
            raise CommentNotFoundException(f"Comments with provided artist id: {album_id} not found.", 400)

    def get_all_comments_about_song(self, song_id):
        comments = self.db.query(Comment).filter(Comment.song_id.like(song_id)).all()
        if comments is None:
            raise CommentNotFoundException(f"Comments with provided song id: {song_id} not found.", 400)

    def get_all_comments_about_user(self, user_username):
        comments = self.db.query(Comment).filter(Comment.user_username.like(user_username)).all()
        if comments is None:
            raise CommentNotFoundException(f"Comments with provided artist id: {user_username} not found.", 400)

    def get_all_comments_about_record_label(self, record_label_id):
        comments = self.db.query(Comment).filter(Comment.record_label_id.like(record_label_id)).all()
        if comments is None:
            raise CommentNotFoundException(f"Comments with provided artist id: {record_label_id} not found.", 400)

    def delete_comment_by_id(self, id: str):
        try:
            comment = self.db.query(Comment).filter(Comment.id == id).first()
            if comment is None:
                raise CommentNotFoundException(f"Comment with provided id: {id} not found.", 400)
            self.db.delete(comment)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def update_comment(self, id: str, header=None, text=None, datetime=None, ratings=None, user_username=None,
                       song_id=None, artist_id=None, album_id=None, record_label_id=None):
        try:
            comment = self.db.query(Comment).filter(Comment.id == id).first()
            if comment is None:
                raise CommentNotFoundException(f"Comment with provided id: {id} not found.", 400)
            if header is not None:
                comment.header = header
            if text is not None:
                comment.text = text
            if datetime is not None:
                comment.datetime = datetime
            if ratings is not None:
                comment.ratings = ratings
            if user_username is not None:
                comment.user_username = user_username
            if song_id is not None:
                comment.song_id = song_id
            if album_id is not None:
                comment.album_id = album_id
            if artist_id is not None:
                comment.artist_id = artist_id
            if record_label_id is not None:
                comment.record_label_id = record_label_id
            self.db.add(comment)
            self.db.commit()
            self.db.refresh(comment)
            return comment
        except Exception as e:
            raise e
