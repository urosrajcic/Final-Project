from fastapi import APIRouter, Depends

from app.user.controller import UserController
from app.user.schemas import *
from app.user.schemas.user_ratings_schemas import *
from app.user.controller.user_auth_controller import JWTBearer

user_router = APIRouter(tags=["Users"], prefix="/api/users")


@user_router.post("/login")
def login_user(user: UserSchemaLogin):
    return UserController.login_user(user.email, user.password)


@user_router.post("/add-new-user", response_model=UserSchema)
def create_user(user: UserSchemaIn):
    return UserController.create_user(username=user.username, email=user.email, password=user.password,
                                      name=user.name, surname=user.surname, date_of_birth=user.date_of_birth,
                                      country_name=user.country_name)


@user_router.post("/add-new-critic", response_model=UserSchema, dependencies=[Depends(JWTBearer("super_user"))])
def create_critic(user: UserSchemaIn):
    return UserController.create_critic(username=user.username, email=user.email, password=user.password,
                                        name=user.name, surname=user.surname, date_of_birth=user.date_of_birth,
                                        country_name=user.country_name)


@user_router.post("/add-new-writer", response_model=UserSchema, dependencies=[Depends(JWTBearer("super_user"))])
def create_writer(user: UserSchemaIn):
    return UserController.create_writer(username=user.username, email=user.email, password=user.password,
                                        name=user.name, surname=user.surname, date_of_birth=user.date_of_birth,
                                        country_name=user.country_name)


@user_router.post("/add-new-critic-and_writer", response_model=UserSchema,
                  dependencies=[Depends(JWTBearer("super_user"))])
def create_writer_and_critic(user: UserSchemaIn):
    return UserController.create_writer_and_critic(username=user.username, email=user.email, password=user.password,
                                                   name=user.name, surname=user.surname,
                                                   date_of_birth=user.date_of_birth,
                                                   country_name=user.country_name)


@user_router.post("/add-new-super-user", response_model=UserSchema, dependencies=[Depends(JWTBearer("super_user"))])
def create_super_user(user: UserSchemaIn):
    return UserController.create_super_user(username=user.username, email=user.email, password=user.password,
                                            name=user.name, surname=user.surname, date_of_birth=user.date_of_birth,
                                            country_name=user.country_name)


@user_router.get("/get-user-by-email", response_model=UserSchema)
def get_user_by_email(email: str):
    return UserController.get_user_by_email(email=email)


@user_router.get("/get-users-by-characters", response_model=list[UserSchemaOut])
def get_users_by_characters(characters: str):
    return UserController.get_users_by_characters(characters=characters)


@user_router.get("/get-all-users", response_model=list[UserSchemaOut])
def get_all_users():
    return UserController.get_all_users()


@user_router.delete("/delete-user-by-username", dependencies=[Depends(JWTBearer("super_user"))])
def delete_user_by_username(username: str):
    return UserController.delete_user_by_username(username=username)


@user_router.put("/update-user", response_model=UserSchema, dependencies=[Depends(JWTBearer("super_user"))])
def update_user(user: UserSchema):
    return UserController.update_user(username=user.username, password=user.password, name=user.name, surname=user.name,
                                      date_of_birth=user.date_of_birth.__str__(), country_name=user.country_name)


@user_router.post("/add-new-user-album-rating", response_model=UserRatingAlbumSchema,
                  dependencies=[Depends(JWTBearer("classic_user"))])
def create_user_album_rating(user_rating: UserRatingAlbumSchemaIn):
    return UserController.rate_album(username=user_rating.user_username, album_id=user_rating.album_id,
                                     rating=user_rating.rating)


@user_router.post("/add-new-user-artist-rating", response_model=UserRatingArtistSchema,
                  dependencies=[Depends(JWTBearer("classic_user"))])
def create_user_artist_rating(user_rating: UserRatingArtistSchemaIn):
    return UserController.rate_artist(username=user_rating.user_username, artist_id=user_rating.artist_id,
                                      rating=user_rating.rating)


@user_router.post("/add-new-user-song-rating", response_model=UserRatingSongSchema,
                  dependencies=[Depends(JWTBearer("classic_user"))])
def create_user_song_rating(user_rating: UserRatingSongSchemaIn):
    return UserController.rate_song(username=user_rating.user_username, song_id=user_rating.song_id,
                                    rating=user_rating.rating)
