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

```text
ekraf-posts-api-to-sftp-etl/
├── data/
│   └── ekraf_posts_<TIMESTAMP>.csv     # Output directory for timestamped CSV files
├── etl/
│   ├── __init__.py
│   ├── config.py                       # Loads configuration from .env and defines constants
│   ├── extract.py                      # Functions to fetch and paginate API data
│   ├── transform.py                    # Normalizes and flattens nested JSON fields
│   └── load.py                         # Handles CSV writing and SFTP file upload
├── scripts/
│   ├── __init__.py
│   └── run_etl.py                      # Main script to execute the ETL pipeline
├── tests/
│   ├── __init__.py
│   ├── conftest.py                     # Shared fixtures for unit tests
│   ├── test_input.json                 # Sample API response for testing
│   ├── test_extract.py                 # Unit tests for extraction logic
│   ├── test_transform.py               # Unit tests for data transformation
│   └── test_load.py                    # Unit tests for CSV generation and SFTP upload
├── .env                                # Environment-specific configuration
├── .gitignore                          # Specifies files/folders to ignore in version control
├── pytest.ini                          # Pytest configuration file
├── requirements.txt                    # Lists required Python packages
└── README.md                           # Project documentation
```

---

## 3. Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/rangsi-bangunindo/ekraf-posts-api-to-sftp-etl.git
   cd ekraf-posts-api-to-sftp-etl
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv .venv
   ```

3. **Activate the Virtual Environment**

   - On **Windows**:

     ```bash
     .venv\Scripts\activate
     ```

   - On **macOS/Linux**:

     ```bash
     source .venv/bin/activate
     ```

4. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

5. **Set Up Environment Variables**

   Create a `.env` file in the project root with the following variables:

   ```env
   SFTP_HOST=<your_sftp_host>
   SFTP_PORT=22
   SFTP_USERNAME=<your_sftp_username>
   SFTP_PASSWORD=<your_sftp_password>
   SFTP_REMOTE_DIR=/uploads
   ```

   > `SFTP_REMOTE_DIR` must be an existing directory on the remote server. The uploaded CSV filename is generated dynamically based on the current timestamp.

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

Test discovery is managed via `pytest.ini`, targeting the `tests/` directory.

---

## 5. Run the ETL Process

Execute the full ETL pipeline:

```bash
python -m scripts.run_etl
```

The script will:

1. Extract data from the EKRAF API.
2. Transform and flatten the structure.
3. Save results as a timestamped CSV in `data/`.
4. Upload the CSV file to the remote SFTP server in the specified `/uploads` directory.

Configuration is automatically loaded from `.env` through `etl/config.py`.

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

---

## 8. Opening the CSV in Excel

The exported CSV uses `utf-8-sig` encoding to preserve special characters (e.g., avoiding `—` becoming `â€`) and `csv.QUOTE_MINIMAL` quoting to avoid unnecessary quotation marks.

### Why Excel May Break the Format

- The CSV uses commas (`,`) as delimiters and contains semicolons (`;`) inside field values.
- Excel may incorrectly split fields like `"Creative; Digital"` due to the system’s **List Separator** setting, which often defaults to semicolon in certain regions.

Using **Text to Columns** with a comma delimiter may result in data loss.

### Recommended Way to Import

1. Go to **Data** → **From Text/CSV**.
2. Select the file.
3. In the import dialog:
   - Set **File Origin** to `65001: Unicode (UTF-8)`.
   - Set **Delimiter** to **Comma**.
   - Click **Load**.

### Optional Cleanup

- Clear table formatting via **Table Design** → **Clear**.
- Remove query connections via **Query** → **Delete**, then close the **Queries & Connections** pane.
- Toggle **Filter** in **Sort & Filter** to disable auto-filters.

> Alternatively, the file can be opened directly in Google Sheets without formatting issues.
