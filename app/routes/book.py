from fastapi import APIRouter
from app.endpoints import book

router = APIRouter()
router.include_router(book.router)