import cv2

def SetupVideoSource(webcamindex, ps4, mjpegenabled, overwriteFPS, width, height):
  # if a video path was not supplied, grab the reference
  # to the webcam
  if mjpegenabled == 0:
    vs = cv2.VideoCapture(webcamindex)
  else:
    vs = cv2.VideoCapture(webcamindex + cv2.CAP_DSHOW)
    # Check if FPS is overwritten in config
    if overwriteFPS != 0:
      vs.set(cv2.CAP_PROP_FPS, overwriteFPS)
      print("Overwrite FPS: "+str(vs.get(cv2.CAP_PROP_FPS)))
    if height != 0 and width != 0:
      vs.set(cv2.CAP_PROP_FRAME_WIDTH, width)
      vs.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    mjpeg = cv2.VideoWriter_fourcc('M','J','P','G')
    vs.set(cv2.CAP_PROP_FOURCC, mjpeg)
  if vs.get(cv2.CAP_PROP_BACKEND) == -1:
    # message = "No Camera could be opened at webcamera index "+str(webcamindex)+". If your webcam only supports compressed format MJPEG instead of YUY2 please set MJPEG option to 1"
    print("No Camera could be opened at webcamera index "+str(webcamindex)+". If your webcam only supports compressed format MJPEG instead of YUY2 please set MJPEG option to 1")
  else:
    if ps4 == 1:
      vs.set(cv2.CAP_PROP_FPS, 120)
      vs.set(cv2.CAP_PROP_FRAME_WIDTH, 1724)
      vs.set(cv2.CAP_PROP_FRAME_HEIGHT, 404)
    print("Backend: "+str(vs.get(cv2.CAP_PROP_BACKEND)))
    print("FourCC: "+str(vs.get(cv2.CAP_PROP_FOURCC)))
    print("FPS: "+str(vs.get(cv2.CAP_PROP_FPS)))
  return vs

def SetVideoFPS(vs, video_fps):  
  if type(video_fps) == float:
      if video_fps == 0.0:
          e = vs.set(cv2.CAP_PROP_FPS, 60)
          new_fps = []
          new_fps.append(0)

      if video_fps > 0.0:
          new_fps = []
          new_fps.append(video_fps)
      video_fps = new_fps
  return video_fps

  def Decode(myframe):
    left = np.zeros((400,632,3), np.uint8)
    right = np.zeros((400,632,3), np.uint8)
    
    for i in range(400):
        left[i] = myframe[i, 32: 640 + 24] 
        right[i] = myframe[i, 640 + 24: 640 + 24 + 632] 
    
    return (left, right)

def setFPS(vs, value):
    print(value)
    vs.set(cv2.CAP_PROP_FPS,value)
    pass 


# def rgb2yuv(rgb):
#     m = np.array([
#         [0.29900, -0.147108,  0.614777],
#         [0.58700, -0.288804, -0.514799],
#         [0.11400,  0.435912, -0.099978]
#     ])
#     yuv = np.dot(rgb, m)
#     yuv[:,:,1:] += 0.5
#     return yuv

# def yuv2rgb(yuv):
#     m = np.array([
#         [1.000,  1.000, 1.000],
#         [0.000, -0.394, 2.032],
#         [1.140, -0.581, 0.000],
#     ])
#     yuv[:, :, 1:] -= 0.5
#     rgb = np.dot(yuv, m)
#     return rgb