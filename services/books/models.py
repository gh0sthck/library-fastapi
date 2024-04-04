import datetime
from typing import TYPE_CHECKING
from database import Base

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship


if TYPE_CHECKING:
    from services.catalogs.models import Catalog
    

class Author(Base):
    __tablename__ = "authors"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(128))
    last_name: Mapped[str] = mapped_column(String(128))
    patronymic: Mapped[str] = mapped_column(String(128))
    birthday_date: Mapped[datetime.datetime]
    deathday_date: Mapped[datetime.datetime]


class Book(Base):
    __tablename__ = "books"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(90), unique=True)
    author_id: Mapped[int] = mapped_column(ForeignKey("authors.id", ondelete="CASCADE"))
    description: Mapped[str] = mapped_column(String(256))
    publish_date: Mapped[datetime.datetime]
    isbn: Mapped[str]
    catalog_id: Mapped[int] = mapped_column(ForeignKey("catalogs.id", ondelete="CASCADE"))
    
    catalog: Mapped["Catalog"] = relationship("catalogs", back_populates="books")
