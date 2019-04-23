#!/usr/bin/env python

import rospy
from sensor_msgs.msg import PointCloud2, PointField
import sensor_msgs.point_cloud2 as pc2
from std_msgs.msg import String

class lab_1_node():
  def __init__(self):
    self.pcl_sub = rospy.Subscriber('/points_raw', PointCloud2, self.pointcloud_callback)
    self.pcl_pub = rospy.Publisher('/points_modified', PointCloud2, queue_size=2)

  def pointcloud_callback(self, msg):
    points = []
    field_names = ('x', 'y', 'z', 'intensity')
    for p in pc2.read_points(msg, field_names = field_names, skip_nans=True):
      if p[0] >= 0:
        points.append(p)
    fields = [PointField('x', 0, PointField.FLOAT32,1),
              PointField('y', 4, PointField.FLOAT32,1),
              PointField('z', 8, PointField.FLOAT32,1),
              PointField('intensity', 12, PointField.UINT32,1),]
    output = pc2.create_cloud(msg.header, fields, points)
    self.pcl_pub.publish(output);

if __name__ == '__main__':
  try:
    rospy.init_node('lab1_py_node', anonymous=True)
    lab_1_node()
    rospy.spin()
  except RuntimeError as e:
    pass
