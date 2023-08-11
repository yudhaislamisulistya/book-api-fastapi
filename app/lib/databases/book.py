from sqlalchemy.orm import Session
import app.models.book as book_model

def get_books(db: Session, skip: int = 0, limit: int = 1000):
    return db.query(book_model.Book).offset(skip).limit(limit).all()

def get_book_by_title(db: Session, title: str):
    return db.query(book_model.Book).filter(book_model.Book.title == title).first()

def get_book_by_id(db: Session, book_id: int):
    return db.query(book_model.Book).filter(book_model.Book.book_id == book_id).first()

def create_book(db: Session, book: book_model.Book):
    db_book = book_model.Book(title=book.title, year=book.year)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def delete_book_by_id(db: Session, book_id: int):
    db.query(book_model.Book).filter(book_model.Book.book_id == book_id).delete()
    db.commit()
    return True

def update_book_by_id(db: Session, book_id: int, book: book_model.Book):
    db.query(book_model.Book).filter(book_model.Book.book_id == book_id).update({book_model.Book.title: book.title, book_model.Book.year: book.year})
    db.commit()
    return True