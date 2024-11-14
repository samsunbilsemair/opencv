import cv2

video_path = 0  # camera seçimi yapılır -1 ile 10 arası bir değerde kamera bulunur.
cap = cv2.VideoCapture(video_path)

while cap.isOpened():
    ret, frame = cap.read()

    if ret:
        """ burada yapılan tüm değişikler frame'i etkiler """

        frame = cv2.resize(frame, None, fx=1/3, fy=1/3, interpolation=cv2.INTER_AREA)

        cv2.imshow('Frame', frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()
