#!/usr/bin/python3
import rclpy
from rclpy.node import Node
import matplotlib.pyplot as plt
from std_msgs.msg import Float32

from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
import math

class SubscriberClass(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(
            Odometry,
            '/odom',
            self.listener_callback,
            10)
        
        self.subscription = self.create_subscription(
            Float32,
            '/finish_plot',
            self.listener_callback2,
            10)
        
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        # print(msg.pose)
        print("positoin x: "+str(msg.pose.pose.position.x))
        print("positoin y: "+str(msg.pose.pose.position.y)) 
        print("orientation z: "+str(msg.pose.pose.orientation.z))
        print("-----")
        plt.plot((msg.pose.pose.position.x),(msg.pose.pose.position.y))
        # print("x-z",msg.pose.pose.position.x-msg.pose.pose.orientation.z)
        # print("y-z",msg.pose.pose.position.y-msg.pose.pose.orientation.z)
        
        # print("=====")
        
        # print(msg.twist.twislt)
        
        # pose_odom = msg.data.pose.pose
        # twist_odom = msg.data.twist.twist
        # print(pose_odom)
        # print(twist_odom)
    def listener_callback2(self, msg):
        print(msg)
    

def main(args=None):
    rclpy.init(args=args)

    subscriber = SubscriberClass()

    rclpy.spin(subscriber)

    subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

