from datetime import date
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.album.exceptions import AlbumNotFoundException
from app.album.model import Album


class AlbumRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_album(self, name: str, date_of_release: date, song_id: str, artist_id: str):
        try:
            album = Album(name, date_of_release, song_id, artist_id)
            self.db.add(album)
            self.db.commit()
            self.db.refresh(album)
            return album
        except IntegrityError as e:
            raise e

    def get_album_by_id(self, id: str):
        album = self.db.query(Album).filter(Album.id == id).first()
        if album is None:
            raise AlbumNotFoundException(f"Album with provided id: {id} not found.", 400)
        return album

    def get_album_by_name(self, name: str):
        albums = self.db.query(Album).filter(Album.name.like(name + "%")).all()
        if albums is None:
            raise Album(f"Album with provided name: {name} not found.", 400)
        return albums

    def get_albums_by_artist(self, artist_id: str):
        albums = self.db.query(Album).filter(Album.artist_id == artist_id).all()
        if albums is None:
            raise Album(f"Album with provided artist id: {artist_id} not found.", 400)
        return albums

    def get_all_albums(self):
        albums = self.db.query(Album).all()
        return albums

    def delete_album_by_id(self, id: str):
        try:
            album = self.db.query(Album).filter(Album.id == id).first()
            if album is None:
                raise AlbumNotFoundException(f"Album with provided id: {id} not found.", 400)
            self.db.delete(album)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def update_album(self, id: str, name=None, length=None, date_of_release=None, items_sold=None, ratings=None,
                     explicit=None, lp=None, ep=None, single=None, mixtape=None, song_id=None, artis_id=None,
                     genre_name=None, award_id=None):
        try:
            album = self.db.query(Album).filter(Album.id == id).first()
            if album is None:
                raise AlbumNotFoundException(f"Album with provided id: {id} not found.", 400)
            if name is not None:
                album.name = name
            if length is not None:
                album.length = length
            if date_of_release is not None:
                album.date_of_release = date_of_release
            if items_sold is not None:
                album.items_sold = items_sold
            if ratings is not None:
                album.ratings = ratings
            if explicit is not None:
                album.explicit = explicit
            if lp is not None:
                album.lp = lp
            if ep is not None:
                album.ep = ep
            if single is not None:
                album.single = single
            if mixtape is not None:
                album.mixtape = mixtape
            if song_id is not None:
                album.song_id = song_id
            if artis_id is not None:
                album.artist_id = artis_id
            if genre_name is not None:
                album.genre_name = genre_name
            if award_id is not None:
                album.award_id = award_id
            self.db.add(album)
            self.db.commit()
            self.db.refresh(album)
            return album
        except Exception as e:
            raise e
