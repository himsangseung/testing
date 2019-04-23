#!/usr/bin/env python 
import ros
import sys
import rospy 
import cv2
from sensor_msgs.msg import Image
#from sensor_msgs/CompressedImage
from cv_bridge import CvBridge, CvBridgeError
from matplotlib import pyplot as plt

import pytesseract
from PIL import Image 
from std_msgs.msg import String


#huff transform -detect arrow --(direction is poiniting ) center of mass -- semgementation ->grid what is each grid
#
class image_converter:

  def __init__(self):
  
    self.bridge = CvBridge()
    self.stringpub = rospy.Publisher('new_message',String, queue_size =10)
    self.string_data = ""
  #  self.image_sub = rospy.Subscriber("/camera/image",Image,self.callback)
    #self.image_sub = rospy.Subscriber("/raspicam_node/image/compressed",Image,self.callback)
  '''
  def callback(self,data):
    try:
      print("runs")
      cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
      #print("runs")
      #cv2.imwrite('camera_image.jpeg',cv_image)      
    
 
      # Set threshold and maxValue
      #thresh = 0
      #maxValue = 255
      # Basic threshold example
      #th, dst = cv2.threshold(src, thresh, maxValue, cv2.THRESH_BINARY)
  
    except CvBridgeError as e:
      print(e)
    #print('sub')
    #imshow("cam",cv_image)
  '''
  '''   
    cv_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY) # Convert to grayscale
    cv_image = cv2.blur(cv_image,(50,50))	 # Blur image
    cv_image = cv2.Canny(cv_image,50,150)

    cv2.imshow("Image window", cv_image)
   
    cv2.waitKey(3)
  '''
	
def main(args):
  ic = image_converter()
  rospy.init_node('test_cv', anonymous=True)
  try:

    '''

    if not 'new_file.pg':
    #src = cv2.imread("image_cam_image.png", cv2.IMREAD_GRAYSCALE)
    src = cv2.imread("image_cam_image.png", cv2.IMREAD_COLOR)
    #src = cv2.imread("chess.jpg", cv2.IMREAD_COLOR)
    #src = cv2.imread('image_cam_image.png', 0)
    #src1 = cv2.
    cv2.imshow("Image window", src) 
    cv2.waitKey()
    #rospy.spin()

    height, width = src.shape[:2]
    x = height
    y = width
    if height % 32 != 0:
      x = height -height%32
    if width % 32 !=0:
      y = width - height %32
    #print(x,y)

    resized = src[0:x, 0:y]
    cv2.imshow("r2",resized)
    cv2.waitKey()

    cv2.imwrite("new_file.png",resized)
    ''' 
    #src = cv2.imread("large.jpg")#oh ok tested ok with thres 190 or 100
    #src = cv2.imread("stop_sign2.jpg") #tested ok truncated stop with thres 190 or 100
    #src = cv2.imread("image_cam_image.png") #tested okay with thres 190
    src = cv2.imread("speed_limit2.jpg")# tested okay with 213
    #src = cv2.imread("text.jpg")# tested okay with 190
    height, width = src.shape[:2]
    x = height
    y = width
    if height % 32 != 0:
      x = height -height%32
    if width % 32 !=0:
      y = width - height %32
    resized = src[0:x, 0:y]
#    cv2.imshow("r2",resized)
#    cv2.waitKey()

    #text = pytesseract.image_to_string(Image.open('new_file.png'))
    #cv2.imwrite("new_file_gray.png",sr c)
    #cv2.waitKey()
    resized = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)#chgd src to resized 1:02p 2/18
#    cv2.imshow("new",resized)
#    cv2.waitKey()  

    threshold_val = 213     # values below thresholdvalue in script heading   CHG 100 - 50 1:40p 
    max_val = 255 #values above thresholdVal will be set to white 255-> 100

    th, modimg = cv2.threshold(resized,threshold_val, max_val, cv2.THRESH_BINARY)#chgd src to resized 1:02p 2/18
    modimg = cv2.blur(modimg,(3,5))
    #modimg = ~modimg
#    modimg = resized
#    modimg = ~modimg
    cv2.imshow("threshold_image",modimg)
    cv2.waitKey(2)

    text = str( pytesseract.image_to_string(modimg, lang="eng") )#chgd src to resized 1:02p 2/18
    print text
    #text = "helllllooo world"
    cv2.waitKey(2)
    #print(text)
    while not rospy.is_shutdown():
      #print(type(text))
      
      #ic.stringpub.publish(text)
      ic.string_data = text
      print text

      ic.stringpub.publish(ic.string_data)
      rospy.sleep(1)
    #rospy.spin()

  except KeyboardInterrupt:
    print("Shutting down")
  cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)
