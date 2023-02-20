from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.album import Album
from app.album.exceptions import AlbumNotFoundException
from app.artist.exceptions import ArtistNotFoundException
from app.artist.model import Artist
from app.award import Award
from app.award.exceptions import AwardNotFoundException
from app.genre.exceptions import GenreNotFoundException
from app.genre.model import Genre
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
                      country_name=None, record_label_id=None):
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
            if country_name is not None:
                artist.country_name = country_name
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

    def add_award_to_artist(self, artist_id: str, award_id: str):
        try:
            artist = self.db.query(Artist).filter(Artist.id == artist_id).first()
            if not artist:
                raise ArtistNotFoundException(f"Artists with provided id: {artist_id} not found.", 400)
            award = self.db.query(Award).filter(Award.id == award_id).first()
            if not award:
                raise AwardNotFoundException(f"Award with provided id: {award_id} not found.", 400)
            artist.awards.append(award)
            self.db.add(artist)
            self.db.commit()
            self.db.refresh(artist)
            return artist
        except IntegrityError as e:
            raise e

    def add_genre_to_artist(self, artist_id: str, genre_name: str):
        try:
            artist = self.db.query(Artist).filter(Artist.id == artist_id).first()
            if not artist:
                raise ArtistNotFoundException(f"Artists with provided id: {artist_id} not found.", 400)
            genre = self.db.query(Genre).filter(Genre.name == genre_name).first()
            if not genre:
                raise GenreNotFoundException(f"Genre with provided name: {genre_name} not found.", 400)
            artist.genres.append(genre)
            self.db.add(artist)
            self.db.commit()
            self.db.refresh(artist)
            return artist
        except IntegrityError as e:
            raise e
