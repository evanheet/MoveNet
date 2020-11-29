import numpy as np
import cv2
import os

data_paths = r"C:\Users\alexa\Documents\data\mlproj_data"
vid_file = r"Test video for Object Detection __ TRIDE.mp4"
vid_path = os.path.join(data_paths,vid_file)

cap = cv2.VideoCapture(vid_path)

# Define the codec and create VideoWriter object
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
fourcc = cv2.VideoWriter_fourcc('M','J','P','G')
out = cv2.VideoWriter('output4.avi',fourcc, 10, (frame_width,frame_height))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        frame = cv2.flip(frame,0)

        # write the flipped frame
        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
        
# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()