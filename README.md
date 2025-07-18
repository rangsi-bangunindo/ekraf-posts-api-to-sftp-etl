# EKRAF Posts ETL: API to SFTP

A modular ETL pipeline that automates the extraction of publication posts from the EKRAF public API, transforms nested JSON data into a clean, flat CSV format, and transfers the result to a remote server via SFTP. Designed for efficient integration between open APIs and internal systems.

---

## 1. Features

- Extracts all paginated data from the EKRAF API.
- Normalizes nested fields (e.g., `attachments`, `categories`, `tags`) into CSV-ready structure.
- Preserves key metadata (timestamps, status, view counts).
- Outputs timestamped CSVs for traceability.
- Transfers files securely to a remote SFTP server.
- Built with modular Python scripts and unit-tested components.

---

## 2. Project Structure

```
ekraf-posts-api-to-sftp-etl/
├── data/
│   └── ekraf_posts_<TIMESTAMP>.csv     # Output directory for timestamped CSV files
├── etl/
│   ├── init.py
│   ├── config.py                       # Stores API endpoint, output path, and SFTP credentials
│   ├── extract.py                      # Contains functions to fetch and paginate API data
│   ├── transform.py                    # Handles normalization and flattening of nested JSON fields
│   └── load.py                         # Handles CSV writing and SFTP file upload
├── scripts/
│   ├── init.py
│   └── run_etl.py                      # Main runner script to execute the ETL pipeline
├── tests/
│   ├── init.py
│   ├── conftest.py                     # Shared fixtures for unit tests
│   ├── test_extract.py                 # Unit tests for the extraction logic
│   ├── test_transform.py               # Unit tests for data transformation
│   ├── test_load.py                    # Unit tests for CSV generation and SFTP upload
│   └── test_input.json                 # Sample API response used in tests
├── pytest.ini                          # Pytest configuration file
├── requirements.txt                    # Lists required Python packages
├── .gitignore                          # Specifies files/folders to ignore in version control
└── README.md                           # Project documentation
```

---

## 3. Installation

### `Clone the Repository`

```bash
git clone https://github.com/rangsi-bangunindo/ekraf-posts-api-to-sftp-etl.git
cd ekraf-posts-api-to-sftp-etl
```

### `Create a Virtual Environment`

```bash
python -m venv .venv
```

### `Activate the Virtual Environment`

- On **Windows**:

```bash
.venv\Scripts\activate
```

- On **macOS/Linux**:

```bash
source .venv/bin/activate
```

### `Install Dependencies`

```bash
pip install -r requirements.txt
```

### `Configure the Project`

Edit the following values in `etl/config.py`:

```python
API_URL = "https://api.ekraf.go.id/posts"
CSV_FILENAME = "ekraf_posts.csv"
DATA_DIR = "data/"
SFTP_HOST = "<sftp_host>"
SFTP_PORT = 22
SFTP_USERNAME = "<username>"
SFTP_PASSWORD = "<password>"
SFTP_REMOTE_PATH = "remote/path/" + CSV_FILENAME
```

---

## 4. Testing

The project includes unit tests for each ETL stage under `etl/`, using mock input to ensure reliability without hitting the live API.

**Test Modules:**

- `tests/test_extract.py`: Validates API requests, pagination, and response parsing.
- `tests/test_transform.py`: Verifies flattening of nested fields and data formatting.
- `tests/test_load.py`: Checks CSV generation and SFTP upload logic.

Run tests with:

```bash
pytest -v
```

Test discovery is managed via pytest.ini, targeting the tests/ directory.

---

## 5. Run the ETL Process

Trigger the full ETL pipeline with:

```bash
python -m scripts.run_etl
```

Ensure configuration values in `etl/config.py` are properly set (API URL, SFTP credentials, output path) before execution.

---

## 6. Output CSV Schema

The generated CSV file contains the following columns, extracted and normalized from the API response:

| Column             | Description                                           |
| ------------------ | ----------------------------------------------------- |
| `id`               | Unique identifier of the post                         |
| `title`            | Title of the post                                     |
| `slug`             | URL-friendly identifier                               |
| `excerpt`          | Short summary or preview of the post                  |
| `thumbnail_seo`    | SEO-optimized thumbnail URL                           |
| `published_at`     | Timestamp indicating when the post was published      |
| `published`        | Boolean indicating whether the post is published      |
| `likes`            | Total number of likes                                 |
| `views`            | Total number of views                                 |
| `liked`            | Boolean indicating if the current user liked the post |
| `meta_title`       | SEO meta title                                        |
| `meta_description` | SEO meta description                                  |
| `meta_keywords`    | SEO meta keywords                                     |
| `user_id`          | ID of the user who created the post                   |
| `created_at`       | Timestamp of post creation                            |
| `updated_at`       | Timestamp of last update                              |
| `user_name`        | Name of the user who created the post                 |
| `user_email`       | Email of the user who created the post                |
| `categories`       | Category titles, concatenated with `\|`               |
| `tags`             | Tag names, concatenated with `\|`                     |
| `attachments`      | Attachment URLs, concatenated with `\|`               |

---

## 7. Error Handling & Logging

Each ETL stage includes targeted error handling to improve fault tolerance and traceability:

- **Extraction**: Handles `requests` exceptions (e.g., timeouts, connection errors), invalid status codes, and pagination errors with informative logs.
- **Transformation**: Checks for missing or malformed fields and applies defaults or skips records while logging warnings.
- **Loading**: Captures file I/O errors (e.g., write permissions, disk space) and SFTP issues (e.g., connection timeouts, auth failures via `paramiko`).

All logs are printed to the console with contextual details. Fatal errors terminate the pipeline early with clear messages to prevent silent data loss or partial transfers.
