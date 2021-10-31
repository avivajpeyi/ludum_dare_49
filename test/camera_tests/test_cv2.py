import cv2

# capture frames from a camera with device index=0
cap = cv2.VideoCapture(0)


check, frame = cap.read()

print(frame)


# loop runs if capturing has been initialized
while 1:

    # reads frame from a camera
    check, frame = cap.read()

    if check:
        # Display the frame
        cv2.imshow("Camera", frame)

    # Wait for 25ms
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# release the camera from video capture
cap.release()

# De-allocate any associated memory usage
cv2.destroyAllWindows()
