from flask import abort, make_response
from app.db import db

def validate_model(cls, model_id):
    try:
        model_id = int(model_id)

    except:
        response = {"message": f"{cls.__name__} id {model_id} invalid"}
        abort(make_response(response, 400))

    query = db.select(cls).where(cls.id == model_id)
    model = db.session.scalar(query)

    if model:
        return model
    
    response = {"message": f"{cls.__name} {model_id} not found"}
    abort(make_response(response, 404))