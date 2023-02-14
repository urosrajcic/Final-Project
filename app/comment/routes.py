from fastapi import APIRouter
from app.comment.controller import CommentController
from app.comment.schemas import *

comment_router = APIRouter(tags=["comments"], prefix="/mdb/comments")


@comment_router.post("/add-new-comment", response_model=CommentSchema)
def create_comment(comment: CommentSchemaIn):
    return CommentController.create_comment(comment.header, comment.text, comment.date_time, comment.user_username)


@comment_router.get("/get-comment-by-id", response_model=CommentSchema)
def get_comment_by_id(id: str):
    return CommentController.get_comment_by_id(id)


@comment_router.get("/get-all-comments", response_model=list[CommentSchema])
def get_all_comments():
    return CommentController.get_all_comment()


@comment_router.get("/get-all-comments-about-an-artist", response_model=list[CommentSchema])
def get_all_about_artist(artist_id: str):
    return CommentController.get_all_comments_about_artist(artist_id)


@comment_router.get("/get-all-comments-about-an-album", response_model=list[CommentSchema])
def get_all_comments_about_album(album_id: str):
    return CommentController.get_all_comments_about_album(album_id)


@comment_router.get("/get-all-comments-a-song", response_model=list[CommentSchema])
def get_all_comments_about_song(song_id: str):
    return CommentController.get_all_comments_about_song(song_id)


@comment_router.get("/get-all-comments-a-record_label", response_model=list[CommentSchema])
def get_all_comments_about_record_label(record_label_id: str):
    return CommentController.get_all_comments_about_record_label(record_label_id)


@comment_router.get("/get-all-comments-from-a-user", response_model=list[CommentSchema])
def get_all_comments_from_user(user_username: str):
    return CommentController.get_all_comments_from_user(user_username)


@comment_router.delete("/delete-comment-by-id")
def delete_comment_by_id(id: str):
    return CommentController.delete_comment_by_id(id)


@comment_router.put("/update-comment-by-id", response_model=CommentSchema)
def update_comment(id: str, header=None, text=None, date_time=None, ratings=None, user_username=None,
                   song_id=None, artist_id=None, album_id=None, record_label_id=None):
    return CommentController.update_comment(id, header, text, date_time, ratings, user_username, song_id,
                                            artist_id, album_id, record_label_id)
