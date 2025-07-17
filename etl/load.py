import csv
import os
import paramiko
from datetime import datetime
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

def remote_path_exists(sftp, path):
    try:
        sftp.stat(path)
        return True
    except FileNotFoundError:
        return False

def upload_to_sftp(local_file_path, remote_path=None):
    """
    Uploads a local file to the specified SFTP server.
    If remote_path is not provided, uploads to /uploads/filename.csv.
    """
    sftp_host = SFTP_CONFIG["host"]
    sftp_port = SFTP_CONFIG["port"]
    sftp_user = SFTP_CONFIG["username"]
    sftp_pass = SFTP_CONFIG["password"]

    filename = os.path.basename(local_file_path)
    if not remote_path:
        remote_path = f"/uploads/{filename}"

    transport = paramiko.Transport((sftp_host, sftp_port))
    transport.connect(username=sftp_user, password=sftp_pass)

    sftp = paramiko.SFTPClient.from_transport(transport)

    remote_dir = os.path.dirname(remote_path)
    if remote_path_exists(sftp, remote_dir):
        print(f"Remote directory exists: {remote_dir}")
        print("Remote contents:", sftp.listdir(remote_dir))
    else:
        print(f"Remote directory does not exist: {remote_dir}")
        sftp.close()
        transport.close()
        return  # Skip upload

    sftp.put(local_file_path, remote_path)
    print(f"File uploaded successfully to: {remote_path}")
    print(f"Uploaded file is available at: /uploads/{os.path.basename(local_file_path)}")

    sftp.close()
    transport.close()
