from sqlalchemy import desc, text, and_
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.album.exceptions import AlbumNotFoundException
from app.album.model import Album
from app.artist import Artist
from app.artist.exceptions import ArtistNotFoundException
from app.award import Award
from app.award.exceptions import AwardNotFoundException
from app.comment import Comment
from app.comment.exceptions import CommentNotFoundException
from app.genre.exceptions import GenreNotFoundException
from app.genre.model import Genre
from app.song import Song
from app.song.exceptions import SongNotFoundException
from app.user.model.user_ratings import UserRating


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

    def calculate_average_rating_for_album(self, album_id: str):
        ratings = self.db.query(UserRating).filter_by(album_id=album_id).all()
        if not ratings:
            return 0.0
        total_rating = sum(rating.rating for rating in ratings)
        total_num_ratings = len(ratings)
        return total_rating / total_num_ratings

    def get_album_by_id(self, id: str):
        album = self.db.query(Album).filter(Album.id == id).first()
        if album is None:
            raise AlbumNotFoundException(f"Album with provided id: {id} not found.", 400)
        return album

    def get_albums_by_characters(self, characters: str):
        albums = self.db.query(Album).filter(Album.name.like(characters + "%")).all()
        return albums

    def get_all_albums(self):
        albums = self.db.query(Album).all()
        return albums

    def get_albums_by_rating(self):
        albums = self.db.query(Album).order_by(desc(Album.ratings)).all()
        return albums

    def get_best_albums_from_year(self, year: str):
        albums = self.db.query(Album).filter(and_(Album.date_of_release.like(f"{year}%"))).\
            order_by(desc(Album.ratings)).all()
        return albums

    def get_album_with_most_awards(self):
        albums = self.db.query(Album).all()
        if len(albums) == 0:
            raise AlbumNotFoundException("There is no album in database.", 500)
        album_max_awards = albums[0]
        for album in albums:
            if len(album.awards) > len(album_max_awards.awards) > 0 or len(album.awards) > 0:
                album_max_awards = album
            else:
                raise AlbumNotFoundException(f"There is no album with awards.", 500)
        return album_max_awards

    def get_albums_by_genre(self, genre: str):
        filter_expression = text(f"genre.name = '{genre}'")
        albums = self.db.query(Album).filter(Album.genres.any(filter_expression)).all()
        return albums

    def get_all_comments_about_album(self, id: str):
        album = self.db.query(Album).filter(Album.id == id).first()
        if album is None:
            raise AlbumNotFoundException(f"Album with provided id: {id} not found.", 400)
        return album.comments

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
                     explicit=None, lp=None, ep=None, single=None, mixtape=None):
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
            album.songs.append(song)
            self.db.add(album)
            self.db.commit()
            self.db.refresh(album)
            return album
        except IntegrityError as e:
            raise e

    def add_award_to_album(self, album_id: str, award_id: str):
        try:
            album = self.db.query(Album).filter(Album.id == album_id).first()
            if not album:
                raise AlbumNotFoundException(f"Album with provided id: {album_id} not found.", 400)
            award = self.db.query(Award).filter(Award.id == award_id).first()
            if not award:
                raise AwardNotFoundException(f"Award with provided id: {award_id} not found.", 400)

            album.awards.append(award)
            self.db.add(album)
            self.db.commit()
            self.db.refresh(album)
            return album
        except IntegrityError as e:
            raise e

    def add_genre_to_album(self, album_id: str, genre_name: str):
        try:
            album = self.db.query(Album).filter(Album.id == album_id).first()
            if not album:
                raise AlbumNotFoundException(f"Album with provided id: {album_id} not found.", 400)
            genre = self.db.query(Genre).filter(Genre.name == genre_name).first()
            if not genre:
                raise GenreNotFoundException(f"Genre with provided name: {genre_name} not found.", 400)
            album.genres.append(genre)
            self.db.add(album)
            self.db.commit()
            self.db.refresh(album)
            return album
        except IntegrityError as e:
            raise e

    def add_comment_to_album(self, album_id: str, comment_id: str):
        try:
            album = self.db.query(Album).filter(Album.id == album_id).first()
            if not album:
                raise AlbumNotFoundException(f"Album with provided id: {album_id} not found.", 400)
            comment = self.db.query(Comment).filter(Comment.id == comment_id).first()
            if not comment:
                raise CommentNotFoundException(f"Comment with provided id: {comment_id} not found.", 400)
            album.comments.append(comment)
            self.db.add(album)
            self.db.commit()
            self.db.refresh(album)
            return album
        except IntegrityError as e:
            raise e

    def remove_artist_from_album(self, album_id: str, artist_id: str):
        try:
            album = self.db.query(Album).filter(Album.id == album_id).first()
            if not album:
                raise AlbumNotFoundException(f"Album with provided id: {album_id} not found.", 400)
            artist = self.db.query(Artist).filter(Artist.id == artist_id).first()
            if not artist:
                raise ArtistNotFoundException(f"Artist with provided id: {artist_id} not found.", 400)
            album.artists.remove(artist)
            self.db.add(album)
            self.db.commit()
            self.db.refresh(album)
            return album
        except IntegrityError as e:
            raise e

    def remove_song_from_album(self, album_id: str, song_id: str):
        try:
            album = self.db.query(Album).filter(Album.id == album_id).first()
            if not album:
                raise AlbumNotFoundException(f"Album with provided id: {album_id} not found.", 400)
            song = self.db.query(Song).filter(Song.id == song_id).first()
            if not song:
                raise SongNotFoundException(f"Song with provided id: {song_id} not found.", 400)
            album.songs.remove(song)
            self.db.add(album)
            self.db.commit()
            self.db.refresh(album)
            return album
        except IntegrityError as e:
            raise e

    def remove_award_from_album(self, album_id: str, award_id: str):
        try:
            album = self.db.query(Album).filter(Album.id == album_id).first()
            if not album:
                raise AlbumNotFoundException(f"Album with provided id: {album_id} not found.", 400)
            award = self.db.query(Award).filter(Award.id == award_id).first()
            if not award:
                raise AwardNotFoundException(f"Award with provided id: {award_id} not found.", 400)
            album.awards.remove(award)
            self.db.add(album)
            self.db.commit()
            self.db.refresh(album)
            return album
        except IntegrityError as e:
            raise e

    def remove_genre_from_album(self, album_id: str, genre_name: str):
        try:
            album = self.db.query(Album).filter(Album.id == album_id).first()
            if not album:
                raise AlbumNotFoundException(f"Album with provided id: {album_id} not found.", 400)
            genre = self.db.query(Genre).filter(Genre.name == genre_name).first()
            if not genre:
                raise GenreNotFoundException(f"Genre with provided name: {genre_name} not found.", 400)
            album.genres.remove(genre)
            self.db.add(album)
            self.db.commit()
            self.db.refresh(album)
            return album
        except IntegrityError as e:
            raise e

    def remove_comment_from_album(self, album_id: str, comment_id: str):
        try:
            album = self.db.query(Album).filter(Album.id == album_id).first()
            if not album:
                raise AlbumNotFoundException(f"Album with provided id: {album_id} not found.", 400)
            comment = self.db.query(Comment).filter(Comment.id == comment_id).first()
            if not comment:
                raise CommentNotFoundException(f"Comment with provided id: {comment_id} not found.", 400)
            album.comments.remove(comment)
            self.db.add(album)
            self.db.commit()
            self.db.refresh(album)
            return album
        except IntegrityError as e:
            raise e
