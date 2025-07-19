import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

def require_env(key):
    """Raises an error if an expected environment variable is missing."""
    value = os.getenv(key)
    if value is None:
        raise EnvironmentError(f"Missing required environment variable: {key}")
    return value

# EKRAF API configuration
API_URL = "https://api.ekraf.go.id/posts"
DEFAULT_PAGE_SIZE = 100

# Local file settings
CSV_FILENAME = "ekraf_posts.csv"
DATA_DIR = "data/"
CSV_OUTPUT_PATH = os.path.join(DATA_DIR, CSV_FILENAME)

# SFTP configuration from environment variables
SFTP_HOST = require_env("SFTP_HOST")
SFTP_PORT = int(os.getenv("SFTP_PORT", 22))
SFTP_USERNAME = require_env("SFTP_USERNAME")
SFTP_PASSWORD = require_env("SFTP_PASSWORD")
SFTP_REMOTE_DIR = require_env("SFTP_REMOTE_DIR")

SFTP_CONFIG = {
    "host": SFTP_HOST,
    "port": SFTP_PORT,
    "username": SFTP_USERNAME,
    "password": SFTP_PASSWORD,
    "remote_dir": SFTP_REMOTE_DIR,
}
