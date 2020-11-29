import numpy as np
import cv2
import os

data_paths = r"C:\Users\alexa\Documents\data\mlproj_data"
vid_file = r"Test video for Object Detection __ TRIDE.mp4"
vid_path = os.path.join(data_paths,vid_file)

cap = cv2.VideoCapture(vid_path )

while(cap.isOpened()):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()