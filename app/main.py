import uvicorn
from fastapi import FastAPI
from starlette.responses import RedirectResponse

from app.db.database import Base, engine

from app.album.routes import album_router
from app.artist.routes import artist_router
from app.award.routes import award_router
from app.country.routes import country_router
from app.comment.routes import comment_router
from app.genre.routes import genre_router
from app.group.routes import group_router
from app.record_label.routes import record_label_router
from app.song.routes import song_router
from app.user.routes import user_router

Base.metadata.create_all(bind=engine)


def init_app():
    _app = FastAPI()

    _app.include_router(user_router)
    _app.include_router(album_router)
    _app.include_router(artist_router)
    _app.include_router(group_router)
    _app.include_router(song_router)
    _app.include_router(comment_router)
    _app.include_router(award_router)
    _app.include_router(country_router)
    _app.include_router(genre_router)
    _app.include_router(record_label_router)

    return _app


app = init_app()


@app.get("/", include_in_schema=False)
def open_music_db():
    return RedirectResponse("/docs")


if __name__ == "__main__":
    uvicorn.run(app)
