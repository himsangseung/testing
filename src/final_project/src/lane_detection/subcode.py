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
import csv
import time
import matplotlib.pyplot as plt
import math

# trying to merge code from testFP5_2.py witht his code
# https://stackoverflow.com/questions/51688799/ros-melodic-opencv-compressedimage-not-publishing
# Last mod 11 April 2019 12:00am Scott Bingham, Jay Lee
# Initial version integrates Jay's line detect code to video loop subscribe and publish -Scott
# Resetting region extract parameters 10 April 11:00pm - Jay Lee
# Fixed perspective 
 and now published with no issue 10 April 11:35pm -Jay Lee
# v6 fixed bugs resulting from uninitialized variables in the case of no lines detected in avg_slope function 11 April 19 08:46pm -Scott
# v7 Trying to "hold" lines for a few cycles.  See demo upload of v7 code displaying average lines on each side.  At end of lane, the code picks up "cross line" on right, but otherwise behavior seemed pretty stable and useful as is. 11 April 10 9:30pm -Scott
# v8 Experimenting with hold lines.  Works pretty well but needs some logic for discarding.
#  adding code to export data to CSV in this version for analysis of patterns.
# added circles tracking center of robot image (blue) versus center of lane (red). 13 April 2019 5:43p
# v10 adding commands to indicate a suggested right or left turn, or to maintain course
#  last mod scott 4/13/19 8:10p
# v11 adding offset px to in conversion - scott 14 Apr 2019 9:37am


FOUND_RIGHT_LINE = 0
FOUND_LEFT_LINE = 0
LAST_RIGHT_LINE = (0, 0, 0, 0)
LAST_LEFT_LINE = (0, 0, 0, 0)
LAST_LINES_AVG = (0, 0, 0, 0)
FOUND_LAST_LINES_AVG = 0
CENTER_LANE_X = 0.0
PX_PER_IN_AT_CAM = 55.3884354693


DATA_FILENAME = "slopesAndOffsets.csv"



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

    poly = np.array(
          [ [ (0, 260),(820, 250), (290, 190) ] ]
            )


    mask = np.zeros_like(img)
    cv2.fillPoly(mask, poly, 255)
    img_mask = cv2.bitwise_and(img, mask)
    return img_mask

def line_display(image, lines):
    '''
    create same size 'black image' array as input image
    takes in hugh
    '''
    img_line = np.zeros_like(image)
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line.reshape(4)
            #print("x1,y1,x2,y2: " + str(x1) + ", " + str(y1) + ", " + str(x2) + ", " + str(y2))
            cv2.line(img_line, (x1, y1), (x2, y2), (255, 0, 0), 3 )
            #print("[x1,y1],[x2,y2] : ")
            #print(line)
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

    PRINT_LINES = 0
    left = []
    right = []
    global FOUND_LEFT_LINE
    global FOUND_RIGHT_LINE
    global LAST_LEFT_LINE
    global LAST_RIGHT_LINE
    global CENTER_LANE_X
    x1 = 0.0
    x2 = 0.0
    x1_x2_avg = 0.0

    epochTime = time.time()

    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line.reshape(4)
            if (PRINT_LINES):
                print("x1, y1, x2, y2: " + str(x1) + ", " + str(y1) + ", " + str(x2) + ", " + str(y2))
            param = np.polyfit((x1, x2), (y1, y2), 1) # added - sign
            #print("param: ", str(param))
            slope = param[0]
            intercept = param[1]
            if slope < 0:
                left.append((slope, intercept))
            else:
                right.append((slope, intercept))
                # this line should be removed once we figure out how to initialize both arrays or handle a null return for left or right line
                #left.append((slope, intercept))
    if len(left) > 0:
        left_avg = np.average( left, axis = 0 )
        #print("left avg: " + str(left_avg))
        m, b = left_avg
        x1 = (480-b)/m  # changed from -b/m
        print("x1: " + str(x1))
        with open(DATA_FILENAME, 'a') as f:
            writer = csv.writer(f, delimiter=",")
            row = []
            row.append(epochTime)
            for cell in left_avg:
                row.append(cell)
            row.append("LeftAvg")
            writer.writerow(row)
            #print(epochTime)
            #writer.writerow(epochTime)
        left_line = coordinates(image, left_avg)
        FOUND_LEFT_LINE = 1
        LAST_LEFT_LINE = left_line
        #print("Left Line:")
        #print(left_line)
    else:
        if FOUND_LEFT_LINE < 100:
            left_line = LAST_LEFT_LINE
        else:
            left_line = (0, 0, 0, 0)
        FOUND_LEFT_LINE += 1
    if len(right) > 0:
        right_avg = np.average( right, axis = 0)
        #print("right avg: " + str(right_avg))
        m, b = right_avg
        x2 = (480-b)/m  # changed from -b/m
        print("x2: " + str(x2))
        with open(DATA_FILENAME, 'a') as f:
            writer = csv.writer(f, delimiter=",")
            row = []
            row.append(epochTime)
            for cell in right_avg:
                row.append(cell)
            row.append("RightAvg")
            writer.writerow(row)
            #print(epochTime)
        right_line = coordinates(image, right_avg)
        FOUND_RIGHT_LINE = 1
        LAST_RIGHT_LINE = right_line
        #print("Right Line:")
        #print(right_line)
    else:
        if FOUND_RIGHT_LINE < 100:
            right_line = LAST_RIGHT_LINE
            FOUND_RIGHT_LINE += 1
        else:
            right_line = (0, 0, 0, 0)
    if x1 != 0 and x2 != 0:
        x1_x2_avg = (x2-x1)/2 + x1
        CENTER_LANE_X = x1_x2_avg
        print("x1_x2_avg: " + str(x1_x2_avg))
    error_x_threshold = 1.8 # changed from 100 [px] to 1.8 [in]
    error_x = x1_x2_avg - 320
    error_x_in = error_x / PX_PER_IN_AT_CAM
    moveMsg = "Undefined"
    if error_x_in > error_x_threshold:
        moveMsg = "Move Right."
    if error_x_in < -error_x_threshold:
        moveMsg = "Move Left."
    if abs(error_x_in) <= error_x_threshold:
        moveMsg = "Maintain Course."
    print(moveMsg)
    print("error x [in]: " + str(error_x_in))
    print("error x [px]: " + str(error_x))
    with open(DATA_FILENAME, 'a') as f:
        writer = csv.writer(f, delimiter=",")
        row = []
        row.append(epochTime)
        row.append(error_x_in)
        row.append(moveMsg)
        writer.writerow(row)
    # replaced left hand param here from "left_line" to "right_line"
    return np.array([left_line, right_line])



