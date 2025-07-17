```
ekraf-posts-api-to-sftp-etl/
│
├── etl/                            # Core ETL logic
│   ├── __init__.py
│   ├── config.py                   # API URL, SFTP credentials, paths
│   ├── extract.py                  # Extract data from API
│   ├── transform.py                # Transform and flatten records
│   └── load.py                     # Save to CSV + upload to SFTP
│
├── scripts/
│   └── run_etl.py                  # Main runner script
│
├── data/                           # Output folder
│   └── ekraf_posts.csv             # Generated CSV (excluded in .gitignore)
│
├── tests/                          # Optional test files
├── requirements.txt
├── .gitignore
└── README.md
```

| Column Name        | Description                            |
| ------------------ | -------------------------------------- |
| `id`               | Post ID                                |
| `title`            | Title of the post                      |
| `slug`             | URL-friendly title                     |
| `excerpt`          | Short excerpt (HTML-encoded)           |
| `thumbnail_seo`    | Thumbnail image URL                    |
| `published_at`     | When the post was published            |
| `published`        | Boolean indicating if published        |
| `likes`            | Number of likes                        |
| `views`            | Number of views                        |
| `meta_title`       | Metadata (optional title)              |
| `meta_description` | Metadata (optional description)        |
| `meta_keywords`    | Metadata (optional keywords)           |
| `user_id`          | ID of the author                       |
| `created_at`       | When the post was created              |
| `updated_at`       | When the post was last updated         |
| `user_name`        | Name of the user (from nested `user`)  |
| `user_email`       | Email of the user (from nested `user`) |
| `categories`       | Pipe-delimited list of category titles |
| `tags`             | Pipe-delimited list of tag names       |
