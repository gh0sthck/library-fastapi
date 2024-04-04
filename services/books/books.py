from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession

from .models import Book
from .schemas import BookCreate


async def create_book(session: AsyncSession, book: BookCreate) -> BookCreate:
    query = insert(Book).values(book.model_dump())
    await session.execute(query)
    await session.commit()
    return book
