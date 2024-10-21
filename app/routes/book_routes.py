from flask import Blueprint, abort, make_response
from ..models.book import books

books_bp = Blueprint("books_bp", __name__, url_prefix="/books")

@books_bp.get("")
def get_all_books():
    books_response = []
    for book in books:
        books_response.append(
            {
                "id": book.id,
                "title": book.title,
                "description": book.description
            }
        )
    
    return books_response

@books_bp.get("/<book_id>")
def get_book_by_id(book_id):
    book = validate_book(book_id)

    return {
        "id" : book.id,
        "title" : book.title,
        "book_description" : book.description  
    }



def validate_book(book_id):
    try:
        book_id = int(book_id)
    except:
        response = {"message": f"book {book_id} invalid"}
        abort(make_response(response, 400))

    for book in books:
        if book_id == book.id:
            return book
    
    response = {"message": f"Book {book_id} not found"}
    abort(make_response(response, 404))