from pydantic import BaseModel
from typing import Union

class Book(BaseModel):
    book_id: Union[int, None] = None
    title: str
    year: Union[int, None] = None
    
    class Config:
        from_attributes = True
        