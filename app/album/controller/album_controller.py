from fastapi import HTTPException, Response, status

from app.album import Album
from app.album.exceptions import *
from app.album.services import AlbumServices


class AlbumController:
    @staticmethod
    def create_album(name: str, length: int, date_of_release: str) -> Album:
        try:
            album = AlbumServices.create_album(name, length, date_of_release)
            return album
        except AlbumAlreadyExistsException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def calculate_average_rating_for_album(album_id: str) -> float:
        try:
            rating = AlbumServices.calculate_average_rating_for_album(album_id)
            return rating
        except AlbumNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_album_by_id(album_id: str) -> Album:
        try:
            album = AlbumServices.get_album_by_id(album_id)
            if album:
                return album
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Album with provided id: "
                                                                                f"{album_id}, does not exist.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_albums_by_characters(characters: str) -> list:
        albums = AlbumServices.get_albums_by_characters(characters)
        return albums

    @staticmethod
    def get_all_albums() -> list:
        albums = AlbumServices.get_all_albums()
        return albums

    @staticmethod
    def get_albums_by_rating() -> list:
        albums = AlbumServices.get_albums_by_rating()
        return albums

    @staticmethod
    def get_best_albums_from_year(year: str) -> list:
        albums = AlbumServices.get_best_albums_from_year(year)
        return albums

    @staticmethod
    def get_album_with_most_awards() -> Album:
        try:
            album = AlbumServices.get_album_with_most_awards()
            if album:
                return album
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="There is no album in database.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_albums_by_genre(genre_name: str) -> list:
        albums = AlbumServices.get_albums_by_genre(genre_name)
        return albums

    @staticmethod
    def get_all_comments_about_album(album_id: str) -> list:
        try:
            comments = AlbumServices.get_all_comments_about_album(album_id)
            if comments:
                return comments
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Album with provided id: "
                                                                                f"{album_id}, does not exist.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def delete_album_by_id(album_id: str):
        try:
            AlbumServices.delete_album_by_id(album_id)
            return Response(content=f"Album with provided id: {album_id} is deleted.")
        except AlbumNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def update_album(album_id: str, name=None, length=None, date_of_release=None, items_sold=None, ratings=None,
                     explicit=None, lp=None, ep=None, single=None, mixtape=None) -> Album:
        try:
            album = AlbumServices.update_album(album_id, name, length, date_of_release, items_sold, ratings, explicit,
                                               lp, ep, single, mixtape)
            return album
        except AlbumNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def add_artist_to_album(album_id: str, artist_id: str) -> Album:
        try:
            album = AlbumServices.add_artist_to_album(album_id, artist_id)
            if album:
                return album
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Album with provided id: "
                                                                                f"{album_id}, does not exist.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def add_group_to_album(album_id: str, group_id: str) -> Album:
        try:
            album = AlbumServices.add_group_to_album(album_id, group_id)
            if album:
                return album
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Album with provided id: "
                                                                                f"{album_id}, does not exist.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def add_song_to_album(album_id: str, song_id: str) -> Album:
        try:
            album = AlbumServices.add_song_to_album(album_id, song_id)
            if album:
                return album
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Album with provided id: "
                                                                                f"{album_id}, does not exist.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def add_award_to_album(album_id: str, award_id: str) -> Album:
        try:
            album = AlbumServices.add_award_to_album(album_id, award_id)
            if album:
                return album
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Album with provided id: "
                                                                                f"{album_id}, does not exist.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def add_genre_to_album(album_id: str, genre_name: str) -> Album:
        try:
            album = AlbumServices.add_genre_to_album(album_id, genre_name)
            if album:
                return album
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Album with provided id: "
                                                                                f"{album_id}, does not exist.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def add_comment_to_album(album_id: str, comment_id: str) -> Album:
        try:
            album = AlbumServices.add_comment_to_album(album_id, comment_id)
            if album:
                return album
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Album with provided id: "
                                                                                f"{album_id}, does not exist.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def remove_artist_from_album(album_id: str, artist_id: str) -> Album:
        try:
            album = AlbumServices.remove_group_from_album(album_id, artist_id)
            if album:
                return album
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Album with provided id: "
                                                                                f"{album_id}, does not exist.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def remove_group_from_album(album_id: str, group_id: str) -> Album:
        try:
            album = AlbumServices.remove_group_from_album(album_id, group_id)
            if album:
                return album
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Album with provided id: "
                                                                                f"{album_id}, does not exist.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def remove_song_from_album(album_id: str, song_id: str) -> Album:
        try:
            album = AlbumServices.remove_song_from_album(album_id, song_id)
            if album:
                return album
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Album with provided id: "
                                                                                f"{album_id}, does not exist.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def remove_award_from_album(album_id: str, award_id: str) -> Album:
        try:
            album = AlbumServices.remove_award_from_album(album_id, award_id)
            if album:
                return album
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Album with provided id: "
                                                                                f"{album_id}, does not exist.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def remove_genre_from_album(album_id: str, genre_name: str) -> Album:
        try:
            album = AlbumServices.remove_genre_from_album(album_id, genre_name)
            if album:
                return album
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Album with provided id: "
                                                                                f"{album_id}, does not exist.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def remove_comment_from_album(album_id: str, comment_id: str) -> Album:
        try:
            album = AlbumServices.remove_comment_from_album(album_id, comment_id)
            if album:
                return album
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Album with provided id: "
                                                                                f"{album_id}, does not exist.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e
