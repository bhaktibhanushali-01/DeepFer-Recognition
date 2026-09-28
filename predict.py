import cv2
import numpy as np
import tensorflow as tf

# Load trained model
model = tf.keras.models.load_model("best_model.keras")

# Emotion labels
emotion_labels = [
    "Angry",
    "Disgust",
    "Fear",
    "Happy",
    "Neutral",
    "Sad",
    "Surprise"
]

IMG_SIZE = 224


def preprocess_image(image):
    """
    Preprocess image for prediction.
    """

    image = cv2.resize(image, (IMG_SIZE, IMG_SIZE))

    image = image.astype("float32") / 255.0

    image = np.expand_dims(image, axis=0)

    return image


def predict_emotion(image):
    """
    Predict emotion from image.
    """

    processed = preprocess_image(image)

    prediction = model.predict(processed, verbose=0)

    predicted_index = np.argmax(prediction)

    confidence = float(np.max(prediction))

    emotion = emotion_labels[predicted_index]

    return emotion, confidence, prediction[0]