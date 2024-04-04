import datetime
from typing import Optional
from pydantic import BaseModel, Field


class Author(BaseModel):
    id: int
    first_name: str = Field(max_length=128)
    last_name: str = Field(max_length=128)
    patronymic: str = Field(max_length=128)
    birthday_date: datetime.datetime
    deathday_date: Optional[datetime.datetime]


class Book(BaseModel):
    id: int
    title: str = Field(max_length=90)
    author: Author
    description: str = Field(max_length=256)
    publish_date: datetime.datetime
    isbn: str
