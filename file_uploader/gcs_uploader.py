from google.cloud import storage
import os

def upload_to_gcs(file_path, bucket_name, project, credentials):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credentials
    client = storage.Client(project=project)
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(str(file_path.name))
    blob.upload_from_filename(str(file_path))
    print(f"Uploaded {file_path} to GCS bucket {bucket_name}")
