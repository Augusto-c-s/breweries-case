from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_get_breweries():
    response = client.get("/get_breweries")
    assert response.status_code == 200
    json_response = response.json()
    assert isinstance(json_response, dict)
    assert "Data" in json_response
    assert isinstance(json_response["Data"], list)
    assert "status" in json_response
    assert json_response["status"] == "Success"

def test_bronze_layer():
    response = client.post("/bronze_layer")
    assert response.status_code == 200
    assert response.json()["message"] == "Data saved to Bronze layer"

def test_silver_layer():
    response = client.post("/silver_layer")
    assert response.status_code == 200
    assert response.json()["message"] == "Data saved to Silver layer"

def test_gold_layer():
    response = client.post("/gold_layer")
    assert response.status_code == 200
    assert response.json()["message"] == "Data saved to Gold layer"
