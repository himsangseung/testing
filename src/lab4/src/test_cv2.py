#!/usr/bin/env python
import sys
import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from matplotlib import pyplot as plt

class image_converter:

  def __init__(self):

    self.bridge = CvBridge()
    self.image_sub = rospy.Subscriber("/camera/image",Image,self.callback)

  def callback(self,data):
    try:
      cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
    except CvBridgeError as e:
      print(e)
'''    
#cv_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY) # Convert to grayscale
#cv_image = cv2.blur(cv_image,(50,50))	 # Blur image
#cv_image = cv2.Canny(cv_image,50,150)

h,w,c = cv_image.shape
#print(h,w,c)
d = 40
rows = 10
#crop_img = cv_image[(h/5)+d:(h)+(d+rows)][1:w]
crop_img = cv_image[(h/3):][1:w]
cv2.imshow("Image window", cv_image)
cv2.imshow("Image window2", crop_img)    
cv2.waitKey(3)
'''

def main(args):
  ic = image_converter()
  rospy.init_node('crop_img', anonymous=True)
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")
  cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)
