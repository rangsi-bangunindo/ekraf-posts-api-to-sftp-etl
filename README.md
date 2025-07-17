# EKRAF Posts ETL: API to SFTP

This ETL (Extract, Transform, Load) pipeline retrieves publication posts from the EKRAF public API, flattens and transforms the data, saves the output into a structured CSV file, and uploads it to a remote SFTP server.

---

## Features

- Extracts paginated posts from the EKRAF API
- Flattens nested fields such as `attachments`, `categories`, and `tags`
- Outputs timestamped CSV files
- Uploads the result to an SFTP server

---

## Project Structure

```
ekraf-posts-api-to-sftp-etl/
├── data/
│   └── ekraf_posts_<TIMESTAMP>.csv          # Output CSV
├── etl/
│   ├── __init__.py
│   ├── config.py                            # API URL, credentials, output paths
│   ├── extract.py                           # Data extraction logic
│   ├── transform.py                         # Data flattening & formatting
│   └── load.py                              # CSV export and SFTP uploader
├── scripts/
│   ├── __init__.py
│   └── run_etl.py                           # Entry-point to run the ETL
├── tests/
│   ├── __init__.py
│   ├── test_extract.py
│   ├── test_transform.py
│   └── test_load.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Installation

```bash
pip install -r requirements.txt
```

---

## Running the ETL

```bash
python -m scripts.run_etl
```

This will generate a timestamped CSV under `data/` and upload it to the configured SFTP server.

---

## Output CSV Schema

The generated CSV contains the following columns:

| Column        | Description                                   |
| ------------- | --------------------------------------------- |
| `id`          | Unique post identifier                        |
| `title`       | Post title                                    |
| `slug`        | URL-friendly identifier                       |
| `status`      | Publication status                            |
| `headline`    | Headline text                                 |
| `content`     | HTML content of the post                      |
| `type`        | Post type or category                         |
| `view_count`  | Total views                                   |
| `created_at`  | Timestamp when created                        |
| `updated_at`  | Last updated timestamp                        |
| `attachments` | Concatenated attachment URLs (joined by `\|`) |
| `categories`  | Concatenated category titles (joined by `\|`) |
| `tags`        | Concatenated tag names (joined by `\|`)       |

---

## Configuration

Edit the configuration values in `etl/config.py`:

```python
API_URL = "https://api.ekraf.go.id/posts"
CSV_FILENAME = "ekraf_posts.csv"
DATA_DIR = "data/"
SFTP_HOST = "your.sftp.host"
SFTP_PORT = 22
SFTP_USERNAME = "your_username"
SFTP_PASSWORD = "your_password"
SFTP_REMOTE_PATH = "/remote/path/" + CSV_FILENAME
```

---

## Running Tests

To run unit tests individually:

```bash
pytest tests/test_extract.py -v
pytest tests/test_transform.py -v
pytest tests/test_load.py -v
```

---

## Dependencies

Defined in `requirements.txt`:

```
requests
paramiko
pytest
```
