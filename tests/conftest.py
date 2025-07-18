import pytest
import json
from pathlib import Path

@pytest.fixture
def sample_raw_posts():
    json_path = Path(__file__).parent / "test_input.json"
    with open(json_path, "r", encoding="utf-8") as f:
        return json.load(f)
