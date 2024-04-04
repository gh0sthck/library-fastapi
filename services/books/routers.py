from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from .schemas import Book, Author, BookCreate
from .books import create_book as create_book_func


book_router = APIRouter(prefix="/books", tags=["Books"])


@book_router.get("/all/")
async def get_all_books() -> dict[str, int]:
    """Return all books at library."""
    return {"test": 200}


@book_router.get("/{author_id}/")
async def get_author_books() -> dict[str, int]:
    """Return all books of specific author."""
    return {"test": 200}
    

@book_router.get("/{book_id}/")
async def get_id_book(book_id: int) -> dict[str, int]:
    """Return specific book by book id."""
    return {"test": 200}


@book_router.get("/{catalog_id}/")
async def get_catalog_books(catalog_id: int) -> dict[str, int]:
    """Return all books by catalog id."""
    return {"test": 200}


@book_router.post("/create/")
async def create_book(
    book: Annotated[BookCreate, Depends()],
    async_session: AsyncSession = Depends(get_async_session), 
    ) -> BookCreate:
    return await create_book_func(book=book, session=async_session)
