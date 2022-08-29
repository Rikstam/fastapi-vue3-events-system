import json

import pytest


mock_event = {
        "title": "A test event title",
        "description": "A test description",
        "location": "A test location",
        "date": "2022-08-27",
        "time": "13:00:00+00:00",
        "organization": "A test organization"
        }


def test_create_event(test_app_with_db):
    response = test_app_with_db.post("/events/", data=json.dumps(mock_event))

    assert response.status_code == 201
    assert response.json()["title"] == "A test event title"
    assert response.json()["description"] == "A test description"
    assert response.json()["location"] == "A test location"
    assert response.json()["date"] == "2022-08-27"
    assert response.json()["time"] == "13:00:00+00:00"
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

def test_read_event(test_app_with_db):
    response = test_app_with_db.post("/events/", data=json.dumps(mock_event))
    event_id = response.json()["id"]

    response = test_app_with_db.get(f"/events/{event_id}/")
    assert response.status_code == 200

    response_dict = response.json()
    assert response_dict["id"] == event_id
    assert response_dict["title"] == mock_event["title"]
    assert response_dict["description"] == mock_event["description"]
    assert response_dict["location"] == mock_event["location"]

def test_read_event_incorrect_id(test_app_with_db):
    response = test_app_with_db.get("/events/999/")
    assert response.status_code == 404
    assert response.json()["detail"] == "Event not found"

def test_read_all_events(test_app_with_db):
    response = test_app_with_db.post("/events/", data=json.dumps(mock_event))
    event_id = response.json()["id"]

    response = test_app_with_db.get("/events/")
    assert response.status_code == 200

    response_list = response.json()
    assert len(list(filter(lambda d: d["id"] == event_id, response_list))) == 1

def test_delete_event(test_app_with_db):
    response = test_app_with_db.post(
        "/events/", data=json.dumps(mock_event)
    )
    event_id = response.json()["id"]

    response = test_app_with_db.delete(f"/events/{event_id}/")
    
    assert response.status_code == 200
    assert response.json() == {
        "id": event_id,
        "title": mock_event["title"],
        "description": mock_event["description"],
        "location": mock_event["location"],
        "date": mock_event["date"],
        "time": mock_event["time"],
        "organization": mock_event["organization"]
    }

def test_delete_event_incorrect_id(test_app_with_db):
    response = test_app_with_db.delete("/events/999/")
    assert response.status_code == 404
    assert response.json()["detail"] == "Event not found"

def test_update_event(test_app_with_db):
    mock_event["title"] = "updated!"
    response = test_app_with_db.post(
        "/events/", data=json.dumps(mock_event)
    )
    event_id = response.json()["id"]

    response = test_app_with_db.put(
        f"/events/{event_id}/",
        data=json.dumps(mock_event)
    )
    assert response.status_code == 200

    response_dict = response.json()
    assert response_dict["id"] == event_id
    assert response_dict["title"] == mock_event["title"]
    assert response_dict["description"] == mock_event["description"]
    assert response_dict["location"] == mock_event["location"]

