import pytest
from fastapi.testclient import TestClient
import copy
from pathlib import Path
import sys

# Ensure src is importable
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))
from app import app, activities


@pytest.fixture
def client():
    """Test client for the FastAPI app."""
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_activities():
    """Reset the in-memory activities dict before each test (Arrange).

    This prevents tests from affecting each other's state.
    """
    original = copy.deepcopy(activities)
    yield
    activities.clear()
    activities.update(copy.deepcopy(original))
