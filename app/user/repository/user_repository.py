from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.album import Album
from app.album.exceptions import AlbumNotFoundException
from app.artist import Artist
from app.artist.exceptions import ArtistNotFoundException
from app.song import Song
from app.song.exceptions import SongNotFoundException
from app.user.exceptions import UserNotFoundException
from app.user.model import User
from app.user.model.user_ratings import UserRating


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, username: str, email: str, password: str, name: str, surname: str,
                    date_of_birth: str, country_name: str):
        try:
            user = User(username, email, password, name, surname, date_of_birth, country_name)
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            return user
        except IntegrityError as e:
            raise e

    def create_critic(self, username: str, email: str, password: str, name: str, surname: str,
                      date_of_birth: str, country_name: str):
        try:
            critic = User(username=username, email=email, password=password, name=name, surname=surname,
                          date_of_birth=date_of_birth, country_name=country_name, critic=True)
            self.db.add(critic)
            self.db.commit()
            self.db.refresh(critic)
            return critic
        except IntegrityError as e:
            raise e

    def create_writer(self, username: str, email: str, password: str, name: str, surname: str,
                      date_of_birth: str, country_name: str):
        try:
            writer = User(username=username, email=email, password=password, name=name, surname=surname,
                          date_of_birth=date_of_birth, country_name=country_name, writer=True)
            self.db.add(writer)
            self.db.commit()
            self.db.refresh(writer)
            return writer
        except IntegrityError as e:
            raise e

    def create_writer_and_critic(self, username: str, email: str, password: str, name: str, surname: str,
                                 date_of_birth: str, country_name: str):
        try:
            user = User(username=username, email=email, password=password, name=name, surname=surname,
                        date_of_birth=date_of_birth, country_name=country_name, critic=True, writer=True)
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            return user
        except IntegrityError as e:
            raise e

    def get_user_by_username(self, username: str):
        user = self.db.query(User).filter(User.username == username).first()
        if user is None:
            raise UserNotFoundException(f"User with provided username: {username} not found.", 400)
        return user

    def get_users_by_characters(self, characters: str):
        users = self.db.query(User).filter(User.username.like(characters + "%")).all()
        if users is None:
            raise UserNotFoundException(f"User with provided characters: {characters} not found.", 400)
        return users

    def get_user_by_email(self, email: str):
        user = self.db.query(User).filter(User.email == email).first()
        if user is None:
            raise UserNotFoundException(f"User with provided email: {email} not found.", 400)
        return user

    def get_all_users(self):
        users = self.db.query(User).all()
        return users

    def delete_user_by_username(self, username: str):
        try:
            user = self.db.query(User).filter(User.username == username).first()
            if user is None:
                raise UserNotFoundException(f"User with provided username: {username} not found.", 400)
            self.db.delete(user)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def update_user(self, username: str, password: str = None, name: str = None,
                    surname: str = None, date_of_birth: str = None, country_name: str = None):
        try:
            user = self.db.query(User).filter(User.username == username).first()
            if user is None:
                raise UserNotFoundException(f"User with provided username: {username} not found.", 400)
            if password is not None:
                user.password = password
            if name is not None:
                user.name = name
            if surname is not None:
                user.surname = surname
            if date_of_birth is not None:
                user.date_of_birth = date_of_birth
            if country_name is not None:
                user.country_name = country_name
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            return user
        except Exception as e:
            raise e

    def rate_album(self, username: str, album_id: str, rating: int):
        try:
            user = self.db.query(User).filter(User.username == username).first()
            if user is None:
                raise UserNotFoundException(f"User with provided username: {username} not found.", 400)
            album = self.db.query(Album).filter(Album.id == album_id).first()
            if album is None:
                raise AlbumNotFoundException(f"Album with provided id: {album_id} not found.", 400)
            if not 1 <= rating <= 10:
                raise HTTPException(status_code=400, detail="Invalid rating")
            user_rating = UserRating(user_username=username, rating=rating, album_id=album_id)
            self.db.add(user_rating)
            self.db.commit()
            self.db.refresh(user_rating)
            return user_rating
        except IntegrityError as e:
            raise e

    def rate_artist(self, username: str, artist_id: str, rating: int):
        try:
            user = self.db.query(User).filter(User.username == username).first()
            if user is None:
                raise UserNotFoundException(f"User with provided username: {username} not found.", 400)
            artist = self.db.query(Artist).filter(Artist.id == artist_id).first()
            if artist is None:
                raise ArtistNotFoundException(f"Artist with provided id: {artist_id} not found.", 400)
            if not 1 <= rating <= 10:
                raise HTTPException(status_code=400, detail="Invalid rating")
            user_rating = UserRating(user_username=username, rating=rating, artist_id=artist_id)
            self.db.add(user_rating)
            self.db.commit()
            self.db.refresh(user_rating)
            return user_rating
        except IntegrityError as e:
            raise e

    def rate_song(self, username: str, song_id: str, rating: int):
        try:
            user = self.db.query(User).filter(User.username == username).first()
            if user is None:
                raise UserNotFoundException(f"User with provided username: {username} not found.", 400)
            song = self.db.query(Song).filter(Song.id == song_id).first()
            if song is None:
                raise SongNotFoundException(f"Song with provided id: {song_id} not found.", 400)
            if not 1 <= rating <= 10:
                raise HTTPException(status_code=400, detail="Invalid rating")
            user_rating = UserRating(user_username=username, rating=rating, song_id=song_id)
            self.db.add(user_rating)
            self.db.commit()
            self.db.refresh(user_rating)
            return user_rating
        except IntegrityError as e:
            raise e
