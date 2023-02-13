from datetime import date
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.song.exceptions import SongNotFoundException
from app.song.model import Song


class SongRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_song(self, name: str, length: int, date_of_release: date, artist_id: str):
        try:
            song = Song(name, length, date_of_release, artist_id)
            self.db.add(song)
            self.db.commit()
            self.db.refresh(song)
            return song
        except IntegrityError as e:
            raise e

    def create_explicit_song(self, name: str, length: int, date_of_release: date, artist_id: str):
        try:
            song = Song(name, length, date_of_release, artist_id, explicit=True)
            self.db.add(song)
            self.db.commit()
            self.db.refresh(song)
            return song
        except IntegrityError as e:
            raise e

    def get_song_by_id(self, id: str):
        song = self.db.query(Song).filter(Song.id == id).first()
        if song is None:
            raise SongNotFoundException(f"Song with provided id: {id} not found.", 400)
        return song

    def get_song_by_characters(self, characters: str):
        songs = self.db.query(Song).filter(Song.name.like(characters + "%")).all()
        if songs is None:
            raise SongNotFoundException(f"Song with provided characters: {characters} not found.", 400)
        return songs

    def get_all_songs(self):
        songs = self.db.query(Song).all()
        return songs

    def delete_song_by_id(self, id: str):
        try:
            song = self.db.query(Song).filter(Song.id == id).first()
            if song is None:
                raise SongNotFoundException(f"Song with provided id: {id} not found.", 400)
            self.db.delete(song)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def update_song(self, id: str, name=None, length=None, items_sold=None, lyrics=None, date_of_release=None,
                    ratings=None, explicit=None, album_id=None, artist_id=None, genre_name=None,
                    award_name=None, user_username=None, record_label_id=None):
        try:
            song = self.db.query(Song).filter(Song.id == id).first()
            if song is None:
                raise SongNotFoundException(f"Song with provided id: {id} not found.", 400)
            if name is not None:
                song.name = name
            if length is not None:
                song.length = length
            if items_sold is not None:
                song.items_sold = items_sold
            if length is not None:
                song.lyrics = lyrics
            if date_of_release is not None:
                song.date_of_release = date_of_release
            if ratings is not None:
                song.ratings = ratings
            if explicit is not None:
                song.explicit = explicit
            if album_id is not None:
                song.album_id = album_id
            if artist_id is not None:
                song.artist_id = artist_id
            if genre_name is not None:
                song.genre_name = genre_name
            if award_name is not None:
                song.award_name = award_name
            if user_username is not None:
                song.user_username = user_username
            if record_label_id is not None:
                song.record_label_id = record_label_id
            self.db.add(song)
            self.db.commit()
            self.db.refresh(song)
            return song
        except Exception as e:
            raise e
