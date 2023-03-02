from sqlalchemy import desc, text, and_
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
from app.group import Group
from app.group.exceptions import GroupNotFoundException
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
        return songs

    def get_all_songs(self):
        songs = self.db.query(Song).all()
        return songs

    def get_songs_by_rating(self):
        songs = self.db.query(Song).order_by(desc(Song.ratings)).all()
        return songs

    def get_best_songs_from_year(self, year: str):
        songs = self.db.query(Song).filter(and_(Song.date_of_release.like(f"{year}%"))).\
            order_by(desc(Song.ratings)).all()
        return songs

    def get_song_with_most_awards(self):
        songs = self.db.query(Song).all()
        if len(songs) == 0:
            raise SongNotFoundException("There is no song in database.", 500)
        song_max_awards = songs[0]
        for song in songs:
            if len(song.awards) > len(song_max_awards.awards) > 0 or len(song.awards) > 0:
                song_max_awards = song
            else:
                raise SongNotFoundException(f"There is no song with awards.", 500)
        return song_max_awards

    def get_songs_by_genre(self, genre: str):
        filter_expression = text(f"genre.name = '{genre}'")
        songs = self.db.query(Song).filter(Song.genres.any(filter_expression)).all()
        return songs

    def get_all_comments_about_song(self, id: str):
        song = self.db.query(Song).filter(Song.id == id).first()
        if song is None:
            raise SongNotFoundException(f"Song with provided id: {id} not found.", 400)
        return song.comments

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

    def add_group_to_song(self, song_id: str, group_id: str):
        try:
            song = self.db.query(Song).filter(Song.id == song_id).first()
            if not song:
                raise SongNotFoundException(f"Song with provided id: {song_id} not found.", 400)
            group = self.db.query(Group).filter(Group.id == group_id).first()
            if not group:
                raise GroupNotFoundException(f"Group with provided id: {group_id} not found.", 400)
            song.groups.append(group)
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

    def remove_group_from_song(self, song_id: str, group_id: str):
        try:
            song = self.db.query(Song).filter(Song.id == song_id).first()
            if not song:
                raise SongNotFoundException(f"Song with provided id: {song_id} not found.", 400)
            group = self.db.query(Group).filter(Group.id == group_id).first()
            if not group:
                raise GroupNotFoundException(f"Group with provided id: {group_id} not found.", 400)
            song.artists.remove(group)
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
