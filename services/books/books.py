from typing import Optional
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from .models import Book
from .schemas import BookCreate


async def get_book(
    session: AsyncSession, 
    id_: Optional[int] = None,
    author_id: Optional[int] = None):
    if id_:
        query = select(Book).filter_by(id=id_)
    elif author_id:
        query = select(Book).filter_by(author_id=author_id)
    else:
        query = select(Book)
    
    result_books = await session.execute(query)
    return result_books.scalars().all()
        


async def create_book(session: AsyncSession, book: BookCreate) -> BookCreate:
    query = insert(Book).values(book.model_dump())
    await session.execute(query)
    await session.commit()
    return book
