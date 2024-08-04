import os
import yaml
from pathlib import Path
import logging
from file_uploader.aws_uploader import upload_to_s3
from file_uploader.gcs_uploader import upload_to_gcs

logging.basicConfig(filename='file_uploader.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logging.info(f"logging has been started")
def list_files(directory):
    files = []
    for root, _, filenames in os.walk(directory):
        for filename in filenames:
            files.append(Path(root) / filename)
    return files

def main():
    config_path = Path(__file__).parent / 'config.yaml'
   
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    p1=Path(__file__).parents[1]
    
    directory = Path(f'{p1}\//test_files//')

    files = list_files(directory)
    

    s3_file_types = config['file_types']['s3']
    gcs_file_types = config['file_types']['gcs']

    for file_path in files:
        # print("---->>>",file_path)
        file_extension = file_path.suffix.lstrip('.').lower()
        if file_extension in s3_file_types:
            try:
                upload_to_s3(file_path, **config['aws'])
                logging.info(f"Uploaded {file_path} to S3 bucket {config['aws']['bucket_name']}")
            except Exception as e:
                logging.error(f"Failed to upload {file_path} to S3: {e}")
        elif file_extension in gcs_file_types:
            try:
                upload_to_gcs(file_path, **config['gcs'])
                logging.info(f"Uploaded {file_path} to GCS bucket {config['gcs']['bucket_name']}")
            except Exception as e:
                logging.error(f"Failed to upload {file_path} to GCS: {e}")

if __name__ == '__main__':
    main()
