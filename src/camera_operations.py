# camera_operations.py
import os
import subprocess

def take_picture(output_folder, image_name):
    """
    Takes a picture using libcamera-still and saves it to the specified folder.
    """
    output_filename = os.path.join(output_folder, image_name)
    try:
        print(f"Taking picture: {output_filename}...")
        subprocess.run(
            ["libcamera-still", "-o", output_filename, "--width", "640", "--height", "480", "--nopreview"],
            check=True
        )
        print(f"Picture saved: {output_filename}")
        return output_filename
    except subprocess.CalledProcessError as e:
        print(f"Error taking picture: {e}")
        exit(1)

def convert_to_mp4(h264_path, mp4_path):
    """
    Converts an H264 video file to MP4 format using ffmpeg.
    """
    try:
        print(f"Converting {h264_path} to {mp4_path}...")
        subprocess.run(
            ["ffmpeg", "-i", h264_path, "-c:v", "copy", mp4_path],
            check=True
        )
        print(f"Conversion complete: {mp4_path}")
        return mp4_path
    except subprocess.CalledProcessError as e:
        print(f"Error converting video: {e}")
        return None

def record_video(output_folder, video_name, duration):
    """
    Records a video using libcamera-vid, converts it to MP4, and saves it.
    """
    h264_filename = os.path.join(output_folder, video_name)
    mp4_filename = h264_filename.replace(".h264", ".mp4")

    try:
        print(f"Recording video: {h264_filename} for {duration} seconds...")
        subprocess.run(
            ["libcamera-vid", "-o", h264_filename, "--width", "640", "--height", "480", "--nopreview", "-t", str(duration * 1000)],
            check=True
        )
        print(f"Video recorded: {h264_filename}")

        # Convert to MP4
        mp4_path = convert_to_mp4(h264_filename, mp4_filename)
        if mp4_path:
            return mp4_path
        else:
            print("Failed to convert video to MP4.")
            return None
    except subprocess.CalledProcessError as e:
        print(f"Error recording video: {e}")
        return None