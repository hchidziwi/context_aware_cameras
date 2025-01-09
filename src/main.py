import time
import RPi.GPIO as GPIO
from datetime import datetime
from file_management import create_folders
from camera_operations import take_picture, record_video
from model_utils import load_model, preprocess_image
from results_handler import save_results_to_file
from file_uploader import upload_file
from pir_sensor import setup_pir_sensor, detect_motion
import config

def main():
    last_prediction = None

    # Setup
    create_folders(config.pictures_folder, config.videos_folder)
    setup_pir_sensor(config.PIR_SENSOR_PIN)
    model = load_model(config.model_path)

    try:
        while True:
            # Step 1: Take a picture
            image_name = f"picture_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
            image_path = take_picture(config.pictures_folder, image_name)

            # Step 2: Preprocess the image
            preprocessed_image = preprocess_image(image_path)

            # Step 3: Predict
            print("Making prediction...")
            predictions = model.predict(preprocessed_image)
            label = "Indoors" if predictions[0][0] > 0.5 else "Outdoors"

            print(f"Prediction: {label}")

            # Step 4: Save the result
            save_results_to_file(config.results_filename, image_name, label)

            # Step 5: Upload image if prediction changes
            if label != last_prediction:
                upload_file(image_path, config.image_upload_url, {'device_id': config.DEVICE_ID, 'label': label})
                last_prediction = label

            # Step 6: Monitor PIR sensor if outdoors
            if label == "Indoors":
                print("Monitoring PIR sensor for motion...")
                if detect_motion(config.PIR_SENSOR_PIN):
                    print("Motion detected!")
                    video_name = f"video_{datetime.now().strftime('%Y%m%d_%H%M%S')}.h264"
                    video_path = record_video(config.videos_folder, video_name, config.VIDEO_DURATION)
                    if video_path:
                        upload_file(video_path, config.video_upload_url, {'device_id': config.DEVICE_ID, 'label': 'Outdoors'})
                else:
                    print("No motion detected.")
            else:
                print("Environment detected as indoors. No video recording.")

            # Pause before the next iteration
            time.sleep(5)
    except KeyboardInterrupt:
        print("Stopping program.")
    finally:
        GPIO.cleanup()
        print("Cleaned up GPIO.")

if __name__ == "__main__":
    main()
