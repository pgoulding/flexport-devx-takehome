import requests
import pytest
import os

app_url = os.environ.get("APP_URL")


@pytest.mark.integration
def test_health_endpoint():
    """
    Test the health endpoint of the application.

    :param app_url: The URL of the running application.
    :type app_url: str
    """
    response = requests.get(app_url + "/health")
    assert response.status_code == 200


@pytest.mark.integration
def test_rps_endpoint():
    """
    Test the RPS endpoint of the application while the server is running.

    :param app_url: The URL of the running application.
    :type app_url: str
    """
    response = requests.post(app_url + "/rps", json={"move": "rock"})
    assert response.status_code == 200
