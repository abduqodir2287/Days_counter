from fastapi.testclient import TestClient

from src.main import app
from src.domain.days.service import days_left


client = TestClient(app)

def test_app():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Message": "Hello world"}

def test_app_not_found():
    response = client.get("/something")
    assert response.status_code == 404
    assert response.json() == {"detail": "Not Found"}

def test_router():
    response = client.get("/days/", params={"year": 2025, "month": 1, "day": 1})
    assert response.status_code == 200

def test_router_already_passed():
    response = client.get("/days/", params={"year": 2020, "month": 1, "day": 1})
    assert response.status_code == 200
    assert response.json() == {"result": "Этот день уже прошел"}

def test_router_incorrect_date():
    response = client.get("/days/", params={"year": 2025, "month": 14, "day": 35})
    assert response.status_code == 200
    assert response.json() == {"result": "Введена некорректная дата"}

def test_router_ok():
    year = 2027
    month = 7
    day = 13
    date = days_left(year, month, day)
    response = client.get("/days/", params={"year": year, "month": month, "day": day})
    assert response.status_code == 200
    assert response.json() == date

def test_router_bad_request():
    year = 2020
    month = 3
    day = 8
    date = days_left(year, month, day)
    response = client.get("/days/", params={"year": year, "month": month, "day": day})
    assert response.status_code == 200
    assert response.json() == date

def test_router_not_found():
    response = client.get("/days/something")
    assert response.status_code == 404
    assert response.json() == {"detail": "Not Found"}

