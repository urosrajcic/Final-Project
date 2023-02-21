from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.comment.exceptions import *
from app.comment.model import Comment


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

    def get_all_comments_from_user(self, user_username: str):
        comments = self.db.query(Comment).filter(Comment.user_username.like(user_username)).all()
        if comments is None:
            raise CommentNotFoundException(f"Comments with provided artist id: {user_username} not found.", 500)

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
