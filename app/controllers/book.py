import app.lib.databases.book as book_db
from sqlalchemy.orm import Session
import app.schemas.book as schema_book

class BookController:
    def get_books(self, db: Session, skip: int = 0, limit: int = 100):
        books = book_db.get_books(db=db, skip=skip, limit=limit)
        return books or []
    
    def create_book(self, db: Session, book=schema_book.Book):
        data = book_db.get_book_by_title(db=db, title=book.title)
        if data:
            return False
        return book_db.create_book(db=db, book=book)
    
    def delete_book(self, db: Session, book_id: int):
        data = book_db.get_book_by_id(db=db, book_id=book_id)
        if not data:
            return False
        return book_db.delete_book_by_id(db=db, book_id=book_id)
        
        
        
        