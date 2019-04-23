#include <ros/ros.h>
#include <geometry_msgs/Twist.h>
#include <sensor_msgs/LaserScan.h>
#include <nav_msgs/Odometry.h>

using namespace ros;

Subscriber lidar_sub;
Subscriber odom_sub;

Publisher vel_pub;

void lidar_callback(const sensor_msgs::LaserScan::ConstPtr& msg){

    float scan_me;
    scan_me = msg->ranges[0];
    ROS_INFO("NEW SCAN RECEIVED, dist = %f",scan_me); 
}

void odom_callback(const nav_msgs::Odometry::ConstPtr& msg){

    float x,y,z;
    x=msg->pose.pose.position.x;
    y=msg->pose.pose.position.y;
    z=msg->pose.pose.position.z;

    //ROS_INFO("Position: x= %f, y= %f, z= %f",x,y,z);

    geometry_msgs::Twist my_twist;

    my_twist.linear.x = x*y*z;
    my_twist.angular.z = -z-x;

    vel_pub.publish(my_twist);

}



int main(int argc, char **argv){

    //ROS Environment
    init(argc,argv,"test1");
    NodeHandle n;

    Rate my_rate(10);

    vel_pub = n.advertise<geometry_msgs::Twist>("/cmd_vel_1",10);

   //while (ok()){

        lidar_sub = n.subscribe("/scan",10,lidar_callback);
        odom_sub = n.subscribe("/odom",10,odom_callback);

        spin();
        my_rate.sleep();
    //} 
    return 0;
}