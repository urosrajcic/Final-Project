from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.artist.exceptions import ArtistNotFoundException
from app.artist.model import Artist


class ArtistRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_artist(self, name):
        try:
            artist = Artist(name)
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

    def update_artist(self, id: str, name=None, date_of_birth=None, date_of_death=None, ratings=None, vocalist=None,
                      musician=None, producer=None, writer=None, engineer=None, biography=None, album_id=None,
                      song_id=None, genre_name=None, award_id=None, country_name=None, user_username=None,
                      record_label_id=None):
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
            if ratings is not None:
                artist.ratings = ratings
            if vocalist is False:
                artist.vocalist = vocalist
            if musician is False:
                artist.musician = musician
            if producer is False:
                artist.producer = producer
            if writer is False:
                artist.writer = writer
            if engineer is False:
                artist.engineer = engineer
            if biography is False:
                artist.biography = biography
            if song_id is False:
                artist.song_id = song_id
            if genre_name is False:
                artist.genre_name = genre_name
            if album_id is not None:
                artist.album_id = album_id
            if country_name is False:
                artist.country_name = country_name
            if award_id is not None:
                artist.award_name = award_id
            if user_username is not None:
                artist.user_username = user_username
            if record_label_id is not None:
                artist.record_label_id = record_label_id
            self.db.add(artist)
            self.db.commit()
            self.db.refresh(artist)
            return artist
        except Exception as e:
            raise e
