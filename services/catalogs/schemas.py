from pydantic import BaseModel, Field


class Catalog(BaseModel):
    id: int
    title: str = Field(max_length=90)
