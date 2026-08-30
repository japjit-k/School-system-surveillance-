import cv2
from datetime import datetime
import csv
import os

# Load face detection model
face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# Create log file with headings
log_file = "security_log.csv"

if not os.path.exists(log_file):
    with open(log_file, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date & Time", "Event"])

# Start webcam
camera = cv2.VideoCapture(0)

print("AI School Surveillance System Started")
print("Press Q to stop")

person_detected_before = False

while True:
    success, frame = camera.read()

    if not success:
        print("Unable to access camera!")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_detector.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5
    )

    if len(faces) > 0:
        status = "PERSON DETECTED"

        # Draw boxes around detected faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h),
                          (0, 255, 0), 2)

        # Log event only once when a person appears
        if not person_detected_before:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            with open(log_file, "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([current_time, "Person detected"])

            person_detected_before = True

    else:
        status = "AREA CLEAR"
        person_detected_before = False

    # Display status
    cv2.putText(
        frame,
        status,
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.imshow("AI School Surveillance System", frame)

    # Press Q to exit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

   camera.release()
cv2.destroyAllWindows()

print("System stopped successfully.")                                                                                                                                                       
                                                                                                                                                               
                                                                                                                                        