from unittest.mock import patch
from etl.extract import fetch_posts

class MockResponse:
    def __init__(self, json_data, status_code=200):
        self._json_data = json_data
        self.status_code = status_code

    def json(self):
        return self._json_data

    def raise_for_status(self):
        if self.status_code >= 400:
            raise Exception(f"HTTP {self.status_code}")

@patch("etl.extract.requests.get")
def test_fetch_posts(mock_get, sample_raw_posts):
    # Simulate paginated responses (e.g., 5 per page)
    page1 = sample_raw_posts.copy()
    page1["data"] = sample_raw_posts["data"][:5]
    page1["pagination"]["total_pages"] = 2

    page2 = sample_raw_posts.copy()
    page2["data"] = sample_raw_posts["data"][5:]
    page2["pagination"]["total_pages"] = 2

    mock_get.side_effect = [
        MockResponse(page1),
        MockResponse(page2)
    ]

    result = fetch_posts()

    assert isinstance(result, list)
    assert len(result) == len(sample_raw_posts["data"])
    assert result[0]["id"] == sample_raw_posts["data"][0]["id"]
    assert result[-1]["id"] == sample_raw_posts["data"][-1]["id"]
