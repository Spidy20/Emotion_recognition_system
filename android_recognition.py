import cv2
import label_image
import os
import  numpy as np
from urllib.request import  urlopen
import time
from playsound import playsound
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

size = 4

# We load the xml file
classifier = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
mobile_video="http://192.168.0.101:8080/shot.jpg"
  # Using default WebCam connected to the PC.

while True:

    img_resp = urlopen(mobile_video)
    img_arr = np.array(bytearray(img_resp.read()), dtype=np.uint8)

    cap = cv2.imdecode(img_arr, -1)
    im=cv2.flip(cap,1,0)
    mini = cv2.resize(im, (int(im.shape[1] / size), int(im.shape[0] / size)))

    # detect MultiScale / faces
    faces = classifier.detectMultiScale(mini)

    # Draw rectangles around each face
    for f in faces:
        (x, y, w, h) = [v * size for v in f]  # Scale the shapesize backup
        sub_face = im[y:y + h, x:x + w]
        FaceFileName = "test.jpg"  # Saving the current image from the webcam for testing.
        cv2.imwrite(FaceFileName, sub_face)
        text = label_image.main(FaceFileName)  # Getting the Result from the label_image file, i.e., Classification Result.
        text = text.title()  # Title Case looks Stunning.
        font = cv2.FONT_HERSHEY_TRIPLEX

        if text == 'Angry':
            cv2.rectangle(im, (x, y), (x + w, y + h), (0, 25, 255), 7)
            cv2.putText(im, text, (x + h, y), font, 1, (0, 25,255), 2)

        if text == 'Smile':
            cv2.rectangle(im, (x, y), (x + w, y + h), (0,260,0), 7)
            cv2.putText(im, text, (x + h, y), font, 1, (0,260,0), 2)

        if text == 'Fear':
            cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 255), 7)
            cv2.putText(im, text, (x + h, y), font, 1, (0, 255, 255), 2)

        if text == 'Sad':
            cv2.rectangle(im, (x, y), (x + w, y + h), (0,191,255), 7)
            cv2.putText(im, text, (x + h, y), font, 1, (0,191,255), 2)

    # Show the image/
    cv2.imshow('Emotion recognition from Android screen', im)
    key = cv2.waitKey(30)& 0xff
    if key == 27:  # The Esc key

        break


