import csv
import time
import PIL.Image
from IPython.display import clear_output
from io import BytesIO
import IPython.display

def array_to_image(a, fmt='jpeg'): # use 'jpeg' instead of 'png' (~5 times faster)
    #Create binary stream object
    f = BytesIO()
    
    #Convert array to binary stream object
    PIL.Image.fromarray(a).save(f, fmt)
    
    return IPython.display.Image(data=f.getvalue())

def end_loop_util(cap, msg):
    tend = time.time()
    cap.release()
    clear_output()
    print(msg)
    return tend

def writeAnotationsToCV(videoName,frameNumber,imageName,outputFolderLocation,outputFileName):
    with open(outputFolderLocation + "{}.csv".format(outputFileName), "a+", newline='') as f:
        writer = csv.writer(f, delimiter=',')
        # write the actual content line by line
        writer.writerow([videoName, frameNumber, imageName])