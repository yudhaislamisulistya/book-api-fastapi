from sqlalchemy import Column, Integer, String
from app.config.database import Base

class Book(Base):
    __tablename__ = "books"
    book_id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    year = Column(Integer, index=True)
    def as_dict(self):
        return {
            "book_id": self.book_id,
            "title": self.title,
            "year": self.year
        }