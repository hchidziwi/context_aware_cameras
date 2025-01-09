
import tensorflow as tf
import numpy as np

def load_model(model_path):
    """
    Loads the TensorFlow model.
    """
    print("Loading model...")
    model = tf.keras.models.load_model(model_path)
    print("Model loaded successfully.")
    return model

def preprocess_image(image_path):
    """
    Preprocesses the image for the model.
    """
    print(f"Preprocessing image: {image_path}...")
    image = tf.keras.utils.load_img(image_path, target_size=(224, 224))
    image_array = tf.keras.utils.img_to_array(image)
    image_array = np.expand_dims(image_array, axis=0)  # Add batch dimension
    image_array = image_array / 255.0  # Normalize pixel values to [0, 1]
    return image_array