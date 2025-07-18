from etl.extract import fetch_posts
from etl.transform import transform_posts
from etl.load import save_to_csv, upload_to_sftp

def run_etl():
    print("Starting ETL process...")

    # Extract
    print("Fetching posts from API...")
    raw_posts = fetch_posts()
    print(f"Fetched {len(raw_posts)} posts.")

    # Transform
    print("Transforming posts...")
    transformed_posts = transform_posts(raw_posts)
    print(f"Transformed {len(transformed_posts)} posts.")

    # Load and save to CSV
    print("Saving transformed posts to CSV...")
    csv_path = save_to_csv(transformed_posts)
    print(f"Saved CSV to: {csv_path}")

    # Upload CSV to SFTP
    print("Uploading CSV to SFTP server...")
    upload_to_sftp(csv_path)
    print("Upload complete!")

if __name__ == "__main__":
    run_etl()
