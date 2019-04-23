#!/usr/bin/env python
import sys
import rospy
import cv2
from sensor_msgs.msg import CompressedImage
from cv_bridge import CvBridge, CvBridgeError
import numpy as np
# Original code was provided with ECE491 course materials (test_cv.py).
# New code file: test_cv_mod2.py
# Modification Author: Scott Bingham ("new code" section)
# Last modified: 12 Feb. 2019 10:45.
#
# The following reference was found to be useful in developing the
# modification on 10 Feb. 2019 17:32. "OpenCV Threshold (Python, C++)"
# by Mallick. https://www.learnopencv.com/opencv-threshold-python-cpp/

class image_converter:

  def __init__(self):

    self.bridge = CvBridge()
    self.image_sub = rospy.Subscriber("/camera/image",CompressedImage,self.callback)

  def callback(self,data):
    try:
      cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
    except CvBridgeError as e:
      print(e)


    cv_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY) # Convert to grayscale
    cv_image = cv2.blur(cv_image,(5,5))	 # Blur image
#    cv_image = cv2.Canny(cv_image,50,150)

# begin new code (followed a reference given in script heading)
    thresholdVal = 200 #values below thresholdVal will be set to black
    maxVal = 255 #values above thresholdVal will be set to white
    th, modImg = cv2.threshold(cv_image, thresholdVal, maxVal, cv2.THRESH_BINARY);
    cv2.imshow("Image window", modImg)
# end new code

#    cv2.imshow("Image window", cv_image)
    cv2.waitKey(3)





def main(args):
  ic = image_converter()
  rospy.init_node('test_cv', anonymous=True)
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")
  cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)
