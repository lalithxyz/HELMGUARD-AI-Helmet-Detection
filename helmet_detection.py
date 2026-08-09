import cv2
from ultralytics import YOLO

# Load the helmet detection model
model = YOLO("helmet_model.pt")

# Start webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Cannot access camera.")
    exit()

print("HELMGUARD started.")
print("Press Q to exit.")

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Run helmet detection
    results = model(frame, conf=0.5)

    # Draw detections
    annotated_frame = results[0].plot()

    # Check detected classes
    helmet_found = False
    no_helmet_found = False

    for box in results[0].boxes:
        class_id = int(box.cls[0])
        class_name = model.names[class_id].lower()

        if "helmet" in class_name and "no" not in class_name:
            helmet_found = True

        if "no" in class_name and "helmet" in class_name:
            no_helmet_found = True

    # Display status
    if helmet_found:
        status = "Helmet Detected"
        ignition = "Ignition ON"
    elif no_helmet_found:
        status = "No Helmet Found"
        ignition = "Ignition OFF"
    else:
        status = "No Rider Detected"
        ignition = "Ignition OFF"

    cv2.putText(
        annotated_frame,
        status,
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.putText(
        annotated_frame,
        ignition,
        (20, 80),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 255, 255),
        2
    )

    cv2.imshow("HELMGUARD - Helmet Detection", annotated_frame)

    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
