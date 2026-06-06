import cv2

def find_camera():
    """
    Finds available camera (Iriun or system webcam)
    """
    for i in range(5):
        cam = cv2.VideoCapture(i)
        if cam.isOpened():
            return i
    return 0


def detect_face():
    """
    Open camera and detect faces using OpenCV
    """
    cam_index = find_camera()
    cam = cv2.VideoCapture(cam_index)

    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    while True:
        ret, frame = cam.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            # Draw rectangle on face
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        cv2.imshow("NOVA Vision", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()