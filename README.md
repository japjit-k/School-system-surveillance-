import cv2

# Open webcam (change 0 to a video file path if needed)
camera = cv2.VideoCapture(0)

print("Smart School Surveillance System Started")
print("Press 'q' to stop the program")

while True:
    success, frame = camera.read()

    if not success:
        print("Unable to access camera")
        break

    # Get frame dimensions
    height, width = frame.shape[:2]

    # Define a demonstration restricted area
    zone_x1 = int(width * 0.35)
    zone_y1 = int(height * 0.30)
    zone_x2 = int(width * 0.65)
    zone_y2 = int(height * 0.80)

    # Draw the restricted zone
    cv2.rectangle(
        frame,
        (zone_x1, zone_y1),
        (zone_x2, zone_y2),
        (0, 0, 255),
        2
    )

    cv2.putText(
        frame,
        "RESTRICTED AREA",
        (zone_x1, zone_y1 - 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 0, 255),
        2
    )

    # Display system status
    cv2.putText(
        frame,
        "SMART SCHOOL SURVEILLANCE - ACTIVE",
        (20, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (0, 255, 0),
        2
    )

    # Show camera feed
    cv2.imshow("School Surveillance System", frame)

    # Press q to quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()
