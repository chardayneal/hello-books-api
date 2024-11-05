from flask import Blueprint, request, abort, make_response
from app.db import db
from app.models.author import Author

author_bp = Blueprint("author_bp", __name__, url_prefix="/authors")

@author_bp.post("")
def create_author():
    request_body = request.get_json()

    try:
        new_author = Author.from_dict(request_body)

    except KeyError as error:
        response = {"message": f"Invalid request: missing {error.args[0]}"}
        abort(make_response(response, 400))

    db.session.add(new_author)
    db.session.commit()

    return make_response(new_author.to_dict(), 201)

@author_bp.get("")
def get_all_authors():
    query = db.select(Author)
    
    names_param = request.args.get("name")
    if names_param:
        query = query.where(Author.name.ilike(f"%{names_param}%"))

    query = query.order_by(Author.id)
    authors = db.session.scalars(query)

    return [author.to_dict() for author in authors], 200

