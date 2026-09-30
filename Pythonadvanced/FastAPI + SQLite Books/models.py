
from pydantic import BaseModel, Field


# ========================================
# Request Model
# ========================================

class BookCreate(BaseModel):
    """Validate data for creating or replacing a book."""

    title: str = Field(min_length=1)
    author: str = Field(min_length=1)
    language: str | None = None
    price: float = Field(ge=0)
    published_year: int | None = None


# ========================================
# Response Model
# ========================================

class Book(BookCreate):
    """Represent a book stored in the database."""

    id: int
    created_at: str