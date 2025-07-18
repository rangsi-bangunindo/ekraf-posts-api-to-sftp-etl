def transform_posts(raw_posts):
    """
    Transforms raw post data into a flat structure for CSV export.
    Returns a list of dictionaries with the expected schema.
    """
    transformed = []

    for post in raw_posts:
        user = post.get("user") or {}
        categories = post.get("categories") or []
        tags = post.get("tags") or []
        attachments = post.get("attachments") or []

        transformed.append({
            "id": post.get("id"),
            "title": (post.get("title") or "").strip(),
            "slug": (post.get("slug") or "").strip(),
            "excerpt": (post.get("excerpt") or "").strip(),
            "thumbnail_seo": (post.get("thumbnail_seo") or "").strip(),
            "published_at": post.get("published_at"),
            "published": post.get("published", False),
            "likes": post.get("likes", 0),
            "views": post.get("views", 0),
            "liked": post.get("liked", False),
            "meta_title": (post.get("meta_title") or "").strip(),
            "meta_description": (post.get("meta_description") or "").strip(),
            "meta_keywords": (post.get("meta_keywords") or "").strip(),
            "user_id": post.get("user_id"),
            "created_at": post.get("created_at"),
            "updated_at": post.get("updated_at"),
            "user_name": (user.get("name") or "").strip(),
            "user_email": (user.get("email") or "").strip(),
            "categories": "|".join(
                (cat.get("title") or "").strip()
                for cat in categories
                if isinstance(cat, dict) and cat.get("title")
            ),
            "tags": "|".join(
                (tag.get("name") or "").strip()
                for tag in tags
                if isinstance(tag, dict) and tag.get("name")
            ),
            "attachments": "|".join(
                (att.get("file") or "").strip()
                for att in attachments
                if isinstance(att, dict) and att.get("file")
            )
        })

    return transformed
