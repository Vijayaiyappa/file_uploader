# File Uploader

This module reads files from a directory and uploads images and media files to AWS S3, and documents to Google Cloud Storage. The types of files to transfer to S3 and Google Cloud Storage are configurable.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/file_uploader.git
    cd file_uploader
    ```

2. Install the module:
    ```bash
    pip install .
    ```

3. Configure your settings in `config.yaml`.

## Usage

Run the module:
```bash
file-uploader
or
python -m file_uploader.main

