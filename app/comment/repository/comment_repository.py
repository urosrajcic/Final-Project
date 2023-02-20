import uuid
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.album import Album
from app.album.exceptions import AlbumNotFoundException
from app.artist import Artist
from app.artist.exceptions import ArtistNotFoundException
from app.comment.exceptions import CommentNotFoundException
from app.comment.model import Comment
from app.song import Song
from app.song.exceptions import SongNotFoundException


class CommentRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_comment_about_artist(self, header: str, text: str, user_username: str, artist_id: uuid):
        try:
            comment = Comment(header, text, user_username)
            self.db.add(comment)
            self.db.commit()
            self.db.refresh(comment)
            artist = self.db.query(Artist).filter(Artist.id is artist_id).first()
            if not artist:
                raise ArtistNotFoundException(f"Artist with provided id: {artist_id} not found.", 400)
            artist.comments.append(comment)
            self.db.add(artist)
            self.db.commit()
            self.db.refresh(artist)
            return artist
        except IntegrityError as e:
            raise e

    def create_comment_about_album(self, header: str, text: str, user_username: str, album_id: uuid):
        try:
            comment = Comment(header, text, user_username)
            album = self.db.query(Album).filter(Album.id is album_id).first()
            if not album:
                raise AlbumNotFoundException(f"Album with provided id: {album_id} not found.", 400)
            album.comments.append(comment)
            self.db.add(album)
            self.db.commit()
            self.db.refresh(album)
            return album
        except IntegrityError as e:
            raise e

    def create_comment_about_song(self, header: str, text: str, user_username: str, song_id: uuid):
        try:
            comment = Comment(header, text, user_username)
            song = self.db.query(Song).filter(Song.id is song_id).first()
            if not song:
                raise SongNotFoundException(f"Song with provided id: {song_id} not found.", 400)
            song.comments.append(comment)
            self.db.add(song)
            self.db.commit()
            self.db.refresh(song)
            return song
        except IntegrityError as e:
            raise e

    def get_comment_by_id(self, id: str):
        comment = self.db.query(Comment).filter(Comment.id == id).first()
        if comment is None:
            raise CommentNotFoundException(f"Comment with provided id: {id} not found.", 400)
        return comment

    def get_all_comments(self):
        comments = self.db.query(Comment).all()
        return comments

    def get_all_comments_from_user(self, user_username: str):
        comments = self.db.query(Comment).filter(Comment.user_username.like(user_username)).all()
        if comments is None:
            raise CommentNotFoundException(f"Comments with provided artist id: {user_username} not found.", 400)

    def delete_comment_by_id(self, id: str):
        try:
            comment = self.db.query(Comment).filter(Comment.id == id).first()
            if comment is None:
                raise CommentNotFoundException(f"Comment with provided id: {id} not found.", 400)
            self.db.delete(comment)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def update_comment(self, id: str, header=None, text=None):
        try:
            comment = self.db.query(Comment).filter(Comment.id == id).first()
            if comment is None:
                raise CommentNotFoundException(f"Comment with provided id: {id} not found.", 400)
            if header is not None:
                comment.header = header
            if text is not None:
                comment.text = text
            self.db.add(comment)
            self.db.commit()
            self.db.refresh(comment)
            return comment
        except Exception as e:
            raise e
