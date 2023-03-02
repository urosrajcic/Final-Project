from fastapi import HTTPException, Response, status
from app.song.exceptions import *
from app.song.services import SongServices


class SongController:
    @staticmethod
    def create_song(name: str, length: int, date_of_release: str):
        try:
            song = SongServices.create_song(name, length, date_of_release)
            return song
        except SongNotFoundException as _e:
            raise HTTPException(status_code=_e.code, detail=_e.message)
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))

    @staticmethod
    def calculate_average_rating_for_song(id: str):
        try:
            rating = SongServices.calculate_average_rating_for_song(id)
            return rating
        except SongNotFoundException as _e:
            raise HTTPException(status_code=_e.code, detail=_e.message)
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))

    @staticmethod
    def get_song_by_id(id: str):
        try:
            song = SongServices.get_song_by_id(id)
            if song:
                return song
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Song with provided id: "
                                                                                f"{id}, does not exist.")
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))

    @staticmethod
    def get_songs_by_characters(characters: str):
        songs = SongServices.get_songs_by_characters(characters)
        return songs

    @staticmethod
    def get_all_songs():
        songs = SongServices.get_all_songs()
        return songs

    @staticmethod
    def get_songs_by_rating():
        songs = SongServices.get_songs_by_rating()
        return songs

    @staticmethod
    def get_best_songs_from_year(year: str):
        songs = SongServices.get_best_songs_from_year(year)
        return songs

    @staticmethod
    def get_song_with_most_awards():
        try:
            song = SongServices.get_song_with_most_awards()
            if song:
                return song
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="There is no song in database.")
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))

    @staticmethod
    def get_songs_by_genre(genre: str):
        songs = SongServices.get_songs_by_genre(genre)
        return songs

    @staticmethod
    def get_all_comments_about_song(id: str):
        try:
            comments = SongServices.get_all_comments_about_song(id)
            if comments:
                return comments
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Song with provided id: "
                                                                                f"{id}, does not exist.")
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))

    @staticmethod
    def delete_song_by_id(id: str):
        try:
            SongServices.delete_song_by_id(id)
            return Response(content=f"Song with provided id: {id} is deleted.")
        except SongNotFoundException as _e:
            raise HTTPException(status_code=_e.code, detail=_e.message)
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))

    @staticmethod
    def update_song(id: str, name=None, length=None, date_of_release=None, items_sold=None, lyrics=None,
                    ratings=None, explicit=None):
        try:
            song = SongServices.update_song(id, name, length, date_of_release, items_sold, lyrics, ratings,
                                            explicit)
            return song
        except SongNotFoundException as _e:
            raise HTTPException(status_code=_e.code, detail=_e.message)
        except Exception as _e:
            raise _e

    @staticmethod
    def add_artist_to_song(song_id: str, artist_id: str):
        try:
            song = SongServices.add_group_to_song(song_id, artist_id)
            if song:
                return song
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Song with provided id: "
                                                                                f"{song_id}, does not exist.")
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))

    @staticmethod
    def add_group_to_song(song_id: str, group_id: str):
        try:
            song = SongServices.add_group_to_song(song_id, group_id)
            if song:
                return song
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Song with provided id: "
                                                                                f"{song_id}, does not exist.")
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))

    @staticmethod
    def add_album_to_song(song_id: str, album_id: str):
        try:
            song = SongServices.add_album_to_song(song_id, album_id)
            if song:
                return song
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Song with provided id: "
                                                                                f"{song_id}, does not exist.")
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))

    @staticmethod
    def add_award_to_song(song_id: str, award_id: str):
        try:
            song = SongServices.add_award_to_song(song_id, award_id)
            if song:
                return song
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Song with provided id: "
                                                                                f"{song_id}, does not exist.")
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))

    @staticmethod
    def add_genre_to_song(song_id: str, genre_name: str):
        try:
            song = SongServices.add_genre_to_song(song_id, genre_name)
            if song:
                return song
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Song with provided id: "
                                                                                f"{song_id}, does not exist.")
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))

    @staticmethod
    def add_comment_to_song(song_id: str, comment_id: str):
        try:
            song = SongServices.add_comment_to_song(song_id, comment_id)
            if song:
                return song
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Song with provided id: "
                                                                                f"{song_id}, does not exist.")
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))

    @staticmethod
    def remove_artist_from_song(song_id: str, artist_id: str):
        try:
            song = SongServices.remove_group_from_song(song_id, artist_id)
            if song:
                return song
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Song with provided id: "
                                                                                f"{song_id}, does not exist.")
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))

    @staticmethod
    def remove_group_from_song(song_id: str, group_id: str):
        try:
            song = SongServices.remove_group_from_song(song_id, group_id)
            if song:
                return song
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Song with provided id: "
                                                                                f"{song_id}, does not exist.")
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))

    @staticmethod
    def remove_album_from_song(song_id: str, album_id: str):
        try:
            song = SongServices.remove_album_from_song(song_id, album_id)
            if song:
                return song
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Song with provided id: "
                                                                                f"{song_id}, does not exist.")
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))

    @staticmethod
    def remove_award_from_song(song_id: str, award_id: str):
        try:
            song = SongServices.remove_award_from_song(song_id, award_id)
            if song:
                return song
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Song with provided id: "
                                                                                f"{song_id}, does not exist.")
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))

    @staticmethod
    def remove_genre_from_song(song_id: str, genre_name: str):
        try:
            song = SongServices.remove_genre_from_song(song_id, genre_name)
            if song:
                return song
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Song with provided id: "
                                                                                f"{song_id}, does not exist.")
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))

    @staticmethod
    def remove_comment_from_song(song_id: str, comment_id: str):
        try:
            song = SongServices.remove_comment_from_song(song_id, comment_id)
            if song:
                return song
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Song with provided id: "
                                                                                f"{song_id}, does not exist.")
        except Exception as _e:
            raise HTTPException(status_code=500, detail=str(_e))
