# 🧠 Brain Tumor Classification using CNN

A deep learning project that classifies brain MRI images into four categories using Convolutional Neural Networks (CNN). The model achieves approximately **95% validation accuracy** after dataset cleaning, preprocessing, and model optimization.

---

## Features

- Brain MRI Classification
- Four-Class Prediction
- Custom CNN Architecture
- Image Preprocessing
- Data Augmentation
- FastAPI Inference API
- Docker Support
- GitHub Actions CI/CD

---

## Dataset

Classes

- Glioma
- Meningioma
- Pituitary Tumor
- No Tumor

Dataset Size

- 2,500 MRI Images

---

## Tech Stack

- Python
- TensorFlow
- Keras
- NumPy
- Pandas
- OpenCV
- Matplotlib
- FastAPI
- Docker
- GitHub Actions

---

## Model Pipeline

MRI Images

↓

Image Cleaning

↓

Resize Images

↓

Normalization

↓

Data Augmentation

↓

CNN Model

↓

Prediction

↓

FastAPI Deployment

---

## Model Architecture

- Convolution Layers
- ReLU Activation
- Max Pooling
- Batch Normalization
- Global Average Pooling
- Dense Layers
- Softmax Output

---

## Performance

| Metric | Score |
|---------|--------|
| Validation Accuracy | 95% |
| Precision | High |
| Recall | High |
| F1 Score | High |

---

## Project Structure

```
Brain-Tumor-CNN/
│
├── dataset/
├── models/
├── notebooks/
├── app/
├── static/
├── Dockerfile
├── requirements.txt
├── README.md
└── main.py
```

---

## Installation

```bash
git clone <repository>

cd Brain-Tumor-CNN

pip install -r requirements.txt

python train.py
```

---

## FastAPI

Run

```bash
uvicorn main:app --reload
```

Prediction Endpoint

```
POST /predict
```

---

## Evaluation

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix
- Classification Report

---

## Future Improvements

- Vision Transformer (ViT)
- EfficientNet Implementation
- Grad-CAM Explainability
- Multi-label Classification
- Ensemble Learning
- Model Quantization
- TensorRT Optimization
- Mobile Deployment
- ONNX Export
- Real-time MRI Upload Portal
- PACS Integration
- Cloud Deployment on AWS SageMaker
- Clinical Decision Support Dashboard

---

## Author

Tamasala Vinay Kumar

AI Engineer | Deep Learning | Computer Vision | CNN | FastAPI | AWS
