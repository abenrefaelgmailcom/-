##### to run the project copy too terminal: python -m uvicorn rest.main:app --reload
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field, ValidationError
app = FastAPI()

# ========================================
# Pydantic Models
# ========================================

class BookCreate(BaseModel):
    title: str = Field(min_length=1)
    author: str = Field(min_length=1)
    year: int
    description: str | None = None


class BookUpdate(BaseModel):
    title: str | None = None
    author: str | None = None
    year: int | None = None
    description: str | None = None


class Book(BookCreate):
    id: int


# ========================================
# FastAPI Application
# ========================================

app = FastAPI(
    title="Books REST API",
    description="A simple CRUD API for managing books",
    version="1.0.0"
)


# ========================================
# In-memory Database
# ========================================

books = [
    {
        "id": 1,
        "title": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "year": 1937,
        "description": "Fantasy novel"
    },
    {
        "id": 2,
        "title": "1984",
        "author": "George Orwell",
        "year": 1949,
        "description": "Dystopian novel"
    },
    {
        "id": 3,
        "title": "Clean Code",
        "author": "Robert C. Martin",
        "year": 2008,
        "description": "Software dev practices"
    }
]

next_id = max(book["id"] for book in books) + 1


# ========================================
# Helper Function
# ========================================

def find_book(book_id: int):
    """Find a book by ID or raise 404."""

    for book in books:
        if book["id"] == book_id:
            return book

    raise HTTPException(
        status_code=404,
        detail="Book not found"
    )


# ========================================
# GET - All Books
# ========================================

@app.get("/books", response_model=list[Book])
def get_books():
    return books

@app.get("/")
def home():
    return {
        "message": "Books REST API is running",
        "documentation": "/docs"
    }

# ========================================
# GET - Book by ID
# ========================================

@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    return find_book(book_id)


# ========================================
# POST - Create Book
# ========================================

@app.post(
    "/books",
    status_code=status.HTTP_201_CREATED
)
def create_book(book: BookCreate):
    global next_id

    new_book = {
        "id": next_id,
        **book.model_dump()
    }

    books.append(new_book)
    next_id += 1

    return {
        "message": "Book created successfully",
        "book": new_book
    }


# ========================================
# PUT - Replace Book
# ========================================

@app.put("/books/{book_id}")
def replace_book(book_id: int, book: BookCreate):
    existing_book = find_book(book_id)

    updated_book = {
        "id": book_id,
        **book.model_dump()
    }

    existing_book.clear()
    existing_book.update(updated_book)

    return {
        "message": "Book replaced successfully",
        "book": existing_book
    }


# ========================================
# PATCH - Partially Update Book
# ========================================

@app.patch("/books/{book_id}")
def update_book(book_id: int, book: BookUpdate):
    existing_book = find_book(book_id)

    changes = book.model_dump(
        exclude_unset=True
    )

    # Validate the complete updated book.
    merged_book = {
        **existing_book,
        **changes
    }

    try:
        validated = Book.model_validate(merged_book)
    except ValidationError as error:
        raise HTTPException(
            status_code=422,
            detail=error.errors()
        )

    existing_book.update(
        validated.model_dump()
    )

    return {
        "message": "Book updated successfully",
        "book": existing_book
    }


# ========================================
# DELETE - Remove Book
# ========================================

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    book = find_book(book_id)

    books.remove(book)

    return {
        "message": "Book deleted successfully",
        "book": book
    }