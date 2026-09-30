
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException, status

import dal
from models import Book, BookCreate


# ========================================
# Application Startup
# ========================================

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Create the table when the server starts.
    dal.create_table_books()

    yield


# ========================================
# FastAPI Application
# ========================================

app = FastAPI(
    title="Books REST API",
    description="REST API using FastAPI, DAL and SQLite",
    version="1.0.0",
    lifespan=lifespan
)


# ========================================
# Root Endpoint
# ========================================

@app.get("/")
def root():
    return {
        "message": "Books API is running",
        "docs": "/docs"
    }


# ========================================
# GET - All Books
# ========================================

@app.get(
    "/books",
    response_model=list[Book]
)
def get_books():
    return dal.get_all_books()


# ========================================
# GET - Book by ID
# ========================================

@app.get(
    "/books/{book_id}",
    response_model=Book
)
def get_book(book_id: int):
    book = dal.get_book_by_id(book_id)

    if book is None:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    return book


# ========================================
# POST - Create Book
# ========================================

@app.post(
    "/books",
    response_model=Book,
    status_code=status.HTTP_201_CREATED
)
def create_book(book: BookCreate):
    return dal.insert_book(
        title=book.title,
        author=book.author,
        language=book.language,
        price=book.price,
        published_year=book.published_year
    )


# ========================================
# PUT - Update Book
# ========================================

@app.put(
    "/books/{book_id}",
    response_model=Book
)
def update_book(book_id: int, book: BookCreate):
    updated_book = dal.update_book(
        book_id=book_id,
        title=book.title,
        author=book.author,
        language=book.language,
        price=book.price,
        published_year=book.published_year
    )

    if updated_book is None:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    return updated_book


# ========================================
# DELETE - Book by ID
# ========================================

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    deleted_book = dal.delete_book(book_id)

    if deleted_book is None:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    return {
        "message": "Book deleted successfully",
        "book": deleted_book
    }


# ========================================
# DELETE - Recreate Books Table
# ========================================

@app.delete("/tables/books")
def recreate_books_table():
    dal.recreate_table_books()

    return {
        "message": "Books table recreated successfully"
    }