import boto3
from botocore.exceptions import NoCredentialsError

def upload_to_s3(file_path, bucket_name, access_key, secret_key):
    # print("working")
    # print(file_path)
    s3 = boto3.client('s3', aws_access_key_id=access_key, aws_secret_access_key=secret_key)
   
    try:
        s3.upload_file(str(file_path), bucket_name, str(file_path.name))
        print(f"Uploaded {file_path} to S3 bucket {bucket_name}")
    except NoCredentialsError:
        print("Credentials not available")
