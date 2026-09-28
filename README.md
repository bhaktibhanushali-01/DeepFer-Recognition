# 😊 Facial Emotion Recognition

## 📌 Project Overview

**Facial Emotion Recognition** is a Deep Learning project that predicts human emotions from face images.

The project includes a trained Keras model and a **Streamlit web application** where users can upload an image and receive the predicted emotion, confidence score, and probability for each supported emotion.

The application supports seven emotion classes:

- Angry
- Disgust
- Fear
- Happy
- Neutral
- Sad
- Surprise

The Streamlit interface allows a user to upload JPG, JPEG, or PNG images and displays the prediction directly in the application. fileciteturn0file0L13-L18

## 🎯 Objectives

- Build a facial emotion recognition application.
- Use a trained Deep Learning model for image classification.
- Preprocess uploaded face images before prediction.
- Predict the emotion with the highest model probability.
- Display prediction confidence.
- Display probabilities for all seven emotion classes.
- Provide an easy-to-use Streamlit interface.

## 🧠 Emotion Classes

The model supports the following seven classes:

| Class | Emotion |
|---|---|
| 0 | Angry |
| 1 | Disgust |
| 2 | Fear |
| 3 | Happy |
| 4 | Neutral |
| 5 | Sad |
| 6 | Surprise |

The same emotion labels are used by the prediction pipeline. fileciteturn0file1L8-L16

## 🛠️ Technologies Used

- Python
- TensorFlow / Keras
- OpenCV
- NumPy
- Pillow
- Streamlit
- Matplotlib
- Scikit-learn
- Seaborn

## 🏗️ Project Architecture

```text
User Uploads Image
        ↓
Streamlit Application
        ↓
Image Conversion to RGB
        ↓
NumPy Image Array
        ↓
Image Preprocessing
        ↓
Resize to 224 × 224
        ↓
Normalize Pixel Values
        ↓
Trained Keras Model
        ↓
Emotion Prediction
        ↓
Predicted Emotion + Confidence
        ↓
Emotion Probability Display
```

## 🔄 Prediction Pipeline

The prediction system loads the trained model from:

```text
best_model.keras
```

The model is loaded using TensorFlow/Keras. fileciteturn0file1L5-L6

### Image Preprocessing

Uploaded images are:

1. Resized to **224 × 224** pixels.
2. Converted to `float32`.
3. Normalized by dividing pixel values by `255.0`.
4. Expanded with a batch dimension before prediction. fileciteturn0file1L19-L33

```python
image = cv2.resize(image, (224, 224))
image = image.astype("float32") / 255.0
image = np.expand_dims(image, axis=0)
```

### Prediction

The processed image is passed to the trained model:

```python
prediction = model.predict(processed, verbose=0)
```

The class with the highest probability is selected using `argmax`, and the maximum probability is used as the confidence score. fileciteturn0file1L36-L51

## 💻 Streamlit Application

The application is built using **Streamlit**.

Users can upload:

```text
.jpg
.jpeg
.png
```

The uploaded image is displayed in the application before prediction. fileciteturn0file0L16-L27

After prediction, the application displays:

```text
Predicted Emotion
Confidence
Emotion Probabilities
```

The probability of each emotion is shown individually using Streamlit progress indicators. fileciteturn0file0L29-L49

## 📊 Output Example

For an uploaded image, the application provides:

```text
Predicted Emotion: Happy
Confidence: XX.XX%

Emotion Probabilities

Angry: XX.XX%
Disgust: XX.XX%
Fear: XX.XX%
Happy: XX.XX%
Neutral: XX.XX%
Sad: XX.XX%
Surprise: XX.XX%
```

## 📁 Project Structure

```text
Facial-Emotion-Recognition/
│
├── app.py
├── predict.py
├── best_model.keras
├── requirements.txt
└── README.md
```

## 📦 Requirements

The project uses:

```text
streamlit==1.39.0
tensorflow==2.21.0
opencv-python
numpy
Pillow
matplotlib
scikit-learn
seaborn
protobuf==6.31.1
```

These dependencies are specified in the project's requirements file. fileciteturn0file2L1-L9

## ▶️ How to Run Locally

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the Project

```bash
cd Facial-Emotion-Recognition
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Environment

**Windows:**

```powershell
venv\Scripts\activate
```

**macOS / Linux:**

```bash
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the Streamlit Application

```bash
streamlit run app.py
```

The application will open in your browser.

## 📌 Important Files

### `app.py`

Contains the Streamlit user interface, image upload functionality, prediction display, confidence score, and emotion probability visualization. fileciteturn0file0L1-L5

### `predict.py`

Contains the model loading, image preprocessing, and emotion prediction functions. fileciteturn0file1L1-L5

### `best_model.keras`

Trained TensorFlow/Keras model used for emotion classification.

### `requirements.txt`

Contains the Python dependencies required to run the project. fileciteturn0file2L1-L9

## 🚀 Future Improvements

Possible improvements include:

- Face detection before emotion classification.
- Real-time webcam emotion recognition.
- Video-based emotion recognition.
- Model performance comparison.
- Data augmentation.
- Improved handling of multiple faces.
- Deployment to a cloud platform.
- Model explainability and confidence calibration.

## 💡 Key Takeaway

This project demonstrates an end-to-end **Deep Learning image classification application**, combining a trained TensorFlow/Keras model with a Streamlit interface for practical facial emotion prediction.

It demonstrates skills in:

`Python` · `TensorFlow` · `Keras` · `OpenCV` · `NumPy` · `Streamlit` · `Deep Learning` · `Computer Vision` · `Image Classification`

## 👩‍💻 Author

**Bhakti Bhanushali**
