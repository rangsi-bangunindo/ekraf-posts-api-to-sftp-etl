import csv
from etl.load import save_to_csv

def test_transform_posts(tmp_path):
    # Sample transformed data with 2 posts
    sample_posts = [
        {
            "id": 101,
            "title": "First Post",
            "slug": "first-post",
            "excerpt": "<p>Excerpt One</p>",
            "thumbnail_seo": "https://cdn.example.com/thumb1.jpg",
            "published_at": "2024-07-01T12:00:00Z",
            "published": True,
            "likes": 10,
            "views": 200,
            "meta_title": "Meta Title One",
            "meta_description": "Meta Desc One",
            "meta_keywords": "music,art",
            "user_id": 1,
            "created_at": "2024-06-01T12:00:00Z",
            "updated_at": "2024-07-01T12:00:00Z",
            "user_name": "Alice",
            "user_email": "alice@example.com",
            "categories": "Culture|Events",
            "tags": "Music|Festival"
        },
        {
            "id": 102,
            "title": "Second Post",
            "slug": "second-post",
            "excerpt": "<p>Excerpt Two</p>",
            "thumbnail_seo": "https://cdn.example.com/thumb2.jpg",
            "published_at": "2024-07-02T13:30:00Z",
            "published": False,
            "likes": 25,
            "views": 150,
            "meta_title": "Meta Title Two",
            "meta_description": "Meta Desc Two",
            "meta_keywords": "business,tech",
            "user_id": 2,
            "created_at": "2024-06-05T10:00:00Z",
            "updated_at": "2024-07-02T14:00:00Z",
            "user_name": "Bob",
            "user_email": "bob@example.com",
            "categories": "Business|Technology",
            "tags": "Startup|AI"
        }
    ]

    output_file = tmp_path / "posts.csv"
    save_to_csv(sample_posts, str(output_file))

    # Check if file exists
    assert output_file.exists()

    # Read with csv.DictReader
    with output_file.open(newline='', encoding='utf-8') as f:
        reader = list(csv.DictReader(f))

    assert len(reader) == 2
    assert reader[0]["title"] == "First Post"
    assert reader[0]["user_name"] == "Alice"
    assert reader[1]["title"] == "Second Post"
    assert reader[1]["user_email"] == "bob@example.com"
