import cv2

videoPath = 'project.avi'
imagesLocation = 'testData'
frameRate = 0 # for 0 all frames are saved, any other positive number every value of frameRate image will be saved.
#Example: frameRate = 2 , every second image, frameRate = 10 every tenth image

# Opens the Video file
cap = cv2.VideoCapture(videoPath)
i = 1
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break
    if frameRate == 0 or i % frameRate == 0:
        cv2.imwrite(imagesLocation + '\\video_' + str(i) + '.jpg', frame)
    i += 1
 
cap.release()