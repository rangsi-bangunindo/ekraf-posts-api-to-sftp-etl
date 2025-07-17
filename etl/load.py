import csv
import os
from datetime import datetime
import paramiko
from etl.config import SFTP_CONFIG, DATA_DIR

def save_to_csv(data, filename=None):
    """
    Saves transformed post data to a CSV file in the data/ directory.
    Automatically generates a timestamped filename if not provided.
    """
    if not filename:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"ekraf_posts_{timestamp}.csv"

    filepath = os.path.join(DATA_DIR, filename)

    if not data:
        raise ValueError("No data to write.")

    with open(filepath, mode="w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

    return filepath  # So we can upload it

def upload_to_sftp(local_file_path, remote_filename=None):
    """
    Uploads a local file to the specified SFTP server.
    """
    sftp_host = SFTP_CONFIG["host"]
    sftp_port = SFTP_CONFIG["port"]
    sftp_user = SFTP_CONFIG["username"]
    sftp_pass = SFTP_CONFIG["password"]

    if not remote_filename:
        remote_filename = os.path.basename(local_file_path)

    transport = paramiko.Transport((sftp_host, sftp_port))
    transport.connect(username=sftp_user, password=sftp_pass)

    sftp = paramiko.SFTPClient.from_transport(transport)
    sftp.put(local_file_path, remote_filename)

    sftp.close()
    transport.close()
