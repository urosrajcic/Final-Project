from fastapi import APIRouter, Depends

from app.comment.controller import CommentController
from app.comment.schemas import *
from app.user.controller import JWTBearer

comment_router = APIRouter(tags=["Comments"], prefix="/mdb/comments")


@comment_router.post("/create-comment", response_model=CommentSchema)
def create_comment(comment: CommentSchemaIn):
    return CommentController.create_comment(header=comment.header, text=comment.text,
                                            user_username=comment.user_username, )


@comment_router.get("/get-comment-by-id", response_model=CommentSchema)
def get_comment_by_id(id: str):
    return CommentController.get_comment_by_id(id=id)


@comment_router.get("/get-all-comments", response_model=list[CommentSchema])
def get_all_comments():
    return CommentController.get_all_comment()


@comment_router.get("/get-news", response_model=list[CommentSchema])
def get_news():
    return CommentController.get_news()


@comment_router.get("/get-album-reviews", response_model=list[CommentSchema])
def get_album_reviews(album_id: str):
    return CommentController.get_album_reviews(album_id=album_id)


@comment_router.get("/get-artist-reviews", response_model=list[CommentSchema])
def get_artist_reviews(artist_id: str):
    return CommentController.get_artist_reviews(artist_id=artist_id)


@comment_router.get("/get-song-reviews", response_model=list[CommentSchema])
def get_song_reviews(song_id: str):
    return CommentController.get_song_reviews(song_id=song_id)


@comment_router.get("/get-all-comments-from-a-user", response_model=list[CommentSchema])
def get_all_comments_from_user(user_username: str):
    return CommentController.get_all_comments_from_user(user_username=user_username)


@comment_router.delete("/delete-comment-by-id", dependencies=[Depends(JWTBearer("super_user")),
                                                              Depends(JWTBearer("classic_user")),
                                                              Depends(JWTBearer("critic")),
                                                              Depends(JWTBearer("writer"))])
def delete_comment_by_id(id: str):
    return CommentController.delete_comment_by_id(id=id)


@comment_router.put("/update-comment", response_model=CommentSchema, dependencies=[Depends(JWTBearer("super_user")),
                                                                                   Depends(JWTBearer("classic_user")),
                                                                                   Depends(JWTBearer("critic")),
                                                                                   Depends(JWTBearer("writer"))])
def update_comment(comment: CommentSchema):
    return CommentController.update_comment(id=comment.id.__str__(), header=comment.header, text=comment.text)
