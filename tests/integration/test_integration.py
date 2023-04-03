import requests


def test_health_endpoint():
    """
    Tests Health Endpoint while application is running
    """
    response = requests.get("http://127.0.0.1:5000/health")
    assert response.status_code == 200


def test_rps_endpoint():
    """
    Tests the RPS endpoint wehile server is running
    """
    response = requests.post("http://127.0.0.1:5000/rps", json={"move": "rock"})
    assert response.status_code == 200
