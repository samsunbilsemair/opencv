import cv2

video_path = 0  # camera seçimi yapılır -1 ile 10 arası bir değerde kamera bulunur.
cap = cv2.VideoCapture(video_path)

while cap.isOpened():
    ret, frame = cap.read()

    if ret:
        """ burada yapılan tüm değişikler frame'i etkiler """
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cv2.imshow('Frame', frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()
