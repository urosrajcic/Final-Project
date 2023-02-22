from sqlalchemy import desc, text, and_
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.album import Album
from app.album.exceptions import AlbumNotFoundException
from app.artist.exceptions import ArtistNotFoundException
from app.artist.model import Artist
from app.award import Award
from app.award.exceptions import AwardNotFoundException
from app.comment import Comment
from app.comment.exceptions import CommentNotFoundException
from app.genre.exceptions import GenreNotFoundException
from app.genre.model import Genre
from app.song import Song
from app.song.exceptions import SongNotFoundException
from app.user.model.user_ratings import UserRating


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

    def calculate_average_rating_for_artist(self, artist_id: str):
        ratings = self.db.query(UserRating).filter_by(artist_id=artist_id).all()
        if not ratings:
            return 0.0
        total_rating = sum(rating.rating for rating in ratings)
        total_num_ratings = len(ratings)
        return total_rating / total_num_ratings

    def get_artist_by_id(self, id: str):
        artist = self.db.query(Artist).filter(Artist.id == id).first()
        if artist is None:
            raise ArtistNotFoundException(f"Artist with provided id: {id} not found.", 400)
        return artist

    def get_artists_by_characters(self, characters: str):
        artists = self.db.query(Artist).filter(Artist.name.like(characters + "%")).all()
        return artists

    def get_all_artists(self):
        artists = self.db.query(Artist).all()
        return artists

    def get_artists_by_rating(self):
        artists = self.db.query(Artist).order_by(desc(Artist.ratings)).all()
        return artists

    def get_artists_from_country(self, country: str):
        artists = self.db.query(Artist).filter(Artist.country_name == country).order_by(desc(Artist.ratings)).all()
        return artists

    def get_artist_with_most_awards(self):
        artists = self.db.query(Artist).all()
        if len(artists) == 0:
            raise ArtistNotFoundException("There is no artist in database.", 500)
        artist_max_awards = artists[0]
        for artist in artists:
            if len(artist.awards) > len(artist_max_awards.awards) > 0 or len(artist.awards) > 0:
                artist_max_awards = artist
            else:
                raise AlbumNotFoundException(f"There is no artist with awards.", 500)
        return artist_max_awards

    def get_artists_by_genre(self, genre: str):
        filter_expression = text(f"genre.name = '{genre}'")
        artists = self.db.query(Artist).filter(Artist.genres.any(filter_expression)).all()
        return artists

    def get_all_comments_about_artist(self, id: str):
        artist = self.db.query(Artist).filter(Artist.id == id).first()
        if artist is None:
            raise ArtistNotFoundException(f"Artist with provided id: {id} not found.", 400)
        return artist.comments

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
                      musician=None, producer=None, writer=None, engineer=None, biography=None, ratings=None,
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
            if ratings is not None:
                artist.ratings = ratings
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

    def add_comment_to_artist(self, artist_id: str, comment_id: str):
        try:
            artist = self.db.query(Artist).filter(Artist.id == artist_id).first()
            if not artist:
                raise ArtistNotFoundException(f"Artists with provided id: {artist_id} not found.", 400)
            comment = self.db.query(Comment).filter(Comment.id == comment_id).first()
            if not comment:
                raise CommentNotFoundException(f"Comment with provided id: {comment_id} not found.", 400)
            artist.comments.append(comment)
            self.db.add(artist)
            self.db.commit()
            self.db.refresh(artist)
            return artist
        except IntegrityError as e:
            raise e

    def remove_song_from_artist(self, artist_id: str, song_id: str):
        try:
            artist = self.db.query(Artist).filter(Artist.id == artist_id).first()
            if not artist:
                raise ArtistNotFoundException(f"Artists with provided id: {artist_id} not found.", 400)
            song = self.db.query(Song).filter(Song.id == song_id).first()
            if not song:
                raise SongNotFoundException(f"Song with provided id: {song_id} not found.", 400)
            artist.songs.remove(song)
            self.db.add(artist)
            self.db.commit()
            self.db.refresh(artist)
            return artist
        except IntegrityError as e:
            raise e

    def remove_album_from_artist(self, artist_id: str, album_id: str):
        try:
            artist = self.db.query(Artist).filter(Artist.id == artist_id).first()
            if not artist:
                raise ArtistNotFoundException(f"Artists with provided id: {artist_id} not found.", 400)
            album = self.db.query(Album).filter(Album.id == album_id).first()
            if not album:
                raise AlbumNotFoundException(f"Album with provided id: {album_id} not found.", 400)
            artist.albums.remove(album)
            self.db.add(artist)
            self.db.commit()
            self.db.refresh(artist)
            return artist
        except IntegrityError as e:
            raise e

    def remove_award_from_artist(self, artist_id: str, award_id: str):
        try:
            artist = self.db.query(Artist).filter(Artist.id == artist_id).first()
            if not artist:
                raise ArtistNotFoundException(f"Artists with provided id: {artist_id} not found.", 400)
            award = self.db.query(Award).filter(Award.id == award_id).first()
            if not award:
                raise AwardNotFoundException(f"Award with provided id: {award_id} not found.", 400)
            artist.awards.remove(award)
            self.db.add(artist)
            self.db.commit()
            self.db.refresh(artist)
            return artist
        except IntegrityError as e:
            raise e

    def remove_genre_from_artist(self, artist_id: str, genre_name: str):
        try:
            artist = self.db.query(Artist).filter(Artist.id == artist_id).first()
            if not artist:
                raise ArtistNotFoundException(f"Artists with provided id: {artist_id} not found.", 400)
            genre = self.db.query(Genre).filter(Genre.name == genre_name).first()
            if not genre:
                raise GenreNotFoundException(f"Genre with provided name: {genre_name} not found.", 400)
            artist.genres.remove(genre)
            self.db.add(artist)
            self.db.commit()
            self.db.refresh(artist)
            return artist
        except IntegrityError as e:
            raise e

    def remove_comment_from_artist(self, artist_id: str, comment_id: str):
        try:
            artist = self.db.query(Artist).filter(Artist.id == artist_id).first()
            if not artist:
                raise ArtistNotFoundException(f"Artists with provided id: {artist_id} not found.", 400)
            comment = self.db.query(Comment).filter(Comment.id == comment_id).first()
            if not comment:
                raise CommentNotFoundException(f"Comment with provided id: {comment_id} not found.", 400)
            artist.comments.remove(comment)
            self.db.add(artist)
            self.db.commit()
            self.db.refresh(artist)
            return artist
        except IntegrityError as e:
            raise e
