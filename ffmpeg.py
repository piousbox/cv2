#/usr/bin/env python
import cv2
import time

faceCascade = cv2.CascadeClassifier('/opt/cv2/cascade.xml')

while True:
    try:
        image = cv2.imread('/opt/cv2/a.jpg')
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(
          gray,
          scaleFactor=1.1,
          minNeighbors=5,
          minSize=(30, 30),
          flags = cv2.CASCADE_SCALE_IMAGE
        )
        # print(f"{len(faces)} faces")
        for (x, y, w, h) in faces:
          cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.imwrite('/opt/cv2/b.jpg', image)
        print(".")
        time.sleep(1)
    except Exception:
        pass
