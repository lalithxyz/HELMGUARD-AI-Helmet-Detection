import cv2
from ultralytics import YOLO

# Load trained HELMGUARD model
model = YOLO("best.pt")

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
        print("Failed to read camera frame.")
        break

    # Run helmet detection
    results = model(frame, conf=0.5)

    # Draw detection boxes
    annotated_frame = results[0].plot()

    helmet_found = False
    no_helmet_found = False

    # Check detected classes
    for box in results[0].boxes:

        class_id = int(box.cls[0])
        class_name = model.names[class_id].lower()

        print("Detected:", class_name)

        if "with helmet" in class_name:
            helmet_found = True

        elif "without helmet" in class_name:
            no_helmet_found = True

    # Decide status
    if helmet_found:
        status = "Helmet Detected"
        ignition = "Ignition ON"

    elif no_helmet_found:
        status = "No Helmet Found"
        ignition = "Ignition OFF"

    else:
        status = "No Rider Detected"
        ignition = "Ignition OFF"

    # Display status
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

    # Show result
    cv2.imshow(
        "HELMGUARD - Helmet Detection",
        annotated_frame
    )

    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
