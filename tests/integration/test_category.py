import json

import pytest

from app.controller import CategoryController


def test_create_category(test_client, monkeypatch):
    test_data = {"id": 1, "name": "something"}

    def mock_put():
        return test_data

    monkeypatch.setattr(CategoryController, "put", mock_put)

    response = test_client.put("/category/", data=json.dumps(test_data), )
    assert response.status_code == 201
    assert response.json() == test_data


def test_create_category_invalid_json(test_client):
    response = test_client.put("/category/", data=json.dumps({"title": "something"}))
    assert response.status_code == 422

    response = test_client.put(
        "/category/", data=json.dumps({"title": "1", "description": "2"})
    )
    assert response.status_code == 422


def test_get_category_by_id(test_client, monkeypatch):
    test_data = {"id": 1, "name": "something"}

    def mock_get(id):
        return test_data

    monkeypatch.setattr(CategoryController, "get", mock_get)

    response = test_client.get("/category/1")
    assert response.status_code == 200
    assert response.json() == test_data


def test_get_category_by_incorrect_id(test_client, monkeypatch):
    def mock_get(id):
        return None

    monkeypatch.setattr(CategoryController, "get", mock_get)

    response = test_client.get("/category/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Note not found"

    response = test_client.get("/notes/0")
    assert response.status_code == 422


def test_get_all_categories(test_client, monkeypatch):
    test_data = [
        {"id": 1, "name": "something"},
        {"id": 2, "name": "else"}
    ]

    def mock_get_all():
        return test_data

    monkeypatch.setattr(CategoryController, "get_all", mock_get_all)

    response = test_client.get("/category/")
    assert response.status_code == 200
    assert response.json() == test_data


def test_update_category(test_client, monkeypatch):
    test_data = {"id": 1, "name": "something"}

    test_update_data = {"id": 1, "name": "changed"}

    def mock_get(id):
        return test_data

    monkeypatch.setattr(CategoryController, "get", mock_get)

    def mock_patch(id):
        return test_update_data

    monkeypatch.setattr(CategoryController, "put", mock_patch)

    response = test_client.put("/category/1/", data=json.dumps(test_update_data), )
    assert response.status_code == 200
    assert response.json() == test_update_data


@pytest.mark.parametrize(
    "id, name, status_code",
    [
        [1, {}, 422],
        [1, {"description": "bar"}, 422],
        [999, {"title": "foo", "description": "bar"}, 404],
        [1, {"title": "1", "description": "bar"}, 422],
        [1, {"title": "foo", "description": "1"}, 422],
        [0, {"title": "foo", "description": "bar"}, 422],
    ],
)
def test_update_note_invalid(test_client, monkeypatch, id, payload, status_code):
    def mock_get(id):
        return None

    monkeypatch.setattr(CategoryController, "get", mock_get)

    response = test_client.put(f"/category/{id}/", data=json.dumps(payload), )
    assert response.status_code == status_code


def test_remove_note(test_client, monkeypatch):
    test_data = {"title": "something", "description": "something else", "id": 1}

    def mock_get(db_session, id):
        return test_data

    monkeypatch.setattr(CategoryController, "get", mock_get)

    def mock_delete(db_session, id):
        return test_data

    monkeypatch.setattr(CategoryController, "delete", mock_delete)

    response = test_client.delete("/category/1/")
    assert response.status_code == 200
    assert response.json() == test_data
