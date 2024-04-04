from fastapi import FastAPI
from .books.routers import book_router


def register_routers(app: FastAPI):
    app.include_router(book_router)


__all__ = ["register_routers"]
