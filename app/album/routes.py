from fastapi import APIRouter, Depends
from app.album.controller import AlbumController
from app.album.schemas import *
from app.artist.schemas import ArtistSchema
from app.user.controller import JWTBearer

album_router = APIRouter(tags=["Albums"], prefix="/mdb/albums")


@album_router.post("/add-new-album", response_model=AlbumSchema, dependencies=[Depends(JWTBearer("super_user"))])
def create_album(album: AlbumSchemaIn):
    return AlbumController.create_album(name=album.name, length=album.length, date_of_release=album.date_of_release,
                                        )


@album_router.get("/get-album-by-id", response_model=AlbumSchema)
def get_album_by_id(id: str):
    return AlbumController.get_album_by_id(id=id)


@album_router.get("/get-albums-by-characters", response_model=list[AlbumSchema])
def get_albums_by_name(characters: str):
    return AlbumController.get_albums_by_characters(characters=characters)


@album_router.get("/get-all-albums", response_model=list[AlbumSchema])
def get_all_albums():
    return AlbumController.get_all_albums()


@album_router.get("/get-albums-by-rating", response_model=list[AlbumSchema])
def get_albums_by_rating():
    return AlbumController.get_albums_by_rating()


@album_router.get("/get-best-albums-from-year", response_model=list[AlbumSchema])
def get_best_albums_from_year(year: str):
    return AlbumController.get_best_albums_from_year(year)


@album_router.get("/get-album-with_most_awards", response_model=AlbumSchema)
def get_album_with_most_awards():
    return AlbumController.get_album_with_most_awards()


@album_router.get("/get-albums-by-genre", response_model=list[AlbumSchema])
def get_albums_by_genre(genre: str):
    return AlbumController.get_albums_by_genre(genre=genre)


@album_router.get("/get-all-comments-about-album")
def get_all_comments_about_album(id: str):
    return AlbumController.get_all_comments_about_album(id=id)


@album_router.delete("/delete-album-by-id", dependencies=[Depends(JWTBearer("super_user"))])
def delete_album_by_id(id: str):
    return AlbumController.delete_album_by_id(id=id)


@album_router.put("/update-album", response_model=AlbumSchema, dependencies=[Depends(JWTBearer("super_user"))])
def update_album(album: AlbumSchema):
    return AlbumController.update_album(id=album.id.__str__(), name=album.name, length=album.length,
                                        date_of_release=album.date_of_release, items_sold=album.items_sold,
                                        ratings=album.ratings, explicit=album.explicit, lp=album.lp, ep=album.ep,
                                        single=album.single, mixtape=album.mixtape)


@album_router.put("/add-artist-to-album", response_model=AlbumSchema, dependencies=[Depends(JWTBearer("super_user"))])
def add_artist_to_album(album: AlbumSchema, artist: ArtistSchema):
    return AlbumController.add_artist_to_album(album_id=album.id.__str__(), artist_id=artist.id.__str__())


@album_router.put("/add-song-to-album", response_model=AlbumSchema, dependencies=[Depends(JWTBearer("super_user"))])
def add_song_to_album(album: AlbumSchema, song: SongSchema):
    return AlbumController.add_song_to_album(album_id=album.id.__str__(), song_id=song.id.__str__())


@album_router.put("/add-award-to-album", response_model=AlbumSchema, dependencies=[Depends(JWTBearer("super_user"))])
def add_award_to_album(album: AlbumSchema, award: AwardSchema):
    return AlbumController.add_award_to_album(album_id=album.id.__str__(), award_id=award.id.__str__())


@album_router.put("/add-genre-to-album", response_model=AlbumSchema, dependencies=[Depends(JWTBearer("super_user"))])
def add_genre_to_album(album: AlbumSchema, genre: GenreSchema):
    return AlbumController.add_genre_to_album(album_id=album.id.__str__(), genre_name=genre.name)


@album_router.put("/add-comment-to-album", response_model=AlbumSchema, dependencies=[Depends(JWTBearer("super_user")),
                                                                                     Depends(JWTBearer("classic_user")),
                                                                                     Depends(JWTBearer("critic")),
                                                                                     Depends(JWTBearer("writer"))])
def add_comment_to_album(album: AlbumSchema, comment: CommentSchema):
    return AlbumController.add_comment_to_album(album_id=album.id.__str__(), comment_id=comment.id.__str__())


@album_router.put("/remove-artist-from-album", response_model=AlbumSchema,
                  dependencies=[Depends(JWTBearer("super_user"))])
def remove_artist_from_album(album: AlbumSchema, artist: ArtistSchema):
    return AlbumController.remove_artist_from_album(album_id=album.id.__str__(), artist_id=artist.id.__str__())


@album_router.put("/remove-song-from-album", response_model=AlbumSchema,
                  dependencies=[Depends(JWTBearer("super_user"))])
def remove_song_from_album(album: AlbumSchema, song: SongSchema):
    return AlbumController.remove_song_from_album(album_id=album.id.__str__(), song_id=song.id.__str__())


@album_router.put("/remove-award-from-album", response_model=AlbumSchema,
                  dependencies=[Depends(JWTBearer("super_user"))])
def remove_award_from_album(album: AlbumSchema, award: AwardSchema):
    return AlbumController.remove_award_from_album(album_id=album.id.__str__(), award_id=award.id.__str__())


@album_router.put("/remove-genre-from-album", response_model=AlbumSchema,
                  dependencies=[Depends(JWTBearer("super_user"))])
def remove_genre_from_album(album: AlbumSchema, genre: GenreSchema):
    return AlbumController.remove_genre_from_album(album_id=album.id.__str__(), genre_name=genre.name)


@album_router.put("/remove-comment-from-album", response_model=AlbumSchema,
                  dependencies=[Depends(JWTBearer("super_user")), Depends(JWTBearer("classic_user")),
                                Depends(JWTBearer("critic")), Depends(JWTBearer("writer"))])
def remove_comment_from_album(album: AlbumSchema, comment: CommentSchema):
    return AlbumController.remove_comment_from_album(album_id=album.id.__str__(), comment_id=comment.id.__str__())
