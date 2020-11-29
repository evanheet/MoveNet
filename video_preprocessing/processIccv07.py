import numpy
import cv2
import pandas as pd

baseFolder = r'C:\Users\Boris\Desktop\College\Machine Learning\dataset2\merayxu-multiview-object-tracking-dataset-21fcf9ca90b7\merayxu-multiview-object-tracking-dataset-21fcf9ca90b7'
# if no folder path, leave this string empty
folderPath = r'CAMPUS\Garden1'
fileName = 'view-HC2'
#make sure video and text files are in the same folder and named the same
videoFormat = "mp4"
labelFormat = "txt"


labels = []

def buildFilePath(isVideo):
    path = baseFolder + '\\' + folderPath + ('\\' if folderPath else '')  + fileName
    if isVideo:
        return path + '.' + videoFormat
    return path + '.' + labelFormat


"""
You can prepare the labels how ever you want, just make sure that the labels global variabl contains:
[
    {
        "frameNumber" : {
            "x" : (int, int), // coordinates of the starting point for the rectangle
            "y" : (int, int), // for ending point
            "name" : string //label name
        }
    } ...
    each object is additional box that will be drown on the video
]

"""
def loadLabels():
    data = pd.read_csv(buildFilePath(False))

    values = data.values
    for x in range(0, len(values)):
        valuesAsArray = values[x][0].split(" ")
        valuesObject = {
            "objectId" : int(valuesAsArray[0]),
            "labelStartX" : int(valuesAsArray[1]),
            "labelStartY" : int(valuesAsArray[2]),
            "labelEndX" : int(valuesAsArray[3]),
            "labelEndY" : int(valuesAsArray[4]),
            "frameNumber" : valuesAsArray[5],
            "isLost" : True if int(valuesAsArray[6]) else False ,
            "label" : valuesAsArray[9]
        }

        currentObject = {}
        try:
            currentObject = labels[valuesObject["objectId"]]
        except:
            labels.append(currentObject)

        newBox = {"x" : (0,0), "y" : (0,0), "name" : ""}
        if not valuesObject["isLost"]:
            newBox = {
                "x": (valuesObject["labelStartX"], valuesObject["labelStartY"]),
                "y": (valuesObject["labelEndX"], valuesObject["labelEndY"]),
                "name": valuesObject["label"]
            }
        currentObject[valuesObject["frameNumber"]] = newBox
    print("Number of objects", len(labels))
    return 1


def playVideo():
    cap = cv2.VideoCapture(buildFilePath(True))

    fourcc = cv2.VideoWriter_fourcc(*'DIVX')
    out = cv2.VideoWriter('output.MOV',fourcc, 20.0, (640,480))

    frameCount = 1

    while(1):
        
        # read the frames
        _,frame = cap.read()

        #A rectangle
        for x in range(0, len(labels)):
            label = labels[x]
            try:
                cv2.rectangle(
                    frame, 
                    label.get(str(frameCount)).get("x"), 
                    label[str(frameCount)]["y"],
                    (0,255,0), 
                    3)
                cv2.putText(
                    frame, 
                    label[str(frameCount)]["name"], 
                    label.get(str(frameCount)).get("x"), 
                    cv2.FONT_HERSHEY_SIMPLEX,  
                    1, 
                    (255, 0, 0), 
                    2, 
                    cv2.LINE_AA)
            except:
                print("Problem processing object", x, " frame: ", frameCount)
            
        out.write(frame)
        #if key pressed is 'Esc', exit the loop
        cv2.imshow('frame',frame)

        frameCount += 1
        if cv2.waitKey(33)== 27:
            break
    out.release()

    cv2.destroyAllWindows()


loadLabels()
playVideo()