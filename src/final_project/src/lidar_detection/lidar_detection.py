#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

class lidar_detection():
    def laserCallback(self, msg):
      
        if msg.ranges[180] < self.look_ahead_dist:
  
            self.twistCmd.linear.x = 0.0
            self.twistCmd.angular.z = 0.0
            self.pubObj.publish(self.twistCmd)
        
    def __init__(self):
        sub = rospy.Subscriber('scan', LaserScan, self.laserCallback)
        self.pubObj = rospy.Publisher("cmd_vel", Twist, queue_size=1)
        self.twistCmd = Twist()
        self.look_ahead_dist = 2
  
if __name__ == '__main__':
    try:
        rospy.init_node('lidar_detection', anonymous=True)
        lidar_detection()
        rospy.spin()
      
    except RuntimeError as e:
        pass
