from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.album import Album
from app.album.exceptions import AlbumNotFoundException
from app.artist.exceptions import ArtistNotFoundException
from app.artist.model import Artist
from app.song import Song
from app.song.exceptions import SongNotFoundException


class ArtistRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_artist(self, name: str, country_name: str, date_of_birth: str):
        try:
            artist = Artist(name, country_name, date_of_birth)
            self.db.add(artist)
            self.db.commit()
            self.db.refresh(artist)
            return artist
        except IntegrityError as e:
            raise e

    def get_artist_by_id(self, id: str):
        artist = self.db.query(Artist).filter(Artist.id == id).first()
        if artist is None:
            raise ArtistNotFoundException(f"Artist with provided id: {id} not found.", 400)
        return artist

    def get_artists_by_name(self, name: str):
        artists = self.db.query(Artist).filter(Artist.name.like(name + "%")).all()
        if artists is None:
            raise ArtistNotFoundException(f"Artists with provided name: {name} not found.", 400)
        return artists

    def get_all_artists(self):
        artists = self.db.query(Artist).all()
        return artists

    def delete_artis_by_id(self, id: str):
        try:
            artist = self.db.query(Artist).filter(Artist.id == id).first()
            if artist is None:
                raise ArtistNotFoundException(f"Artist with provided id: {id} not found.", 400)
            self.db.delete(artist)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def update_artist(self, id: str, name=None, date_of_birth=None, date_of_death=None, vocalist=None,
                      musician=None, producer=None, writer=None, engineer=None, biography=None,
                      genre_name=None, award_id=None, country_name=None, record_label_id=None):
        try:
            artist = self.db.query(Artist).filter(Artist.id == id).first()
            if artist is None:
                raise ArtistNotFoundException(f"Artist with provided id: {id} not found.", 400)
            if name is not None:
                artist.name = name
            if date_of_birth is not None:
                artist.date_of_birth = date_of_birth
            if date_of_death is not None:
                artist.date_of_death = date_of_death
            if vocalist is None:
                artist.vocalist = False
            else:
                artist.vocalist = True
            if musician is None:
                artist.musician = False
            else:
                artist.musician = True
            if producer is None:
                artist.producer = False
            else:
                artist.producer = True
            if writer is None:
                artist.writer = False
            else:
                artist.writer = True
            if engineer is None:
                artist.engineer = False
            else:
                artist.engineer = True
            if biography is not None:
                artist.biography = biography
            if genre_name is not None:
                artist.genre_name = genre_name
            if country_name is not None:
                artist.country_name = country_name
            if award_id is not None:
                artist.award_name = award_id
            if record_label_id is not None:
                artist.record_label_id = record_label_id
            self.db.add(artist)
            self.db.commit()
            self.db.refresh(artist)
            return artist
        except Exception as e:
            raise e

    def add_song_to_artist(self, artist_id: str, song_id: str):
        try:
            artist = self.db.query(Artist).filter(Artist.id == artist_id).first()
            if not artist:
                raise ArtistNotFoundException(f"Artists with provided id: {artist_id} not found.", 400)
            song = self.db.query(Song).filter(Song.id == song_id).first()
            if not song:
                raise SongNotFoundException(f"Song with provided id: {song_id} not found.", 400)

            artist.songs.append(song)
            self.db.add(artist)
            self.db.commit()
            self.db.refresh(artist)
            return artist
        except IntegrityError as e:
            raise e

    def add_album_to_artist(self, artist_id: str, album_id: str):
        try:
            artist = self.db.query(Artist).filter(Artist.id == artist_id).first()
            if not artist:
                raise ArtistNotFoundException(f"Artists with provided id: {artist_id} not found.", 400)
            album = self.db.query(Album).filter(Album.id == album_id).first()
            if not album:
                raise AlbumNotFoundException(f"Album with provided id: {album_id} not found.", 400)

            artist.albums.append(album)
            self.db.add(artist)
            self.db.commit()
            self.db.refresh(artist)
            return artist
        except IntegrityError as e:
            raise e
