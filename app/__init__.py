from flask import Flask
from app.db import db, migrate
from app.models import book, author
from app.routes.book_routes import books_bp
from app.routes.author_routes import author_bp
import os


def create_app(config=None):
    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')

    if config:
        app.config.update(config)

    db.init_app(app)
    migrate.init_app(app, db)

    #register Blueprints here
    app.register_blueprint(books_bp)
    app.register_blueprint(author_bp)

    return app