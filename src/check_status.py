import requests
import time
import subprocess
import psutil

# Configuration
CHECK_INTERVAL = 5  # Time interval (in seconds) between checks
REMOTE_PHP_URL = "http://hopechidziwisano.com/check_status.php"  # Replace with your PHP script URL
DEVICE_ID = "device123"  # Replace with the specific device ID
SCRIPT_TO_RUN = "/home/G1/Documents/test_cam/src/main.py"  # Replace with the name of your Python script

def is_script_running(script_name):
    """Check if the script is already running."""
    for process in psutil.process_iter(['name', 'cmdline']):
        if script_name in process.info['cmdline']:
            return process
    return None

def start_script(script_name):
    """Start the other script."""
    subprocess.Popen(["python3", script_name])


def stop_script(process):
    """Stop the running script."""
    process.terminate()
    process.wait()

while True:
    try:
        # Fetch the status from the remote PHP script
        response = requests.get(REMOTE_PHP_URL, params={"device_id": DEVICE_ID})
        response.raise_for_status()
        status = int(response.text.strip())

        # Check if the script is running
        running_process = is_script_running(SCRIPT_TO_RUN)

        if status == 1 and not running_process:
            print(f"Status is 1 for device {DEVICE_ID}. Starting {SCRIPT_TO_RUN}...")
            start_script(SCRIPT_TO_RUN)
        elif status == 0 and running_process:
            print(f"Status is 0 for device {DEVICE_ID}. Stopping {SCRIPT_TO_RUN}...")
            stop_script(running_process)

    except Exception as e:
        print(f"Error: {e}")

    time.sleep(CHECK_INTERVAL)
