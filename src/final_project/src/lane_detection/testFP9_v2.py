#!/usr/bin/env python

from __future__ import print_function

import roslib
#roslib.load_manifest('comp_vision')
import sys
import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image, CompressedImage
from cv_bridge import CvBridge, CvBridgeError

import numpy as np
import matplotlib.pyplot as plt
import math

# trying to merge code from testFP5_2.py witht his code
# https://stackoverflow.com/questions/51688799/ros-melodic-opencv-compressedimage-not-publishing
# Last mod 10 April 2019 8:44pm Scott Bingham
# integrating jay's line detect code to video loop
# seems to work for canny edge detection but had trouble with some of the line det functions when feeding the video image frames in

######Sub functions
def canny_ed(input_img):
    '''
    Convert RGB To Gray,
    Glassiaun Blur, and Canny Edge Detection
    '''
    img_gray = cv2.cvtColor(input_img, cv2.COLOR_RGB2GRAY)
    img_blur = cv2.GaussianBlur(img_gray, ( 5, 5), 0)
    img_canny = cv2.Canny(img_blur, 40 ,100)
    return img_canny

def region_extract(img):
    '''
    Triangle region extraction
    poly corrdinates(horizontal, vertical)
    last param (vertex of the triangle)
    '''
    h = img.shape[0]
    ##original poly
    #poly = np.array(
    #  [ [ (0, 300),(800, 300), (300, 190) ] ]
    #)

    poly = np.array(
      [ [ (0, 260),(820, 250), (290, 190) ] ]
        )


    mask = np.zeros_like(img)
    cv2.fillPoly(mask, poly, 255)
    img_mask = cv2.bitwise_and(img, mask)
    return img_mask

def line_display(imag, lines):
    '''
    create same size 'black image' array as input image
    takes in hugh
    '''
    img_line = np.zeros_like(image)
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line.reshape(4)
            cv2.line(img_line, (x1, y1), (x2, y2), (255, 0, 0), 3 )
            #B, G ,R Color and line thickness

    return img_line

def coordinates( image, param):
    '''
    Ideally takes 3/5 of the height, eliminates top portion
    get a new coordinate
    '''
    slope, intercept = param
    #print(image.shape, "shape")



    y1 = image.shape[0]
    y2= int(y1*0.4)
    x1 = int((y1 - intercept)/slope)
    x2 = int((y2 - intercept)/slope)
    return np.array([x1, y1, x2, y2])



def avg_slope(image, lines):
    '''
    setting left side lane and right side lane separate
    get poly fit to make a best fit with coordinates
    '''
    left = []
    right = []

    for line in lines:
        x1, y1, x2, y2 = line.reshape(4)
        param = np.polyfit((x1, x2), (y1, y2), 1)
        slope = param[0]
        intercept = param[1]
        if slope < 0:
            left.append((slope, intercept))
        else:
            right.append((slope, intercept))

    left_avg = np.average( left, axis = 0 )
    right_avg = np.average( right, axis = 0)
    left_line = coordinates(image, left_avg)
    right_line = coordinates(image, right_avg)
    return np.array ( [left_line, right_line])



class ImageConverter:

    def __init__(self):
        self.image_pub = rospy.Publisher("/image/compressed", CompressedImage, queue_size=1)
        self.brige = CvBridge()
        self.image_sub = rospy.Subscriber("/raspicam_node/image/compressed", CompressedImage, self.callback)

    def callback(self,data):
        try:
            cv_image = self.brige.compressed_imgmsg_to_cv2(data, "passthrough")
        except CvBridgeError as e:
            print(e)

        (rows, cols, channels) = cv_image.shape
        if cols > 60 and rows > 60:
            cv2.circle(cv_image, (50,50), 10, 255)

#        cv2.imshow("Image Window", cv_image)
#        cv2.waitKey(3)
# insert jays code
        image = cv_image
        #try:
        image_copy = np.copy(image)
           # Edge Detection using Canny E.D
        img_canny_detection = canny_ed(image_copy)
        img_region_extract = region_extract(img_canny_detection)
        lines = cv2.HoughLinesP(img_region_extract, 2, np.pi / 180, 100, np.array([]), minLineLength=40, maxLineGap=5)
        # num of pixels in the bin, 1 deg, thereshold(min), placeholder, tracd below 40 lines rejected, max distance btw pixels)

        lines_avg = avg_slope(image_copy, lines)
        img_lines = line_display(image_copy, lines)

        #img_combined = img_canny_detection
        #img_combined = img_region_extract
        img_combined = cv2.addWeighted(image_copy, 0.7, img_lines, 1, 1)
        rows, cols, ch = img_combined.shape

        #psts1 = np.float32([[155, 240], [463, 243], [0, 290], [600, 290]])
        #psts2 = np.float32([[0, 0], [640, 0], [0, 450], [640, 450]])
        #M = cv2.getPerspectiveTransform(psts1, psts2)
        #dst = cv2.warpPerspective(img_combined, M, (640, 450))
        try:
        # changed this from cv_image to img_combined
            self.image_pub.publish(self.brige.cv2_to_compressed_imgmsg(img_combined))
        except CvBridgeError as e:
            print(e)
        #except:
        #    print("error")

#end jays code



def main(args):
    ic = ImageConverter()
    rospy.init_node("image_converter", anonymous=True)
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("shutting down")
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main(sys.argv)
