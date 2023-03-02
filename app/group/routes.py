from fastapi import APIRouter, Depends

from app.album.schemas import *
from app.group.controller import GroupController
from app.song.schemas import *
from app.group.schemas import *
from app.user.controller import JWTBearer

group_router = APIRouter(tags=["Groups"], prefix="/api/groups")


@group_router.post("/add-new-group", response_model=GroupSchema, dependencies=[Depends(JWTBearer("super_user"))])
def create_group(group: GroupSchemaIn):
    return GroupController.create_group(name=group.name, country_name=group.country_name,
                                        date_of_forming=group.date_of_forming)


@group_router.get("/get-group-by-id", response_model=GroupSchema)
def get_group_by_id(id: str):
    return GroupController.get_group_by_id(id=id)


@group_router.get("/get-groups-by-characters", response_model=list[GroupSchemaOut])
def get_groups_by_characters(characters: str):
    return GroupController.get_groups_by_characters(characters=characters)


@group_router.get("/get-all-groups", response_model=list[GroupSchemaOut])
def get_all_groups():
    return GroupController.get_all_groups()


@group_router.get("/get-groups-by-rating", response_model=list[GroupSchemaOut])
def get_groups_by_rating():
    return GroupController.get_groups_by_rating()


@group_router.get("/get-groups-from-country", response_model=list[GroupSchemaOut])
def get_groups_from_country(country: str):
    return GroupController.get_groups_from_country(country=country)


@group_router.get("/get-group-with_most_awards", response_model=GroupSchema)
def get_group_with_most_awards():
    return GroupController.get_group_with_most_awards()


@group_router.get("/get-groups-by-genre", response_model=list[GroupSchemaOut])
def get_groups_by_genre(genre: str):
    return GroupController.get_groups_by_genre(genre=genre)


@group_router.get("/get-all-comments-about-group")
def get_all_comments_about_group(id: str):
    return GroupController.get_all_comments_about_group(id=id)


@group_router.delete("/delete-group-by-id", dependencies=[Depends(JWTBearer("super_user"))])
def delete_group_by_id(id: str):
    return GroupController.delete_group_by_id(id=id)


@group_router.put("/update-group", response_model=GroupSchema, dependencies=[Depends(JWTBearer("super_user"))])
def update_group(group: GroupSchema):
    return GroupController.update_group(id=group.id.__str__(), name=group.name, date_of_forming=group.date_of_forming,
                                        date_of_disband=group.date_of_disband, vocalist=group.vocalist,
                                        musician=group.musician, producer=group.producer, writer=group.writer,
                                        engineer=group.engineer, biography=group.biography, ratings=group.ratings,
                                        country_name=group.country_name, record_label_id=group.record_label_id)


@group_router.put("/add-song-to-group", response_model=GroupSchema, dependencies=[Depends(JWTBearer("super_user"))])
def add_song_to_group(group: GroupSchema, song: SongSchemaOut):
    return GroupController.add_song_to_group(group_id=group.id.__str__(), song_id=song.id.__str__())


@group_router.put("/add-album-to-group", response_model=GroupSchema, dependencies=[Depends(JWTBearer("super_user"))])
def add_album_to_group(group: GroupSchema, album: AlbumSchemaOut):
    return GroupController.add_album_to_group(group_id=group.id.__str__(), album_id=album.id.__str__())


@group_router.put("/add-award-to-group", response_model=GroupSchema, dependencies=[Depends(JWTBearer("super_user"))])
def add_award_to_group(group: GroupSchema, award: AwardSchema):
    return GroupController.add_award_to_group(group_id=group.id.__str__(), award_id=award.id.__str__())


@group_router.put("/add-genre-to-group", response_model=GroupSchema, dependencies=[Depends(JWTBearer("super_user"))])
def add_genre_to_group(group: GroupSchema, genre: GenreSchema):
    return GroupController.add_genre_to_group(group_id=group.id.__str__(), genre_name=genre.name)


@group_router.put("/add-comment-to-group", response_model=GroupSchema,
                  dependencies=[Depends(JWTBearer("super_user")), Depends(JWTBearer("classic_user")),
                                Depends(JWTBearer("critic")), Depends(JWTBearer("writer"))])
def add_comment_to_group(group: GroupSchema, comment: CommentSchema):
    return GroupController.add_comment_to_group(group_id=group.id.__str__(), comment_id=comment.id.__str__())


@group_router.put("/remove-song-from-group", response_model=GroupSchema,
                  dependencies=[Depends(JWTBearer("super_user"))])
def remove_song_from_group(group: GroupSchema, song: SongSchemaOut):
    return GroupController.remove_song_from_group(group_id=group.id.__str__(), song_id=song.id.__str__())


@group_router.put("/remove-album-from-group", response_model=GroupSchema,
                  dependencies=[Depends(JWTBearer("super_user"))])
def remove_album_from_group(group: GroupSchema, album: AlbumSchemaOut):
    return GroupController.remove_album_from_group(group_id=group.id.__str__(), album_id=album.id.__str__())


@group_router.put("/remove-award-from-group", response_model=GroupSchema,
                  dependencies=[Depends(JWTBearer("super_user"))])
def remove_award_from_group(group: GroupSchema, award: AwardSchema):
    return GroupController.remove_award_from_group(group_id=group.id.__str__(), award_id=award.id.__str__())


@group_router.put("/remove-genre-from-group", response_model=GroupSchema,
                  dependencies=[Depends(JWTBearer("super_user"))])
def remove_genre_from_group(group: GroupSchema, genre: GenreSchema):
    return GroupController.remove_genre_from_group(group_id=group.id.__str__(), genre_name=genre.name)


@group_router.put("/remove-comment-from-group", response_model=GroupSchema,
                  dependencies=[Depends(JWTBearer("super_user")), Depends(JWTBearer("classic_user")),
                                Depends(JWTBearer("critic")), Depends(JWTBearer("writer"))])
def remove_comment_from_group(group: GroupSchema, comment: CommentSchema):
    return GroupController.remove_comment_from_group(group_id=group.id.__str__(), comment_id=comment.id.__str__())
