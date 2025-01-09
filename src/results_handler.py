# results_handler.py
from datetime import datetime

def save_results_to_file(results_filename, image_name, prediction):
    """
    Saves the prediction result to a text file.
    """
    with open(results_filename, "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        result_line = f"{timestamp}: Image - {image_name}, Prediction - {prediction}\n"
        file.write(result_line)
    print(f"Results saved to {results_filename}.")
