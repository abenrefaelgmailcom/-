
import sqlite3
from contextlib import contextmanager

DB_NAME = "books.db"


# ========================================
# Database Connection
# ========================================

@contextmanager
def get_connection():
    """Open, commit or rollback, and close a SQLite connection."""

    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row

    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


# ========================================
# Helper Function
# ========================================

def row_to_dict(row):
    """Convert a SQLite row to a dictionary."""

    if row is None:
        return None

    return dict(row)


# ========================================
# Create Table
# ========================================

def create_table_books():
    query = """
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        language TEXT,
        price REAL NOT NULL CHECK(price >= 0),
        published_year INTEGER,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """

    with get_connection() as conn:
        conn.execute(query)


# ========================================
# Drop and Recreate Table
# ========================================

def drop_table_books():
    with get_connection() as conn:
        conn.execute("DROP TABLE IF EXISTS books")


def recreate_table_books():
    """Drop and recreate the books table."""

    # Perform both operations in one transaction.
    with get_connection() as conn:
        conn.execute("DROP TABLE IF EXISTS books")

        conn.execute("""
            CREATE TABLE books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                language TEXT,
                price REAL NOT NULL CHECK(price >= 0),
                published_year INTEGER,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)


# ========================================
# Insert Book
# ========================================

def insert_book(title, author, language, price, published_year):
    query = """
    INSERT INTO books (
        title, author, language, price, published_year
    )
    VALUES (?, ?, ?, ?, ?)
    """

    with get_connection() as conn:
        cursor = conn.execute(
            query,
            (title, author, language, price, published_year)
        )

        book_id = cursor.lastrowid

    return get_book_by_id(book_id)


# ========================================
# Get All Books
# ========================================

def get_all_books():
    query = """
    SELECT
        id,
        title,
        author,
        language,
        price,
        published_year,
        created_at
    FROM books
    ORDER BY id
    """

    with get_connection() as conn:
        rows = conn.execute(query).fetchall()

    return [row_to_dict(row) for row in rows]


# ========================================
# Get Book by ID
# ========================================

def get_book_by_id(book_id):
    query = """
    SELECT
        id,
        title,
        author,
        language,
        price,
        published_year,
        created_at
    FROM books
    WHERE id = ?
    """

    with get_connection() as conn:
        row = conn.execute(
            query,
            (book_id,)
        ).fetchone()

    return row_to_dict(row)


# ========================================
# Update Book
# ========================================

def update_book(
    book_id,
    title,
    author,
    language,
    price,
    published_year
):
    query = """
    UPDATE books
    SET title = ?,
        author = ?,
        language = ?,
        price = ?,
        published_year = ?
    WHERE id = ?
    """

    with get_connection() as conn:
        cursor = conn.execute(
            query,
            (
                title,
                author,
                language,
                price,
                published_year,
                book_id
            )
        )

        affected_rows = cursor.rowcount

    if affected_rows == 0:
        return None

    return get_book_by_id(book_id)


# ========================================
# Delete Book
# ========================================

def delete_book(book_id):
    with get_connection() as conn:
        row = conn.execute(
            """
            SELECT *
            FROM books
            WHERE id = ?
            """,
            (book_id,)
        ).fetchone()

        if row is None:
            return None

        existing_book = row_to_dict(row)

        conn.execute(
            "DELETE FROM books WHERE id = ?",
            (book_id,)
        )

    return existing_book