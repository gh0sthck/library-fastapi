from typing import TYPE_CHECKING, List
from database import Base

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship


if TYPE_CHECKING:
    from services.books.models import Book


class Catalog(Base):
    __tablename__ = "catalogs"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(90))
    
    books: Mapped[List["Book"]] = relationship(back_populates="catalog")
