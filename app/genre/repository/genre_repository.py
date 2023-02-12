from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.genre.model import Genre
from app.genre.exceptions import GenreNotFoundException


class GenreRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_genre(self, name):
        try:
            genre = Genre(name)
            self.db.add(genre)
            self.db.commit()
            self.db.refresh(genre)
            return genre
        except IntegrityError as e:
            raise e

    def get_genre_by_characters(self, characters: str):
        genre = self.db.query(Genre).filter(Genre.name.like(characters + "%")).all()
        if genre is None:
            raise Genre(f"Genre with provided characters: {characters} not found.", 400)
        return genre

    def get_all_genres(self):
        genres = self.db.query(Genre).all()
        return genres

    def delete_genre_by_name(self, name: str):
        try:
            genre = self.db.query(Genre).filter(Genre.name == name).first()
            if genre is None:
                raise GenreNotFoundException(f"Genre with provided name: {name} not found.", 400)
            self.db.delete(genre)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def update_genre(self, name: str, song_id=None, artist_id=None, album_id=None):
        try:
            genre = self.db.query(Genre).filter(Genre.name == name).first()
            if genre is None:
                raise GenreNotFoundException(f"Genre with provided name: {name} not found.", 400)
            if song_id is not None:
                genre.song_id = song_id
            if artist_id is not None:
                genre.artist_id = artist_id
            if album_id is False:
                genre.album_id = album_id
            self.db.add(genre)
            self.db.commit()
            self.db.refresh(genre)
            return genre
        except Exception as e:
            raise e
