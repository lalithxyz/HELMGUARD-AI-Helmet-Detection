import cv2
import tensorflow as tf

# Load the trained helmet detection model
model = tf.keras.models.load_model("helmet_detection_model.h5")

# Start the camera
camera = cv2.VideoCapture(0)

while True:
    ret, frame = camera.read()

    if not ret:
        break

    # Resize image for MobileNet
    image = cv2.resize(frame, (224, 224))
    image = image / 255.0
    image = image.reshape(1, 224, 224, 3)

    # Predict helmet status
    prediction = model.predict(image, verbose=0)

    if prediction[0][0] > 0.5:
        result = "Helmet Detected - Ignition ON"
    else:
        result = "No Helmet - Ignition OFF"

    # Display result
    cv2.putText(
        frame,
        result,
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 0),
        2
    )

    cv2.imshow("HELMGUARD", frame)

    # Press Q to exit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()
