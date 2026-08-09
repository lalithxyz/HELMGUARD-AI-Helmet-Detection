# HELMGUARD – System Workflow

## Workflow

Camera
↓
Image Capture
↓
YOLO Helmet Detection Model
↓
Helmet Classification
↓
With Helmet / Without Helmet
↓
Vehicle Ignition Control

## Detection Logic

### With Helmet

Helmet detected → Ignition ON

### Without Helmet

No helmet detected → Ignition OFF

## AI Model

The system uses a trained YOLO model to identify two classes:

- With Helmet
- Without Helmet
