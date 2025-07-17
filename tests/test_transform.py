# tests/test_transform.py

import pytest
from etl.transform import transform_posts

sample_raw_posts = [
    {
        "id": 101,
        "title": "Sample Title One",
        "slug": "sample-title-one",
        "excerpt": "<p>Excerpt One</p>",
        "thumbnail_seo": "https://cdn.example.com/thumb1.jpg",
        "published_at": "2024-07-01T12:00:00Z",
        "published": True,
        "likes": 10,
        "views": 200,
        "meta_title": "Meta Title One",
        "meta_description": "Meta Description One",
        "meta_keywords": "keyword1, keyword2",
        "user_id": 1,
        "created_at": "2024-06-01T12:00:00Z",
        "updated_at": "2024-07-01T12:00:00Z",
        "user": {
            "name": "John Doe",
            "email": "john@example.com"
        },
        "categories": [
            {"title": "Culture"},
            {"title": "Events"}
        ],
        "tags": [
            {"name": "Music"},
            {"name": "Festival"}
        ]
    },
    {
        "id": 102,
        "title": "Sample Title Two",
        "slug": "sample-title-two",
        "excerpt": "<p>Excerpt Two</p>",
        "thumbnail_seo": "https://cdn.example.com/thumb2.jpg",
        "published_at": "2024-07-02T13:30:00Z",
        "published": False,
        "likes": 5,
        "views": 150,
        "meta_title": "Meta Title Two",
        "meta_description": "Meta Description Two",
        "meta_keywords": "keyword3, keyword4",
        "user_id": 2,
        "created_at": "2024-06-05T10:00:00Z",
        "updated_at": "2024-07-02T14:00:00Z",
        "user": {
            "name": "Jane Smith",
            "email": "jane@example.com"
        },
        "categories": [
            {"title": "Business"},
            {"title": "Technology"}
        ],
        "tags": [
            {"name": "Startup"},
            {"name": "AI"}
        ]
    }
]

def test_transform_posts():
    result = transform_posts(sample_raw_posts)
    
    assert isinstance(result, list)
    assert len(result) == 2
    
    # Check first post details
    post1 = result[0]
    assert post1["id"] == 101
    assert post1["title"] == "Sample Title One"
    assert post1["published"] is True
    assert post1["user_name"] == "John Doe"
    assert post1["categories"] == "Culture|Events"
    assert post1["tags"] == "Music|Festival"

    # Check second post details
    post2 = result[1]
    assert post2["id"] == 102
    assert post2["title"] == "Sample Title Two"
    assert post2["published"] is False
    assert post2["user_email"] == "jane@example.com"
    assert post2["categories"] == "Business|Technology"
    assert post2["tags"] == "Startup|AI"
