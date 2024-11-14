# import the necessary packages
from collections import deque
import numpy as np
import argparse
import cv2
import imutils

def decode(myframe):
    left = np.zeros((400,632,3), np.uint8)
    right = np.zeros((400,632,3), np.uint8)
    
    for i in range(400):
        left[i] = myframe[i, 32: 640 + 24] 
        right[i] = myframe[i, 640 + 24: 640 + 24 + 632] 
    
    return (left, right)

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video",
                help="path to the (optional) video file")
ap.add_argument("-o", "--output",
                help="path to the (optional) output video file")
args = vars(ap.parse_args())


if args.get("video", False):        

    vs = cv2.VideoCapture(args["video"])
    videofile = True

    # Get video metadata

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video_fps = vs.get(cv2.CAP_PROP_FPS)
    height = 400 #vs.get(cv2.CAP_PROP_FRAME_HEIGHT)
    width = 632 #vs.get(cv2.CAP_PROP_FRAME_WIDTH)

    if args.get("output", False):
        resizevideo = cv2.VideoWriter(args["output"], apiPreference=0, fourcc=fourcc,fps=120, frameSize=(int(width), int(height)))
    else:
        resizevideo = cv2.VideoWriter(args["video"]+"-resized.mp4", apiPreference=0, fourcc=fourcc,fps=120, frameSize=(int(width), int(height)))

    while True:
        ret, origframe = vs.read()
        if ret == True:
            leftframe, rightframe = decode(origframe)
            origframe = leftframe
            resizevideo.write(origframe)
        if origframe is None:
            resizevideo.release()
            break

    # close all windows
    vs.release()
else:
    print("video file path must be provided with option -v --video")
cv2.destroyAllWindows()