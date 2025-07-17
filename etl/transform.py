def transform_posts(raw_posts):
    """
    Transforms raw post data into a flat structure for CSV export.
    Returns a list of dictionaries with the desired schema.
    """
    transformed = []

    for post in raw_posts:
        user = post.get("user") or {}
        categories = post.get("categories") or []
        tags = post.get("tags") or []

        transformed.append({
            "id": post.get("id"),
            "title": post.get("title", "").strip(),
            "slug": post.get("slug"),
            "excerpt": post.get("excerpt"),
            "thumbnail_seo": post.get("thumbnail_seo"),
            "published_at": post.get("published_at"),
            "published": post.get("published"),
            "likes": post.get("likes", 0),
            "views": post.get("views", 0),
            "meta_title": post.get("meta_title"),
            "meta_description": post.get("meta_description"),
            "meta_keywords": post.get("meta_keywords"),
            "user_id": post.get("user_id"),
            "created_at": post.get("created_at"),
            "updated_at": post.get("updated_at"),
            "user_name": user.get("name"),
            "user_email": user.get("email"),
            "categories": "|".join(cat.get("title", "").strip() for cat in categories if "title" in cat),
            "tags": "|".join(tag.get("name", "").strip() for tag in tags if "name" in tag),
        })

    return transformed