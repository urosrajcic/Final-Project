from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.album.exceptions import AlbumNotFoundException
from app.album.model import Album
from app.artist import Artist
from app.artist.exceptions import ArtistNotFoundException
from app.song import Song
from app.song.exceptions import SongNotFoundException


class AlbumRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_album(self, name: str, length: int, date_of_release: str):
        try:
            album = Album(name, length, date_of_release)
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
                     explicit=None, lp=None, ep=None, single=None, mixtape=None, genre_name=None, award_id=None):
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
            if explicit is None:
                album.explicit = False
            else:
                album.explicit = True
            if lp is None:
                album.lp = False
            else:
                album.lp = True
            if ep is None:
                album.ep = False
            else:
                album.ep = True
            if single is None:
                album.single = False
            else:
                album.single = True
            if mixtape is None:
                album.mixtape = False
            else:
                album.mixtape = True
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

    def add_artist_to_album(self, album_id: str, artist_id: str):
        try:
            album = self.db.query(Album).filter(Album.id == album_id).first()
            if not album:
                raise AlbumNotFoundException(f"Album with provided id: {album_id} not found.", 400)
            artist = self.db.query(Artist).filter(Artist.id == artist_id).first()
            if not artist:
                raise ArtistNotFoundException(f"Artist with provided id: {artist_id} not found.", 400)

            album.artists.append(artist)
            self.db.add(album)
            self.db.commit()
            self.db.refresh(album)
            return album
        except IntegrityError as e:
            raise e

    def add_song_to_album(self, album_id: str, song_id: str):
        try:
            album = self.db.query(Album).filter(Album.id == album_id).first()
            if not album:
                raise AlbumNotFoundException(f"Album with provided id: {album_id} not found.", 400)
            song = self.db.query(Song).filter(Song.id == song_id).first()
            if not song:
                raise SongNotFoundException(f"Song with provided id: {song_id} not found.", 400)

            album.artists.append(song)
            self.db.add(album)
            self.db.commit()
            self.db.refresh(album)
            return album
        except IntegrityError as e:
            raise e
