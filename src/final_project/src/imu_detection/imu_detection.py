#!/usr/bin/env python 
import ros
import rospy
import sys
import rospy 
import cv2
from geometry_msgs.msg import Twist
from std_msgs.msg import String
from sensor_msgs.msg import Imu

class move():
    def __init__(self):
        self.pub = rospy.Publisher("new_message", String, queue_size = 10)
        #self.pub = rospy.Publisher("/cmd_vel",Twist, queue_size =10)
        #self.sub = rospy.Subscriber("/new_message",String,self.callback)
        self.sub = rospy.Subscriber("imu",Imu, self.callback)
        self.msg = String()
        self.speed = Twist()
        self.imu_data = Imu()

    def callback(self,data):
        if data.linear_acceleration.x > 3:
        
          self.msg = "over linear acc.x over the threshold limit of 5"
          print("over linear acc.x over the threshold limit of 5") 
            #print(self.list[3])
            #self.speed.linear.x = float (self.list[3])/100 
          self.pub.publish(self.msg)  
            #print(float (self.list[3])/100 )
            #self.pub.publish(self.speed)

        

        

def main(args):
  ic = move()
  rospy.init_node('imu_detection', anonymous=True)
  try:
      rospy.spin()
  
  except KeyboardInterrupt:
    print("Shutting down")
  cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)
