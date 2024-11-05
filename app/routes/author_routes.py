from flask import Blueprint, request, abort, make_response
from app.db import db
from app.models.author import Author
from app.models.book import Book
from app.routes.route_utilities import create_model, validate_model

author_bp = Blueprint("author_bp", __name__, url_prefix="/authors")

@author_bp.post("")
def create_author():
    request_body = request.get_json()

    return create_model(Author, request_body)

@author_bp.post("/<author_id>/books")
def create_book_with_author(author_id):
    author = validate_model(Author, author_id)

    request_body = request.get_json()
    request_body["author_id"] = author.id

    return create_author(Author, request_body)

@author_bp.get("")
def get_all_authors():
    query = db.select(Author)
    
    names_param = request.args.get("name")
    if names_param:
        query = query.where(Author.name.ilike(f"%{names_param}%"))

    query = query.order_by(Author.id)
    authors = db.session.scalars(query)

    return [author.to_dict() for author in authors], 200

@author_bp.get("/<author_id>/books")
def get_all_book_by_author(author_id):
    author = validate_model(Author, author_id)

    return [book.to_dict for book in author.books], 200