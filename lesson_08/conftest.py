import pytest
import requests
import uuid
from config import BASE_URL, HEADERS


@pytest.fixture
def create_project():
    """Создаёт проект и возвращает его id, удаляет после теста."""
    payload = {
        "title": f"Test Project {uuid.uuid4().hex[:8]}"
    }
    response = requests.post(
        f"{BASE_URL}/projects",
        headers=HEADERS,
        json=payload
    )
    response.raise_for_status()
    project_id = response.json().get("id")
    yield project_id
    # Удаляем проект после теста
    try:
        requests.delete(
            f"{BASE_URL}/projects/{project_id}",
            headers=HEADERS
        )
    except Exception:
        pass


@pytest.fixture
def valid_project_payload():
    return {"title": f"Test Project {uuid.uuid4().hex[:8]}"}
