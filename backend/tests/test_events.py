import json

import pytest


def test_create_event(test_app_with_db):
    response = test_app_with_db.post("/events/", data=json.dumps({"title": "A test event title"}))

    assert response.status_code == 201
    assert response.json()["title"] == "A test event title"

def test_create_events_invalid_json(test_app):
    response = test_app.post("/events/", data=json.dumps({}))
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "loc": ["body", "title"],
                "msg": "field required",
                "type": "value_error.missing"
            }
        ]
    }
