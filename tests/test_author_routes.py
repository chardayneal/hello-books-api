import pytest
from app.db import db
from app.models.author import Author

def test_get_all_authors_with_no_records(client):
    # Act
    response = client.get("/authors")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

@pytest.fixture
def two_saved_authors(app):
    # Arrange
    c_author = Author(name="C Neal")
    j_author = Author(name="Jayne Allen")

    # db.session.add_all([ocean_book, mountain_book])
    db.session.add(c_author)
    db.session.add(j_author)
    db.session.commit()

@pytest.mark.skip
def test_get_one_author(client, two_saved_authors):
    # Act
    response = client.get("/authors/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Kennedy Ryan"
    }

def test_create_one_book(client):
    # Act
    response = client.post("/authors", json={
        "name": "Kennedy Ryan"
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == {
        "id": 1,
        "name": "Kennedy Ryan"
    }
