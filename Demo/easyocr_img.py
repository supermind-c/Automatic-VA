import cv2
import easyocr
import matplotlib.pyplot as plt


# read the image
image_path = "C:\\Users\\66961\\Documents\\Image_Processing\\ref_img\\5_1.jpg"
img = cv2.imread(image_path)

# instance text detection
reader = easyocr.Reader(['en'], gpu=False)
# detect text on image
text_raw = reader.readtext(img)

threshold = 0.25

#draw box and text
for t in text_raw:
    #print(t)
    bbox, text, score = t
    print(text)
    if score > threshold:
        cv2.rectangle(img, bbox[0], bbox[2], (0,255,0), 5)
        cv2.putText(img, text, bbox[0], cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)
        
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()
    