import cv2
from time import time
from random import randint
import dropbox

start_time = time()

def take_snapshot():
    num = randint(1,100)
    videoCaptureObject = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    result = True
    while(result):
        ret,frame = videoCaptureObject.read()
        img_name = "img" + str(num) + ".png"
        cv2.imwrite(img_name,frame)
        result = False
        return img_name
    print("Snapshot taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()
