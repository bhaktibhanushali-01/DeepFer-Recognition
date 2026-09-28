import streamlit as st
import cv2
import numpy as np
from PIL import Image
from predict import predict_emotion

st.set_page_config(
    page_title="Facial Emotion Recognition",
    page_icon="😊",
    layout="wide"
)

st.title("😊 Facial Emotion Recognition")
st.write("Upload a face image and the AI model will predict the emotion.")

uploaded_file = st.file_uploader(
    "Upload an Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")

    image_np = np.array(image)

    st.image(image, caption="Uploaded Image", use_column_width=True)

    with st.spinner("Predicting..."):
        emotion, confidence, probabilities = predict_emotion(image_np)

    st.success(f"**Predicted Emotion:** {emotion}")
    st.info(f"**Confidence:** {confidence*100:.2f}%")

    st.subheader("Emotion Probabilities")

    emotions = [
        "Angry",
        "Disgust",
        "Fear",
        "Happy",
        "Neutral",
        "Sad",
        "Surprise"
    ]

    for emo, prob in zip(emotions, probabilities):
        st.progress(float(prob))
        st.write(f"{emo}: {prob*100:.2f}%")