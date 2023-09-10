import cv2
import easyocr

# read the image
cap = cv2.VideoCapture(0)

# instance text detection
reader = easyocr.Reader(["en"], gpu=False)

# detect text on image
threshold = 0.1

# draw box and text
while True:
    ret, frame = cap.read()
    text_raw = reader.readtext(frame)
    for t in text_raw:
        # print(t)
        bbox, text, score = t
        print(text)
        if score > threshold:
            cv2.rectangle(frame, bbox[0], bbox[2], (0, 255, 0), 5)
            cv2.putText(
                frame, text, bbox[0], cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    
    cv2.imshow("Text Recognition", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
