from etl.transform import transform_posts

def test_transform_posts(sample_raw_posts):
    result = transform_posts(sample_raw_posts["data"])

    assert isinstance(result, list)
    assert len(result) == 10

    for post in result:
        assert "id" in post
        assert "title" in post
        assert "published" in post
        assert "categories" in post
        assert "tags" in post
