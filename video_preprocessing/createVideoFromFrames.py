import cv2
import numpy as np
import glob

folderWithImagesPath = r'C:\Users\Boris\Desktop\College\Machine Learning data\YOLO_Object_Detection-master\YOLOv3_PyTorch\test\output_multiple_images';
imageFormat = '.jpg'
outputVideoPath = 'project.avi'
img_array = []

def addBackslashStarToPath(path):
    lastChar = path[-1]
    return path + "*" if lastChar == "\\" or lastChar == "/" else path + "\\*"


for filename in glob.glob(addBackslashStarToPath(folderWithImagesPath) + imageFormat):
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)
 
 
out = cv2.VideoWriter(outputVideoPath,cv2.VideoWriter_fourcc(*'DIVX'), 15, size)
 
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()