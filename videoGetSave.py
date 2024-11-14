import cv2
cap = cv2.VideoCapture(0)
frame_witdh = int(cap.get(3))
frame_higth = int(cap.get(4))

video_cod = cv2.VideoWriter.fourcc(*"XVID")
videoOutput = cv2.VideoWriter("../assets/videomuz.avi", video_cod, 30, (frame_witdh, frame_higth))

while True:
    ret, frame = cap.read()

    if ret:
        cv2.imshow("FRAME", frame)
        videoOutput.write(frame)
        if cv2.waitKeyEx(25) & 0xFF == ord("q"):
            break
    else:
        break

cap.release()
videoOutput.release()
cv2.destroyAllWindows()

