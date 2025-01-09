# file_uploader.py
import requests

def upload_file(file_path, upload_url, additional_data):
    """
    Uploads a file to a remote server.
    """
    try:
        print(f"Uploading {file_path} to {upload_url}...")
        with open(file_path, 'rb') as f:
            files = {'file': f}
            data = additional_data
            response = requests.post(upload_url, files=files, data=data)
        if response.status_code == 200:
            print(response.text)
        else:
            print(f"Upload failed: {response.status_code}, {response.text}")
    except Exception as e:
        print(f"Error uploading file: {e}")