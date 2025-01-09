# file_management.py
import os

def create_folders(pictures_folder, videos_folder):
    """
    Creates necessary folders if they don't exist.
    Specifically, these folders stores images and videos
    """
    os.makedirs(pictures_folder, exist_ok=True)
    os.makedirs(videos_folder, exist_ok=True)