from sqlalchemy import desc
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.album import Album
from app.album.exceptions import AlbumNotFoundException
from app.artist import Artist
from app.artist.exceptions import ArtistNotFoundException
from app.award import Award
from app.award.exceptions import AwardNotFoundException
from app.comment import Comment
from app.comment.exceptions import CommentNotFoundException
from app.genre.exceptions import GenreNotFoundException
from app.genre.model import Genre
from app.song.exceptions import SongNotFoundException
from app.song.model import Song
from app.user.model.user_ratings import UserRating


class SongRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_song(self, name: str, length: int, date_of_release: str):
        try:
            song = Song(name, length, date_of_release)
            self.db.add(song)
            self.db.commit()
            self.db.refresh(song)
            return song
        except IntegrityError as e:
            raise e

    def calculate_average_rating_for_song(self, song_id: str):
        ratings = self.db.query(UserRating).filter_by(song_id=song_id).all()
        if not ratings:
            return 0.0
        total_rating = sum(rating.rating for rating in ratings)
        total_num_ratings = len(ratings)
        return total_rating / total_num_ratings

    def get_song_by_id(self, id: str):
        song = self.db.query(Song).filter(Song.id == id).first()
        if song is None:
            raise SongNotFoundException(f"Song with provided id: {id} not found.", 400)
        return song

    def get_songs_by_characters(self, characters: str):
        songs = self.db.query(Song).filter(Song.name.like(characters + "%")).all()
        if songs is None:
            raise SongNotFoundException(f"Song with provided characters: {characters} not found.", 400)
        return songs

    def get_all_songs(self):
        songs = self.db.query(Song).all()
        return songs

    def get_songs_by_rating(self):
        songs = self.db.query(Song).order_by(desc(Song.ratings)).all()
        if songs is None:
            raise SongNotFoundException("Songs not found.", 400)
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

    def update_song(self, id: str, name=None, length=None, date_of_release=None, items_sold=None, lyrics=None,
                    ratings=None, explicit=None):
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
            if explicit is None:
                song.explicit = False
            else:
                song.explicit = True
            self.db.add(song)
            self.db.commit()
            self.db.refresh(song)
            return song
        except Exception as e:
            raise e

    def add_artist_to_song(self, song_id: str, artist_id: str):
        try:
            song = self.db.query(Song).filter(Song.id == song_id).first()
            if not song:
                raise SongNotFoundException(f"Song with provided id: {song_id} not found.", 400)
            artist = self.db.query(Artist).filter(Artist.id == artist_id).first()
            if not artist:
                raise ArtistNotFoundException(f"Artists with provided id: {artist_id} not found.", 400)
            song.artists.append(artist)
            self.db.add(song)
            self.db.commit()
            self.db.refresh(song)
            return song
        except IntegrityError as e:
            raise e

    def add_album_to_song(self, song_id: str, album_id: str):
        try:
            song = self.db.query(Song).filter(Song.id == song_id).first()
            if not song:
                raise SongNotFoundException(f"Song with provided id: {song_id} not found.", 400)
            album = self.db.query(Album).filter(Album.id == album_id).first()
            if not album:
                raise AlbumNotFoundException(f"Album with provided id: {album_id} not found.", 400)
            song.artists.append(album)
            self.db.add(song)
            self.db.commit()
            self.db.refresh(song)
            return song
        except IntegrityError as e:
            raise e

    def add_award_to_song(self, song_id: str, award_id: str):
        try:
            song = self.db.query(Song).filter(Song.id == song_id).first()
            if not song:
                raise SongNotFoundException(f"Song with provided id: {song_id} not found.", 400)
            award = self.db.query(Award).filter(Award.id == award_id).first()
            if not award:
                raise AwardNotFoundException(f"Award with provided id: {award_id} not found.", 400)
            song.awards.append(award)
            self.db.add(song)
            self.db.commit()
            self.db.refresh(song)
            return song
        except IntegrityError as e:
            raise e

    def add_genre_to_song(self, song_id: str, genre_name: str):
        try:
            song = self.db.query(Song).filter(Song.id == song_id).first()
            if not song:
                raise SongNotFoundException(f"Song with provided id: {song_id} not found.", 400)
            genre = self.db.query(Genre).filter(Genre.name == genre_name).first()
            if not genre:
                raise GenreNotFoundException(f"Genre with provided name: {genre_name} not found.", 400)
            song.genres.append(genre)
            self.db.add(song)
            self.db.commit()
            self.db.refresh(song)
            return song
        except IntegrityError as e:
            raise e

    def add_comment_to_song(self, song_id: str, comment_id: str):
        try:
            song = self.db.query(Song).filter(Song.id == song_id).first()
            if not song:
                raise SongNotFoundException(f"Song with provided id: {song_id} not found.", 400)
            comment = self.db.query(Comment).filter(Comment.id == comment_id).first()
            if not comment:
                raise CommentNotFoundException(f"Comment with provided id: {comment_id} not found.", 400)
            song.comments.append(comment)
            self.db.add(song)
            self.db.commit()
            self.db.refresh(song)
            return song
        except IntegrityError as e:
            raise e

    def remove_artist_from_song(self, song_id: str, artist_id: str):
        try:
            song = self.db.query(Song).filter(Song.id == song_id).first()
            if not song:
                raise SongNotFoundException(f"Song with provided id: {song_id} not found.", 400)
            artist = self.db.query(Artist).filter(Artist.id == artist_id).first()
            if not artist:
                raise ArtistNotFoundException(f"Artists with provided id: {artist_id} not found.", 400)
            song.artists.remove(artist)
            self.db.add(song)
            self.db.commit()
            self.db.refresh(song)
            return song
        except IntegrityError as e:
            raise e

    def remove_album_from_song(self, song_id: str, album_id: str):
        try:
            song = self.db.query(Song).filter(Song.id == song_id).first()
            if not song:
                raise SongNotFoundException(f"Song with provided id: {song_id} not found.", 400)
            album = self.db.query(Album).filter(Album.id == album_id).first()
            if not album:
                raise AlbumNotFoundException(f"Album with provided id: {album_id} not found.", 400)
            song.artists.remove(album)
            self.db.add(song)
            self.db.commit()
            self.db.refresh(song)
            return song
        except IntegrityError as e:
            raise e

    def remove_award_from_song(self, song_id: str, award_id: str):
        try:
            song = self.db.query(Song).filter(Song.id == song_id).first()
            if not song:
                raise SongNotFoundException(f"Song with provided id: {song_id} not found.", 400)
            award = self.db.query(Award).filter(Award.id == award_id).first()
            if not award:
                raise AwardNotFoundException(f"Award with provided id: {award_id} not found.", 400)
            song.awards.remove(award)
            self.db.add(song)
            self.db.commit()
            self.db.refresh(song)
            return song
        except IntegrityError as e:
            raise e

    def remove_genre_from_song(self, song_id: str, genre_name: str):
        try:
            song = self.db.query(Song).filter(Song.id == song_id).first()
            if not song:
                raise SongNotFoundException(f"Song with provided id: {song_id} not found.", 400)
            genre = self.db.query(Genre).filter(Genre.name == genre_name).first()
            if not genre:
                raise GenreNotFoundException(f"Genre with provided name: {genre_name} not found.", 400)
            song.genres.remove(genre)
            self.db.add(song)
            self.db.commit()
            self.db.refresh(song)
            return song
        except IntegrityError as e:
            raise e

    def remove_comment_from_song(self, song_id: str, comment_id: str):
        try:
            song = self.db.query(Song).filter(Song.id == song_id).first()
            if not song:
                raise SongNotFoundException(f"Song with provided id: {song_id} not found.", 400)
            comment = self.db.query(Comment).filter(Comment.id == comment_id).first()
            if not comment:
                raise CommentNotFoundException(f"Comment with provided id: {comment_id} not found.", 400)
            song.comments.remove(comment)
            self.db.add(song)
            self.db.commit()
            self.db.refresh(song)
            return song
        except IntegrityError as e:
            raise e
