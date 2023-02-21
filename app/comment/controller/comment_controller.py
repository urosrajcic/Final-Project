from fastapi import HTTPException, Response, status
from app.comment.exceptions import *
from app.comment.services import CommentServices


class CommentController:
    @staticmethod
    def create_comment(header: str, text: str, user_username: str):
        try:
            comment = CommentServices.create_comment(header, text, user_username)
            return comment
        except CommentNotFoundException as _e:
            raise HTTPException(status_code=_e.code, detail=_e.message)
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))

    @staticmethod
    def get_comment_by_id(id: str):
        try:
            comment = CommentServices.get_comment_by_id(id)
            if comment:
                return comment
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Comment with provided id: "
                                                                                f"{id}, does not exist.")
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))

    @staticmethod
    def get_all_comment():
        comments = CommentServices.get_all_comments()
        return comments

    @staticmethod
    def get_all_comments_from_user(user_username: str):
        try:
            comments = CommentServices.get_all_comments_from_user(user_username)
            if comments:
                return comments
        except CommentNotFoundException as _e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Comments from user - username: "
                                                                                f"{user_username}, does not exist.")
        except Exception as e:
            raise e

    @staticmethod
    def delete_comment_by_id(id: str):
        try:
            CommentServices.delete_comment_by_id(id)
            return Response(content=f"Comment with provided id: {id} is deleted.")
        except CommentNotFoundException as _e:
            raise HTTPException(status_code=_e.code, detail=_e.message)
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))

    @staticmethod
    def update_comment(id: str, header=None, text=None):
        try:
            comment = CommentServices.update_comment(id, header, text)
            return comment
        except CommentNotFoundException as _e:
            raise HTTPException(status_code=_e.code, detail=_e.message)
        except Exception as _e:
            raise _e
