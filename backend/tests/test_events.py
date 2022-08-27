import json

import pytest


def test_create_event(test_app_with_db):
    response = test_app_with_db.post("/events/", data=json.dumps({
        "title": "A test event title",
        "description": "A test description",
        "location": "A test location",
        "date": "2022-08-27",
        "time": "13:00",
        "organization": "A test organization"
        }))

    assert response.status_code == 201
    assert response.json()["title"] == "A test event title"
    assert response.json()["description"] == "A test description"
    assert response.json()["location"] == "A test location"
    assert response.json()["date"] == "2022-08-27"
    assert response.json()["time"] == "13:00:00"
    assert response.json()["organization"] == "A test organization"

def test_create_events_invalid_json(test_app):
    response = test_app.post("/events/", data=json.dumps({}))
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "loc": ["body", "title"],
                "msg": "field required",
                "type": "value_error.missing"
            },
            {
                "loc": ["body", "description"],
                "msg": "field required",
                "type": "value_error.missing"
            },
            {
                "loc": ["body", "location"],
                "msg": "field required",
                "type": "value_error.missing"
            },
            {
                "loc": ["body", "date"],
                "msg": "field required",
                "type": "value_error.missing"
            },
            {
                "loc": ["body", "time"],
                "msg": "field required",
                "type": "value_error.missing"
            },
            {
                "loc": ["body", "organization"],
                "msg": "field required",
                "type": "value_error.missing"
            },
        ]
    }
