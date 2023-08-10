from typing import Union
from pydantic import BaseModel
class Book(BaseModel):
    book_id: Union[int, None] = None
    title: str
    year: Union[int, None] = None

    class Config:
        from_attributes = True
        