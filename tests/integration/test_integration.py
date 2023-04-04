import requests
import pytest


@pytest.mark.integration
def test_health_endpoint(app_url):
    """
    Tests Health Endpoint while application is running
    """
    response = requests.get(app_url + "/:5000/health")
    assert response.status_code == 200


@pytest.mark.integration
def test_rps_endpoint(app_url):
    """
    Tests the RPS endpoint wehile server is running
    """
    response = requests.post(app_url + "/:5000/rps", json={"move": "rock"})
    assert response.status_code == 200
