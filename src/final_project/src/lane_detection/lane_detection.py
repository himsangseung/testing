#!/usr/bin/env python
#X-491 Final Project
#Lane Detection Algorithm for image or video file
#Modified by Jay Lee 3/31/19
#Rererencees:
#https://www.youtube.com/watch?v=eLTLtUVuuy4
#https://medium.com/@mrhwick/simple-lane-detection-with-opencv-bfeb6ae54ec0
import cv2
import numpy as np
import matplotlib.pyplot as plt
import math

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
      [ [ (0, 300),(800, 300), (300, 190) ] ]
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

    if lines is not None:
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


#########if image input

image = cv2.imread('image.png')
image_copy = np.copy(image)
#Edge Detection using Canny E.D
img_canny_detection = canny_ed(image_copy)
img_region_extract = region_extract(img_canny_detection)


lines = cv2.HoughLinesP(img_region_extract, 2, np.pi/180, 100, np.array([]), minLineLength = 40, maxLineGap = 5 )
# num of pixels in the bin, 1 deg, thereshold(min), placeholder, tracd below 40 lines rejected, max distance btw pixels)

lines_avg = avg_slope(image_copy, lines)
img_lines = line_display(image_copy, lines)
#img_lines = line_display(image_copy, lines_avg)

img_combined = cv2.addWeighted(image_copy, 0.7, img_lines, 1, 1)
plt.imshow(img_combined)
plt.show()
#plt.waitKey(0)

'''
img = cv2.imread('image.png')
rows, cols, ch = img.shape
'''

rows, cols, ch = img_combined.shape
#https://docs.opencv.org/3.4/da/d6e/tutorial_py_geometric_transformations.html

psts1 = np.float32 ( [ [155, 240], [463, 243],[0,290], [600, 290]  ] )
psts2 = np.float32 ( [[0, 0], [640, 0 ], [0, 450], [640, 450] ] )

M = cv2.getPerspectiveTransform( psts1, psts2 )
dst = cv2.warpPerspective (img_combined, M, (640,450) )

#plt.subplot(121), plt.imshow(img), plt.title('input')
#plt.subplot(122), plt.imshow(dst), plt.title('output')
#plt.imshow(img_combined)
#plt.show()
plt.imshow(dst)
plt.show()
#plt.show()

'''
#########video
cap = cv2.VideoCapture("some _name")
while (cap.isOpened()):
    _, frame = cap.read()
    img_canny_detection = canny_ed(frame)
    img_region_extract = region_extract(img_canny_detection)
    lines = cv2.HoughLinesP(img_region_extract, 2, np.pi/180, 100, np.array([]), minLineLength = 40, maxLineGap = 5 )

    lines_avg = avg_slope(frame, lines)

    #img_lines = line_display(frame, lines)
    img_lines = line_display(frame, lines_avg)
    img_combined = cv2.addWeighted(frame, 0.7, img_lines, 1, 1)
    #cv2.imshow("now", img_combined)
    if cv2.waitKey(1) == ord('q'):
        break
'''
