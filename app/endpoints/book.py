from fastapi import APIRouter, Depends, Response, status, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from app.controllers.book import BookController
from app.config.database import SessionLocal, engine
import app.models.book as model_book
import app.schemas.book as schema_book


router = APIRouter(
    prefix="/books",
    tags=["books"],
)

model_book.Base.metadata.create_all(bind=engine)
book_controller = BookController()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
async def read_books(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    response: Response = None,
):
    results = book_controller.get_books(db=db, skip=skip, limit=limit)
    if not results:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"detail": "Books not found", "status_code": status.HTTP_404_NOT_FOUND}
    return results


@router.post("/", response_model=schema_book.Book)
async def create_book(book: schema_book.Book, db: Session = Depends(get_db)):
    results = book_controller.create_book(db=db, book=book)
    if not results:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={
                "message": "Book already exists",
                "status_code": status.HTTP_400_BAD_REQUEST,
            },
        )
    response_content = {
        "data": results.as_dict(),
        "detail": {
            "message": "Successfully added book",
            "status_code": status.HTTP_201_CREATED,
        },
    }
    return JSONResponse(content=response_content, status_code=status.HTTP_201_CREATED)

@router.put("/{book_id}", response_model=schema_book.Book)
async def update_book(book_id: int, book: schema_book.Book, db: Session = Depends(get_db)):
    results = book_controller.update_book(db=db, book_id=book_id, book=book)
    if not results:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                "message": "Book not found",
                "status_code": status.HTTP_404_NOT_FOUND,
            },
        )
    response_content = {
        "detail": {
            "message": "Successfully updated book",
            "status_code": status.HTTP_200_OK,
        },
    }
    return JSONResponse(content=response_content, status_code=status.HTTP_200_OK)

@router.delete("/{book_id}")
async def delete_book(book_id: int, db: Session = Depends(get_db)):
    results = book_controller.delete_book(db=db, book_id=book_id)
    if not results:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                "message": "Book not found",
                "status_code": status.HTTP_404_NOT_FOUND,
            },
        )
    response_content = {
        "detail": {
            "message": "Successfully deleted book",
            "status_code": status.HTTP_200_OK,
        }
    }
    return JSONResponse(content=response_content, status_code=status.HTTP_200_OK)
