from fastapi import HTTPException, Response, status

from app.group.exceptions import *
from app.group.services import GroupServices


class GroupController:
    @staticmethod
    def create_group(name: str, country_name: str, date_of_forming: str):
        try:
            artist = GroupServices.create_group(name, country_name, date_of_forming)
            return artist
        except GroupNotFoundException as _e:
            raise HTTPException(status_code=_e.code, detail=_e.message)
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))

    @staticmethod
    def calculate_average_rating_for_group(id: str):
        try:
            rating = GroupServices.calculate_average_rating_for_group(id)
            return rating
        except GroupNotFoundException as _e:
            raise HTTPException(status_code=_e.code, detail=_e.message)
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))

    @staticmethod
    def get_group_by_id(id: str):
        try:
            group = GroupServices.get_group_by_id(id)
            if group:
                return group
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Group with provided id: "
                                                                                f"{id}, does not exist.")
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))

    @staticmethod
    def get_groups_by_characters(characters: str):
        groups = GroupServices.get_groups_by_characters(characters)
        return groups

    @staticmethod
    def get_all_groups():
        groups = GroupServices.get_all_groups()
        return groups

    @staticmethod
    def get_groups_by_rating():
        groups = GroupServices.get_groups_by_rating()
        return groups

    @staticmethod
    def get_groups_from_country(country: str):
        groups = GroupServices.get_groups_from_country(country)
        return groups

    @staticmethod
    def get_group_with_most_awards():
        try:
            group = GroupServices.get_group_with_most_awards()
            if group:
                return group
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="There is no group in database.")
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))

    @staticmethod
    def get_groups_by_genre(genre: str):
        groups = GroupServices.get_groups_by_genre(genre)
        return groups

    @staticmethod
    def get_all_comments_about_group(id: str):
        try:
            comments = GroupServices.get_all_comments_about_group(id)
            if comments:
                return comments
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Group with provided id: "
                                                                                f"{id}, does not exist.")
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))

    @staticmethod
    def delete_group_by_id(id: str):
        try:
            GroupServices.delete_group_by_id(id)
            return Response(content=f"Group with provided id: {id} is deleted.")
        except GroupNotFoundException as _e:
            raise HTTPException(status_code=_e.code, detail=_e.message)
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))

    @staticmethod
    def update_group(id: str, name=None, date_of_forming=None, date_of_disband=None, vocalist=None,
                     musician=None, producer=None, writer=None, engineer=None, biography=None, ratings=None,
                     country_name=None, record_label_id=None):
        try:
            group = GroupServices.update_group(id, name, date_of_forming, date_of_disband, vocalist,
                                               musician, producer, writer, engineer, biography, ratings,
                                               country_name, record_label_id)
            return group
        except GroupNotFoundException as _e:
            raise HTTPException(status_code=_e.code, detail=_e.message)
        except Exception as _e:
            raise _e

    @staticmethod
    def add_song_to_group(group_id: str, song_id: str):
        try:
            group = GroupServices.add_song_to_group(group_id, song_id)
            if group:
                return group
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Group with provided id: "
                                                                                f"{group_id}, does not exist.")
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))

    @staticmethod
    def add_album_to_group(group_id: str, album_id: str):
        try:
            group = GroupServices.add_album_to_group(group_id, album_id)
            if group:
                return group
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Group with provided id: "
                                                                                f"{group_id}, does not exist.")
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))

    @staticmethod
    def add_award_to_group(group_id: str, award_id: str):
        try:
            group = GroupServices.add_award_to_group(group_id, award_id)
            if group:
                return group
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Group with provided id: "
                                                                                f"{group_id}, does not exist.")
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))

    @staticmethod
    def add_genre_to_group(group_id: str, genre_name: str):
        try:
            group = GroupServices.add_genre_to_group(group_id, genre_name)
            if group:
                return group
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Group with provided id: "
                                                                                f"{group_id}, does not exist.")
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))

    @staticmethod
    def add_comment_to_group(group_id: str, comment_id: str):
        try:
            group = GroupServices.add_comment_to_group(group_id, comment_id)
            if group:
                return group
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Group with provided id: "
                                                                                f"{group_id}, does not exist.")
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))

    @staticmethod
    def remove_song_from_group(group_id: str, song_id: str):
        try:
            group = GroupServices.remove_song_from_group(group_id, song_id)
            if group:
                return group
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Group with provided id: "
                                                                                f"{group_id}, does not exist.")
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))

    @staticmethod
    def remove_album_from_group(group_id: str, album_id: str):
        try:
            group = GroupServices.remove_album_from_group(group_id, album_id)
            if group:
                return group
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Group with provided id: "
                                                                                f"{group_id}, does not exist.")
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))

    @staticmethod
    def remove_award_from_group(group_id: str, award_id: str):
        try:
            group = GroupServices.remove_award_from_group(group_id, award_id)
            if group:
                return group
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Group with provided id: "
                                                                                f"{group_id}, does not exist.")
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))

    @staticmethod
    def remove_genre_from_group(group_id: str, genre_name: str):
        try:
            group = GroupServices.remove_genre_from_group(group_id, genre_name)
            if group:
                return group
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Group with provided id: "
                                                                                f"{group_id}, does not exist.")
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))

    @staticmethod
    def remove_comment_from_group(group_id: str, comment_id: str):
        try:
            group = GroupServices.remove_comment_from_group(group_id, comment_id)
            if group:
                return group
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Group with provided id: "
                                                                                f"{group_id}, does not exist.")
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))
