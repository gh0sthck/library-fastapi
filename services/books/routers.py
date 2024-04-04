from fastapi import APIRouter

from .schemas import Book, Author


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
