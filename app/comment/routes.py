from fastapi import APIRouter

from app.album.schemas import AlbumSchema
from app.artist.schemas import ArtistSchema
from app.comment.controller import CommentController
from app.comment.schemas import *
from app.song.schemas import SongSchema

comment_router = APIRouter(tags=["comments"], prefix="/mdb/comments")


@comment_router.post("/add-new-comment_to_artist", response_model=CommentSchema)
def create_comment_about_artist(comment: CommentSchemaIn, artist: ArtistSchema):
    return CommentController.create_comment_about_artist(header=comment.header, text=comment.text,
                                                         user_username=comment.user_username,
                                                         artist_id=artist.id)


@comment_router.post("/add-new-comment_to_album", response_model=CommentSchema)
def create_comment_about_album(comment: CommentSchemaIn, album: AlbumSchema):
    return CommentController.create_comment_about_album(header=comment.header, text=comment.text,
                                                        user_username=comment.user_username,
                                                        album_id=album.id)


@comment_router.post("/add-new-comment_to_song", response_model=CommentSchema)
def create_comment_about_song(comment: CommentSchemaIn, song: SongSchema):
    return CommentController.create_comment_about_song(header=comment.header, text=comment.text,
                                                       user_username=comment.user_username,
                                                       song_id=song.id)


@comment_router.get("/get-comment-by-id", response_model=CommentSchema)
def get_comment_by_id(id: str):
    return CommentController.get_comment_by_id(id)


@comment_router.get("/get-all-comments", response_model=list[CommentSchema])
def get_all_comments():
    return CommentController.get_all_comment()


@comment_router.get("/get-all-comments-from-a-user", response_model=list[CommentSchema])
def get_all_comments_from_user(user_username: str):
    return CommentController.get_all_comments_from_user(user_username)


@comment_router.delete("/delete-comment-by-id")
def delete_comment_by_id(id: str):
    return CommentController.delete_comment_by_id(id)


@comment_router.put("/update-comment-by-id", response_model=CommentSchema)
def update_comment(id: str, header=None, text=None):
    return CommentController.update_comment(id, header, text)
