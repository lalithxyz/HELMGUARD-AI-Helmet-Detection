# HELMGUARD – AI-Based Helmet Detection and Vehicle Safety System

## Project Description

HELMGUARD is an AI-powered helmet detection system designed to improve two-wheeler rider safety. The system uses computer vision and deep learning to detect whether a rider is wearing a helmet. Based on the detection result, the system can allow or restrict vehicle ignition.

## How It Works

1. A camera captures the rider's image.
2. OpenCV processes the captured image.
3. The image is passed to a trained MobileNet deep learning model.
4. The model predicts whether the rider is wearing a helmet.
5. If a helmet is detected, the vehicle ignition is enabled.
6. If no helmet is detected, the ignition remains disabled.

## Technologies Used

- Python
- TensorFlow
- Keras
- MobileNet
- OpenCV
- Arduino / Microcontroller
- Raspberry Pi

## Project Features

- Real-time helmet detection
- Image processing using OpenCV
- Deep learning-based classification
- Helmet / No Helmet prediction
- Automated ignition control
- AI and embedded-system integration

## Model

The project uses a MobileNet-based deep learning model trained to classify helmet and non-helmet images.

The model achieved approximately 95% accuracy during testing.

## Project Details

**Duration:** 2nd Year – Final Year

**Team Size:** 3

**Domain:** Artificial Intelligence, Computer Vision and IoT

**Complexity:** Intermediate to Advanced

## My Contribution

- Dataset preparation
- Image preprocessing
- Model training
- Model testing and evaluation
- Real-time helmet detection
- Integration of detection output with vehicle ignition control

## System Workflow

Camera → Image Processing → MobileNet Model → Helmet Detection → Microcontroller → Ignition Control

## Publication

**Paper Title:** Helmet Detection in Two Wheeler Using Image Processing

**Conference:** 2025 International Conference on Computing and Communication Technologies (ICCCT)

**Year:** 2025

**DOI:** 10.1109/ICCCT63501.2025.11020144

## Key Outcome

Developed a working prototype that combines artificial intelligence, computer vision and embedded systems to detect helmet compliance and control vehicle ignition, providing an automated approach to improve two-wheeler rider safety.
