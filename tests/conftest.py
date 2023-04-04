import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--app_url", action="store", default="http://localhost/", help="Application URL"
    )


@pytest.fixture(scope="session")
def app_url(request):
    return request.config.getoption("--app_url")
