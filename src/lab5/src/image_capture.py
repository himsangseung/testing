#!/usr/bin/env python 
import ros
import sys
import rospy 
import cv2
from sensor_msgs.msg import Image
#from sensor_msgs import CompressedImage
from cv_bridge import CvBridge, CvBridgeError
from matplotlib import pyplot as plt

import pytesseract
from PIL import Image 
from std_msgs.msg import String


#huff transform -detect arrow --(direction is poiniting ) center of mass -- semgementation ->grid what is each grid
class image_converter:

  def __init__(self):
  
    self.bridge = CvBridge()
    #self.image_sub = rospy.Subscriber("/camera/image",Image,self.callback)
    self.image_sub = rospy.Subscriber("/raspicam_node/image/compressed",Image,self.callback)
  
  def callback(self,data):
    try:
      cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
      cv2.imwrite('camera_image.jpeg',cv_image)      

    except CvBridgeError as e:
      print(e)

	
def main(args):
  ic = image_converter()
  rospy.init_node('test_cv', anonymous=True)
  try:
      pass

  except KeyboardInterrupt:
    print("Shutting down")
  cv2.destroyAllWindows()  
    

if __name__ == '__main__':
    main(sys.argv)