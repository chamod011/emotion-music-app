from deepface import DeepFace
import cv2

def detect_emotion():
    cap = cv2.VideoCapture(0)

    print("Opening camera... Press 'q' to capture")

    while True:
        ret, frame = cap.read()
        cv2.imshow("Press Q to capture", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    try:
        result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
        emotion = result[0]['dominant_emotion']
        return emotion
    except:
        return "neutral"