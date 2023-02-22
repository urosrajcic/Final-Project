from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.album import Album
from app.artist import Artist
from app.comment.exceptions import *
from app.comment.model import Comment
from app.song import Song
from app.user import User


class CommentRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_comment(self, header: str, text: str, user_username: str):
        try:
            comment = Comment(header, text, user_username)
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

    def get_news(self):
        news = self.db.query(Comment).join(User).filter(User.writer).all()
        return news

    def get_album_reviews(self, album_id: str):
        reviews = self.db.query(Comment).join(User).join(Album, Comment.album).filter(User.critic,
                                                                                      Album.id == album_id).all()
        return reviews

    def get_artist_reviews(self, artist_id: str):
        reviews = self.db.query(Comment).join(User).join(Artist, Comment.artist).filter(User.critic,
                                                                                        Artist.id == artist_id).all()
        return reviews

    def get_song_reviews(self, song_id: str):
        reviews = self.db.query(Comment).join(User).join(Song, Comment.song).filter(User.critic,
                                                                                    Song.id == song_id).all()
        return reviews

    def get_all_comments_from_user(self, user_username: str):
        comments = self.db.query(Comment).filter(Comment.user_username.like(user_username)).all()
        if comments is None:
            raise CommentNotFoundException(f"Comments with provided user username: {user_username} not found.", 500)

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

    def update_comment(self, id: str, header=None, text=None):
        try:
            comment = self.db.query(Comment).filter(Comment.id == id).first()
            if comment is None:
                raise CommentNotFoundException(f"Comment with provided id: {id} not found.", 400)
            if header is not None:
                comment.header = header
            if text is not None:
                comment.text = text
            self.db.add(comment)
            self.db.commit()
            self.db.refresh(comment)
            return comment
        except Exception as e:
            raise e
