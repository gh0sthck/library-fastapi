from fastapi import FastAPI

from .books.routers import book_router
from .catalogs.routers import catalog_router


def register_routers(app: FastAPI):
    app.include_router(book_router)
    app.include_router(catalog_router)


__all__ = ["register_routers"]
