import copy

import pytest
from fastapi.testclient import TestClient

from src.app import app, activities

initial_activities_state = copy.deepcopy(activities)


@pytest.fixture
def client():
    """Fixture that resets activities before each test and returns a TestClient."""
    activities.clear()
    activities.update(copy.deepcopy(initial_activities_state))
    return TestClient(app)
