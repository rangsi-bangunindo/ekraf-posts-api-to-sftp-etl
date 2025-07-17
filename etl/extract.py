import requests

BASE_URL = "https://api.ekraf.go.id/posts"

def fetch_posts():
    """
    Fetch all posts from the EKRAF API using pagination.
    Returns:
        List[Dict]: A list of post dictionaries.
    """
    posts = []
    page = 1

    while True:
        response = requests.get(BASE_URL, params={"page": page})
        response.raise_for_status()

        data = response.json()

        # Validate structure
        page_posts = data.get("data", [])
        pagination = data.get("pagination", {})

        if not page_posts:
            break

        posts.extend(page_posts)

        # Stop if last page reached
        total_pages = pagination.get("total_pages")
        if total_pages is None or page >= total_pages:
            break

        page += 1

    return posts
