from flask import Blueprint, abort, make_response, request, Response
from app.models.book import Book
from ..db import db
# from ..models.book import books

books_bp = Blueprint("books_bp", __name__, url_prefix="/books")

@books_bp.post("")
def create_book():
    request_body = request.get_json()

    try:
        new_book = Book.from_dict(request_body)
    
    except KeyError as error:
        response = {"message": f"Invalid request: missing {error.args[0]}"}
        abort(make_response(response, 400))
        
    db.session.add(new_book)
    db.session.commit()

    return new_book.to_dict(), 201

@books_bp.get("")
def get_all_books():
    title_param = request.args.get("title")

    if title_param: 
        query = db.select(Book).where(Book.title.ilike(f"%{title_param}%")).order_by(Book.id)
        books = db.session.scalars(query)        
    else :
        query = db.select(Book).order_by(Book.id)
        books = db.session.scalars(query)

    return [book.to_dict() for book in books]

    
@books_bp.get("/<book_id>")
def get_one_book(book_id):
    return validate_book(book_id).to_dict()

@books_bp.put("/book_id")
def update_one_book(book_id):
    book = validate_book(book_id)

    request_body = request.get_json()
    for key, value in request_body:
        book[key] = value
    db.session.commit()

    return Response(status=204, mimetype="application/json")

@books_bp.delete("/<book_id>")
def delete_book(book_id):
    book = validate_book(book_id)
    db.session.delete(book)
    db.session.commit()

    return Response(status=204, mimetype="application/json")

def validate_book(book_id):
    try:
        book_id = int(book_id)
    except:
        response = {"message": f"book {book_id} invalid"}
        abort(make_response(response, 400))

    query = db.select(Book).where(Book.id == book_id)
    book = db.session.scalar(query)

    if book:
        return book
    
    response = {"message": f"Book {book_id} not found"}
    abort(make_response(response, 404))

