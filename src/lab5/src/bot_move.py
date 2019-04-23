#!/usr/bin/env python 
import ros
import rospy
import sys
import rospy 
import cv2
from geometry_msgs.msg import Twist
from std_msgs.msg import String

class move():
    def __init__(self):
        self.pub = rospy.Publisher("/cmd_vel",Twist, queue_size =10)
        self.sub = rospy.Subscriber("/new_message",String,self.callback)
        self.msg = ""
        self.list = []
        self.speed = Twist()

    def callback(self,data):
        self.list = data.data.split('\n')
        if self.list[3].isdigit():
            #print(self.list[3])
            self.speed.linear.x = float (self.list[3])/100 
              
            #print(float (self.list[3])/100 )
            self.pub.publish(self.speed)

        

        

def main(args):
  ic = move()
  rospy.init_node('test_cv', anonymous=True)
  try:
      rospy.spin()
  
  except KeyboardInterrupt:
    print("Shutting down")
  cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)
