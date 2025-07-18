# EKRAF API configuration
API_URL = "https://api.ekraf.go.id/posts"
DEFAULT_PAGE_SIZE = 100  # Max results per request

# Local file settings
CSV_FILENAME = "ekraf_posts.csv"
DATA_DIR = "data/"
CSV_OUTPUT_PATH = DATA_DIR + CSV_FILENAME

# SFTP configuration
SFTP_HOST = "5.189.154.248"
SFTP_PORT = 22
SFTP_USERNAME = "rangsi"
SFTP_PASSWORD = "Passwd093"

# Remote SFTP path to upload the CSV
SFTP_REMOTE_PATH = "/home/rangsi/" + CSV_FILENAME

SFTP_CONFIG = {
    "host": SFTP_HOST,
    "port": SFTP_PORT,
    "username": SFTP_USERNAME,
    "password": SFTP_PASSWORD,
    "remote_path": SFTP_REMOTE_PATH,
}
