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
def test_fetch_posts(mock_get):
    # Simulate page 1
    mock_get.side_effect = [
        MockResponse({
            "status": "success",
            "message": "Data fetched",
            "data": [
                {"id": 1, "title": "Post 1", "excerpt": "Summary 1"},
                {"id": 2, "title": "Post 2", "excerpt": "Summary 2"}
            ],
            "pagination": {"total_pages": 2}
        }),
        # Simulate page 2
        MockResponse({
            "data": [
                {"id": 3, "title": "Post 3", "excerpt": "Summary 3"}
            ],
            "pagination": {"total_pages": 2}
        }),
        # Simulate empty third page (should not happen, but just in case)
        MockResponse({"data": [], "pagination": {"total_pages": 2}})
    ]

    result = fetch_posts()
    
    assert isinstance(result, list)
    assert len(result) == 3
    assert result[0]["id"] == 1
    assert result[2]["title"] == "Post 3"   
    