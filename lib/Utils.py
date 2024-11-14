import cv2
from lib.BallColors import *

def resizeWithAspectRatio(image, width=None, height=None, inter=cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]

    if width is None and height is None:
        return image
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))

    return cv2.resize(image, dim, interpolation=inter)

def GetAngle (flipImage, videofile, p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    dX = x2 - x1
    dY = y2 - y1
    rads = math.atan2 (-dY, dX)

    if flipImage == 1 and videofile == False:    	
        rads = rads*-1
    return math.degrees (rads)

def GetHLSVals(args, customhsv):
  hsvVals = yellow
  if customhsv == {}:
    if args.get("ballcolor", False):
      if args["ballcolor"] == "white":
        hsvVals = white
      elif args["ballcolor"] == "white2":
        hsvVals = white2
      elif args["ballcolor"] ==  "yellow":
        hsvVals = yellow 
      elif args["ballcolor"] ==  "yellow2":
        hsvVals = yellow2
      elif args["ballcolor"] ==  "orange":
        hsvVals = orange
      elif args["ballcolor"] ==  "orange2":
        hsvVals = orange2
      elif args["ballcolor"] ==  "orange3":
        hsvVals = orange3
      elif args["ballcolor"] ==  "orange4":
        hsvVals = orange4
      elif args["ballcolor"] ==  "green":
        hsvVals = green
      elif args["ballcolor"] ==  "green2":
        hsvVals = green2               
      elif args["ballcolor"] ==  "red":
        hsvVals = red
      elif args["ballcolor"] ==  "red2":
        hsvVals = red2
      else:
        hsvVals = yellow

      if args["ballcolor"] is not None:
        print("Ballcolor: "+str(args["ballcolor"]))
  else:
      hsvVals = customhsv
      print("Custom HSV Values being used from config.ini")
  return hsvVals