class ImageConverter:

    def __init__(self):

        self.brige = CvBridge()
        self.brige2 = CvBridge()
        self.image_pub = rospy.Publisher("/image/compressed2", CompressedImage, queue_size=1)
        self.top_image_pub = rospy.Publisher("/top_image/compressed", CompressedImage, queue_size=1)
        #self.image_pub2 = rospy.Publisher("/image/compressed2", CompressedImage, queue_size=1)

        self.image_sub = rospy.Subscriber("/raspicam_node/image/compressed", CompressedImage, self.callback)

    def callback(self,data):
        try:
            cv_image = self.brige.compressed_imgmsg_to_cv2(data, "passthrough")
        except CvBridgeError as e:
            print(e)

        (rows, cols, channels) = cv_image.shape
        if cols > 60 and rows > 60:
            #cv2.circle(cv_image, (50,50), 10, 255)
            # print center of lane line bisector angle average intersection
            if CENTER_LANE_X <= 640 and CENTER_LANE_X>= 0:
                cv2.circle(cv_image, (int(CENTER_LANE_X), 480), 20, (0, 0, 255))
            elif CENTER_LANE_X > 640:
                cv2.circle(cv_image, (640, 480), 20, (0, 0, 255))
            elif CENTER_LANE_X < 0:
                cv2.circle(cv_image, (0, 480), 20, (0, 0, 255))
            # print target
            cv2.circle(cv_image, (int(640/2), 480), 20, (255, 0, 0))
# insert jays code
        global LAST_LINES_AVG
        image = cv_image
        #try:
        image_copy = np.copy(image)
        img_combined = image_copy
           # Edge Detection using Canny E.D
        img_canny_detection = canny_ed(image_copy)
        img_region_extract = region_extract(img_canny_detection)
        img_combined = img_canny_detection

        try:
        # changed this from cv_image to img_combined
            self.image_pub.publish(self.brige.cv2_to_compressed_imgmsg(img_combined))
           # self.top_image_pub.publish(self.brige.cv2_to_compressed_imgmsg(dst))
            #self.image_pub.publish(self.brige.cv2_to_compressed_imgmsg(dst))
            #self.image_pub2.publish(CvBridge().cv2_to_compressed_imgmsg(dst))
        except CvBridgeError as e:
            print(e)

#end jays code



def main(args):
    with open(DATA_FILENAME, 'a') as f:
        writer = csv.writer(f, delimiter=",")
        writer.writerow(["Time", "Slope", "Offset", "LineType"])

    ic = ImageConverter()
    rospy.init_node("image_converter", anonymous=True)
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("shutting down")
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main(sys.argv)
