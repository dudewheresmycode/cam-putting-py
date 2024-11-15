import argparse
from configparser import ConfigParser

parser = ConfigParser()

def ParseArguments():
  ap = argparse.ArgumentParser()
  ap.add_argument("-v", "--video",
                  help="path to the (optional) video file")
  ap.add_argument("-i", "--img",
                  help="path to the (optional) image file")
  ap.add_argument("-b", "--buffer", type=int, default=64,
                  help="max buffer size - default is 64")
  ap.add_argument("-w", "--camera", type=int, default=0,
                  help="webcam index number - default is 0")
  ap.add_argument("-c", "--ballcolor",
                  help="ball color - default is yellow")
  ap.add_argument("-d", "--debug",
                  help="debug - color finder and wait timer")
  ap.add_argument("-t", "--top",
                  help="make window always on top")
  ap.add_argument("-r", "--resize", type=int, default=360,
                  help="window resize width (in pixels) - default is 360px")
  ap.add_argument("-x", "--xpos", type=int, default=40,
                  help="window x position (in pixels) - default is 40px")
  ap.add_argument("-y", "--ypos", type=int, default=40,
                  help="window y position (in pixels) - default is 40px")
  ap.add_argument("-f", "--frameless",
                  help="Use a frameless always-on-top window")
  ap.add_argument("-g", "--config",
                  help="The config file to use")

  args = vars(ap.parse_args())
  return args

def ParseConfigFile(configFile):  
  parser.read(configFile)
  config = {}

  if parser.has_option('putting', 'startx1'):
      sx1=int(parser.get('putting', 'startx1'))
  else:
      sx1=10
  if parser.has_option('putting', 'startx2'):
      sx2=int(parser.get('putting', 'startx2'))
  else:
      sx2=180
  if parser.has_option('putting', 'y1'):
      y1=int(parser.get('putting', 'y1'))
  else:
      y1=180
  if parser.has_option('putting', 'y2'):
      y2=int(parser.get('putting', 'y2'))
  else:
      y2=450
  if parser.has_option('putting', 'radius'):
      ballradius=int(parser.get('putting', 'radius'))
  else:
      ballradius=0
  if parser.has_option('putting', 'flip'):
      flipImage=int(parser.get('putting', 'flip'))
  else:
      flipImage=0
  if parser.has_option('putting', 'flipview'):
      flipView=int(parser.get('putting', 'flipview'))
  else:
      flipView=0
  if parser.has_option('putting', 'darkness'):
      darkness=int(parser.get('putting', 'darkness'))
  else:
      darkness=0
  if parser.has_option('putting', 'mjpeg'):
      mjpegenabled=int(parser.get('putting', 'mjpeg'))
  else:
      mjpegenabled=0
  if parser.has_option('putting', 'ps4'):
      ps4=int(parser.get('putting', 'ps4'))
  else:
      ps4=0
  if parser.has_option('putting', 'fps'):
      overwriteFPS=int(parser.get('putting', 'fps'))
  else:
      overwriteFPS=0
  if parser.has_option('putting', 'height'):
      height=int(parser.get('putting', 'height'))
  else:
      height=360
  if parser.has_option('putting', 'width'):
      width=int(parser.get('putting', 'width'))
  else:
      width=640
  if parser.has_option('putting', 'customhsv'):
      customhsv=ast.literal_eval(parser.get('putting', 'customhsv'))
      print(customhsv)
  else:
      customhsv={}
  if parser.has_option('putting', 'showreplay'):
      showreplay=int(parser.get('putting', 'showreplay'))
  else:
      showreplay=0
  if parser.has_option('putting', 'replaycam'):
      replaycam=int(parser.get('putting', 'replaycam'))
  else:
      replaycam=0
  if parser.has_option('putting', 'replaycamindex'):
      replaycamindex=int(parser.get('putting', 'replaycamindex'))
  else:
      replaycamindex=0
  if parser.has_option('putting', 'replaycamps4'):
      replaycamps4=int(parser.get('putting', 'replaycamps4'))
  else:
      replaycamps4=0

  return (
    sx1,
    sx2,
    y1,
    y2,
    ballradius,
    flipImage,
    flipView,
    darkness,
    mjpegenabled,
    ps4,
    overwriteFPS,
    height,
    width,
    customhsv,
    showreplay,
    replaycam,
    replaycamindex,
    replaycamps4,
    parser
  )


def setXStart(value):
    print(value)
    startcoord[0][0]=value
    startcoord[2][0]=value

    global sx1
    sx1=int(value)    
    parser.set('putting', 'startx1', str(sx1))
    parser.write(open(CFG_FILE, "w"))
    pass

def setXEnd(value):
    print(value)
    startcoord[1][0]=value
    startcoord[3][0]=value 

    global x1
    global x2
    global sx2
     
    # Detection Gateway
    x1=int(value+10)
    x2=int(x1+10)

    #coord=[[x1,y1],[x2,y1],[x1,y2],[x2,y2]]
    coord[0][0]=x1
    coord[2][0]=x1
    coord[1][0]=x2
    coord[3][0]=x2

    sx2=int(value)    
    parser.set('putting', 'startx2', str(sx2))
    parser.write(open(CFG_FILE, "w"))
    pass  

def setYStart(value):
    print(value)
    startcoord[0][1]=value
    startcoord[1][1]=value

    global y1

    #coord=[[x1,y1],[x2,y1],[x1,y2],[x2,y2]]
    coord[0][1]=value   
    coord[1][1]=value

    y1=int(value)    
    parser.set('putting', 'y1', str(y1))
    parser.write(open(CFG_FILE, "w"))     
    pass


def setYEnd(value):
    print(value)
    startcoord[2][1]=value
    startcoord[3][1]=value 

    global y2

    #coord=[[x1,y1],[x2,y1],[x1,y2],[x2,y2]]
    coord[2][1]=value   
    coord[3][1]=value

    y2=int(value)    
    parser.set('putting', 'y2', str(y2))
    parser.write(open(CFG_FILE, "w"))     
    pass 

def setBallRadius(value):
    print(value)    
    global ballradius
    ballradius = int(value)
    parser.set('putting', 'radius', str(ballradius))
    parser.write(open(CFG_FILE, "w"))
    pass

def setFlip(value):
    print(value)    
    global flipImage
    flipImage = int(value)
    parser.set('putting', 'flip', str(flipImage))
    parser.write(open(CFG_FILE, "w"))
    pass

def setFlipView(value):
    print(value)    
    global flipView
    flipView = int(value)
    parser.set('putting', 'flipView', str(flipView))
    parser.write(open(CFG_FILE, "w"))
    pass

def setMjpeg(valu, vs):
    print(value)    
    global mjpegenabled
    global message
    if mjpegenabled != int(value):
        vs.release()
        message = "Video Codec changed - Please restart the putting app"
    mjpegenabled = int(value)
    parser.set('putting', 'mjpeg', str(mjpegenabled))
    parser.write(open(CFG_FILE, "w"))
    pass

def setOverwriteFPS(value, vs):
    print(value)    
    global overwriteFPS
    global message
    if overwriteFPS != int(value):
        vs.release()
        message = "Overwrite of FPS changed - Please restart the putting app"
    overwriteFPS = int(value)
    parser.set('putting', 'fps', str(overwriteFPS))
    parser.write(open(CFG_FILE, "w"))
    pass

def setDarkness(value):
    print(value)    
    global darkness
    darkness = int(value)
    parser.set('putting', 'darkness', str(darkness))
    parser.write(open(CFG_FILE, "w"))
    pass