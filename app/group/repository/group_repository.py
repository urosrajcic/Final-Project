from sqlalchemy import desc, text, and_
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.album import Album
from app.album.exceptions import AlbumNotFoundException
from app.group.exceptions import *
from app.artist.model import Artist
from app.award import Award
from app.award.exceptions import AwardNotFoundException
from app.comment import Comment
from app.comment.exceptions import CommentNotFoundException
from app.genre.exceptions import GenreNotFoundException
from app.genre.model import Genre
from app.group import Group
from app.song import Song
from app.song.exceptions import SongNotFoundException
from app.user.model.user_ratings import UserRating


class GroupRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_group(self, name: str, country_name: str, date_of_forming: str):
        try:
            group = Group(name, country_name, date_of_forming)
            self.db.add(group)
            self.db.commit()
            self.db.refresh(group)
            return group
        except IntegrityError as e:
            raise e

    def calculate_average_rating_for_group(self, group_id: str):
        ratings = self.db.query(UserRating).filter_by(group_id=group_id).all()
        if not ratings:
            return 0.0
        total_rating = sum(rating.rating for rating in ratings)
        total_num_ratings = len(ratings)
        return total_rating / total_num_ratings

    def get_group_by_id(self, id: str):
        group = self.db.query(Group).filter(Group.id == id).first()
        if group is None:
            raise GroupNotFoundException(f"Group with provided id: {id} not found.", 400)
        return group

    def get_groups_by_characters(self, characters: str):
        groups = self.db.query(Group).filter(Group.name.like(characters + "%")).all()
        return groups

    def get_all_groups(self):
        groups = self.db.query(Group).all()
        return groups

    def get_groups_by_rating(self):
        groups = self.db.query(Group).order_by(desc(Group.ratings)).all()
        return groups

    def get_groups_from_country(self, country: str):
        groups = self.db.query(Group).filter(Group.country_name == country).order_by(desc(Group.ratings)).all()
        return groups

    def get_group_with_most_awards(self):
        groups = self.db.query(Group).all()
        if len(groups) == 0:
            raise GroupNotFoundException("There is no group in database.", 404)
        group_max_awards = groups[0]
        for group in groups:
            if len(group.awards) > len(group_max_awards.awards) > 0 or len(group.awards) > 0:
                group_max_awards = group
            else:
                raise GroupNotFoundException(f"There is no group with awards.", 404)
        return group_max_awards

    def get_groups_by_genre(self, genre: str):
        filter_expression = text(f"genre.name = '{genre}'")
        groups = self.db.query(Group).filter(Group.genres.any(filter_expression)).all()
        return groups

    def get_all_comments_about_group(self, id: str):
        groups = self.db.query(Group).filter(Group.id == id).first()
        if groups is None:
            raise GroupNotFoundException(f"Group with provided id: {id} not found.", 500)
        return groups.comments

    def delete_group_by_id(self, id: str):
        try:
            group = self.db.query(Group).filter(Group.id == id).first()
            if group is None:
                raise GroupNotFoundException(f"Group with provided id: {id} not found.", 500)
            self.db.delete(group)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def update_group(self, id: str, name=None, date_of_forming=None, date_of_disband=None, vocalist=None,
                     musician=None, producer=None, writer=None, engineer=None, biography=None, ratings=None,
                     country_name=None, record_label_id=None):
        try:
            group = self.db.query(Group).filter(Group.id == id).first()
            if group is None:
                raise GroupNotFoundException(f"Group with provided id: {id} not found.", 400)
            if name is not None:
                group.name = name
            if date_of_forming is not None:
                group.date_of_birth = date_of_forming
            if date_of_disband is not None:
                group.date_of_death = date_of_disband
            if vocalist is None:
                group.vocalist = False
            else:
                group.vocalist = True
            if musician is None:
                group.musician = False
            else:
                group.musician = True
            if producer is None:
                group.producer = False
            else:
                group.producer = True
            if writer is None:
                group.writer = False
            else:
                group.writer = True
            if engineer is None:
                group.engineer = False
            else:
                group.engineer = True
            if biography is not None:
                group.biography = biography
            if ratings is not None:
                group.ratings = ratings
            if country_name is not None:
                group.country_name = country_name
            if record_label_id is not None:
                group.record_label_id = record_label_id
            self.db.add(group)
            self.db.commit()
            self.db.refresh(group)
            return group
        except Exception as e:
            raise e

    def add_song_to_group(self, group_id: str, song_id: str):
        try:
            group = self.db.query(Group).filter(Group.id == group_id).first()
            if not group:
                raise GroupNotFoundException(f"Group with provided id: {group_id} not found.", 400)
            song = self.db.query(Song).filter(Song.id == song_id).first()
            if not song:
                raise SongNotFoundException(f"Song with provided id: {song_id} not found.", 400)
            group.songs.append(song)
            self.db.add(group)
            self.db.commit()
            self.db.refresh(group)
            return group
        except IntegrityError as e:
            raise e

    def add_album_to_group(self, group_id: str, album_id: str):
        try:
            group = self.db.query(Group).filter(Group.id == group_id).first()
            if not group:
                raise GroupNotFoundException(f"Group with provided id: {group_id} not found.", 400)
            album = self.db.query(Album).filter(Album.id == album_id).first()
            if not album:
                raise AlbumNotFoundException(f"Album with provided id: {album_id} not found.", 400)
            group.albums.append(album)
            self.db.add(group)
            self.db.commit()
            self.db.refresh(group)
            return group
        except IntegrityError as e:
            raise e

    def add_award_to_group(self, group_id: str, award_id: str):
        try:
            group = self.db.query(Group).filter(Group.id == group_id).first()
            if not group:
                raise GroupNotFoundException(f"Group with provided id: {group_id} not found.", 400)
            award = self.db.query(Award).filter(Award.id == award_id).first()
            if not award:
                raise AwardNotFoundException(f"Award with provided id: {award_id} not found.", 400)
            group.awards.append(award)
            self.db.add(group)
            self.db.commit()
            self.db.refresh(group)
            return group
        except IntegrityError as e:
            raise e

    def add_genre_to_group(self, group_id: str, genre_name: str):
        try:
            group = self.db.query(Group).filter(Group.id == group_id).first()
            if not group:
                raise GroupNotFoundException(f"Group with provided id: {group_id} not found.", 400)
            genre = self.db.query(Genre).filter(Genre.name == genre_name).first()
            if not genre:
                raise GenreNotFoundException(f"Genre with provided name: {genre_name} not found.", 400)
            group.genres.append(genre)
            self.db.add(group)
            self.db.commit()
            self.db.refresh(group)
            return group
        except IntegrityError as e:
            raise e

    def add_comment_to_group(self, group_id: str, comment_id: str):
        try:
            group = self.db.query(Group).filter(Group.id == group_id).first()
            if not group:
                raise GroupNotFoundException(f"Group with provided id: {group_id} not found.", 400)
            comment = self.db.query(Comment).filter(Comment.id == comment_id).first()
            if not comment:
                raise CommentNotFoundException(f"Comment with provided id: {comment_id} not found.", 400)
            group.comments.append(comment)
            self.db.add(group)
            self.db.commit()
            self.db.refresh(group)
            return group
        except IntegrityError as e:
            raise e

    def remove_song_from_group(self, group_id: str, song_id: str):
        try:
            group = self.db.query(Group).filter(Group.id == group_id).first()
            if not group:
                raise GroupNotFoundException(f"Group with provided id: {group_id} not found.", 400)
            song = self.db.query(Song).filter(Song.id == song_id).first()
            if not song:
                raise SongNotFoundException(f"Song with provided id: {song_id} not found.", 400)
            group.songs.remove(song)
            self.db.add(group)
            self.db.commit()
            self.db.refresh(group)
            return group
        except IntegrityError as e:
            raise e

    def remove_album_from_group(self, group_id: str, album_id: str):
        try:
            group = self.db.query(Group).filter(Group.id == group_id).first()
            if not group:
                raise GroupNotFoundException(f"Group with provided id: {group_id} not found.", 400)
            album = self.db.query(Album).filter(Album.id == album_id).first()
            if not album:
                raise AlbumNotFoundException(f"Album with provided id: {album_id} not found.", 400)
            group.albums.remove(album)
            self.db.add(group)
            self.db.commit()
            self.db.refresh(group)
            return group
        except IntegrityError as e:
            raise e

    def remove_award_from_group(self, group_id: str, award_id: str):
        try:
            group = self.db.query(Group).filter(Group.id == group_id).first()
            if not group:
                raise GroupNotFoundException(f"Group with provided id: {group_id} not found.", 400)
            award = self.db.query(Award).filter(Award.id == award_id).first()
            if not award:
                raise AwardNotFoundException(f"Award with provided id: {award_id} not found.", 400)
            group.awards.remove(award)
            self.db.add(group)
            self.db.commit()
            self.db.refresh(group)
            return group
        except IntegrityError as e:
            raise e

    def remove_genre_from_group(self, group_id: str, genre_name: str):
        try:
            group = self.db.query(Group).filter(Group.id == group_id).first()
            if not group:
                raise GroupNotFoundException(f"Group with provided id: {group_id} not found.", 400)
            genre = self.db.query(Genre).filter(Genre.name == genre_name).first()
            if not genre:
                raise GenreNotFoundException(f"Genre with provided name: {genre_name} not found.", 400)
            group.genres.remove(genre)
            self.db.add(group)
            self.db.commit()
            self.db.refresh(group)
            return group
        except IntegrityError as e:
            raise e

    def remove_comment_from_group(self, group_id: str, comment_id: str):
        try:
            group = self.db.query(Group).filter(Group.id == group_id).first()
            if not group:
                raise GroupNotFoundException(f"Group with provided id: {group_id} not found.", 400)
            comment = self.db.query(Comment).filter(Comment.id == comment_id).first()
            if not comment:
                raise CommentNotFoundException(f"Comment with provided id: {comment_id} not found.", 400)
            group.comments.remove(comment)
            self.db.add(group)
            self.db.commit()
            self.db.refresh(group)
            return group
        except IntegrityError as e:
            raise e
