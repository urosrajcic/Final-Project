from fastapi import APIRouter, Depends

from app.album.schemas import AlbumSchema
from app.artist.schemas import ArtistSchema
from app.song.controller import SongController
from app.song.schemas import *
from app.user.controller import JWTBearer

song_router = APIRouter(tags=["Songs"], prefix="/mdb/songs")


@song_router.post("/add-new-song", response_model=SongSchema, dependencies=[Depends(JWTBearer("super_user"))])
def create_song(song: SongSchemaIn):
    return SongController.create_song(name=song.name, length=song.length, date_of_release=song.date_of_release)


@song_router.get("/get-song-by-id", response_model=SongSchema)
def get_song_by_id(id: str):
    return SongController.get_song_by_id(id=id)


@song_router.get("/get-songs-by-characters", response_model=list[SongSchema])
def get_songs_by_characters(characters: str):
    return SongController.get_songs_by_characters(characters=characters)


@song_router.get("/get-all-songs", response_model=list[SongSchema])
def get_all_songs():
    return SongController.get_all_songs()


@song_router.get("/get-songs-by-rating", response_model=list[SongSchema])
def get_songs_by_rating():
    return SongController.get_songs_by_rating()


@song_router.get("/get-best-songs-from-year", response_model=list[SongSchema])
def get_best_songs_from_year(year: str):
    return SongController.get_best_songs_from_year(year)


@song_router.get("/get-song-with_most_awards", response_model=SongSchema)
def get_song_with_most_awards():
    return SongController.get_song_with_most_awards()


@song_router.get("/get-songs-by-genre", response_model=list[SongSchema])
def get_songs_by_genre(genre: str):
    return SongController.get_songs_by_genre(genre=genre)


@song_router.get("/get-all-comments-about-song")
def get_all_comments_about_song(id: str):
    return SongController.get_all_comments_about_song(id=id)


@song_router.delete("/delete-song-by-id")
def delete_song_by_id(id: str):
    return SongController.delete_song_by_id(id=id)


@song_router.put("/update-song", response_model=SongSchema, dependencies=[Depends(JWTBearer("super_user"))])
def update_song(song: SongSchema):
    return SongController.update_song(id=song.id.__str__(), name=song.name, length=song.length,
                                      date_of_release=song.date_of_release, items_sold=song.items_sold,
                                      lyrics=song.lyrics, ratings=song.ratings, explicit=song.explicit)


@song_router.put("/add-artist-to-song", response_model=SongSchema, dependencies=[Depends(JWTBearer("super_user"))])
def add_artist_to_song(song: SongSchema, artist: ArtistSchema):
    return SongController.add_artist_to_song(song_id=song.id.__str__(), artist_id=artist.id.__str__())


@song_router.put("/add-album-to-song", response_model=SongSchema, dependencies=[Depends(JWTBearer("super_user"))])
def add_album_to_song(song: SongSchema, album: AlbumSchema):
    return SongController.add_album_to_song(song_id=song.id.__str__(), album_id=album.id.__str__())


@song_router.put("/add-award-to-song", response_model=SongSchema, dependencies=[Depends(JWTBearer("super_user"))])
def add_award_to_song(song: SongSchema, award: AwardSchema):
    return SongController.add_award_to_song(song_id=song.id.__str__(), award_id=award.id.__str__())


@song_router.put("/add-genre-to-song", response_model=SongSchema, dependencies=[Depends(JWTBearer("super_user"))])
def add_genre_to_song(song: SongSchema, genre: GenreSchema):
    return SongController.add_genre_to_song(song_id=song.id.__str__(), genre_name=genre.name)


@song_router.put("/add-comment-to-song", response_model=SongSchema, dependencies=[Depends(JWTBearer("super_user"))])
def add_comment_to_song(song: SongSchema, comment: CommentSchema):
    return SongController.add_comment_to_song(song_id=song.id.__str__(), comment_id=comment.id.__str__())


@song_router.put("/remove-artist-from-song", response_model=SongSchema, dependencies=[Depends(JWTBearer("super_user"))])
def remove_artist_to_song(song: SongSchema, artist: ArtistSchema):
    return SongController.remove_artist_from_song(song_id=song.id.__str__(), artist_id=artist.id.__str__())


@song_router.put("/remove-album-from-song", response_model=SongSchema, dependencies=[Depends(JWTBearer("super_user"))])
def remove_album_from_song(song: SongSchema, album: AlbumSchema):
    return SongController.remove_album_from_song(song_id=song.id.__str__(), album_id=album.id.__str__())


@song_router.put("/remove-award-from-song", response_model=SongSchema, dependencies=[Depends(JWTBearer("super_user"))])
def remove_award_from_song(song: SongSchema, award: AwardSchema):
    return SongController.remove_award_from_song(song_id=song.id.__str__(), award_id=award.id.__str__())


@song_router.put("/remove-genre-from-song", response_model=SongSchema, dependencies=[Depends(JWTBearer("super_user"))])
def remove_genre_from_song(song: SongSchema, genre: GenreSchema):
    return SongController.remove_genre_from_song(song_id=song.id.__str__(), genre_name=genre.name)


@song_router.put("/remove-comment-from-song", response_model=SongSchema,
                 dependencies=[Depends(JWTBearer("super_user"))])
def remove_comment_from_song(song: SongSchema, comment: CommentSchema):
    return SongController.remove_comment_from_song(song_id=song.id.__str__(), comment_id=comment.id.__str__())
