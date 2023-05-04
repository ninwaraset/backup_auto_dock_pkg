#!/usr/bin/python3
import rclpy
from rclpy.node import Node
import matplotlib.pyplot as plt
from std_msgs.msg import Float32

from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
import math
class PathP(Node):

    def __init__(self):
        super().__init__('path')
        self.subscription1 = self.create_subscription(
            Odometry,
            '/odom',
            self.listener_callback,
            10)
        
        self.subscription2 = self.create_subscription(
            Float32,
            '/finish_plot',
            self.listener_callback2,
            10)
        
        # self.subscription  # prevent unused variable warning
        self.xy = [0,0]
        self.x = 0.0
        self.y = 0.0
        time_period_1 = 0.2
        self.timer_1 = self.create_timer(time_period_1,self.timer_1_callback)
        
        self.key = 0.0
        self.color = ["pink","red","orange","brown","blue","green","yellow","cyan"]
        self.zxc = 0
        fig, ( self.ax1, self.ax2) = plt.subplots(1,2)
        self.ax1.set_title('real odometry')
        self.ax2.set_title('odometry')

    def listener_callback(self, msg):
        
        # print(msg.pose)
        print("positoin x: "+str(msg.pose.pose.position.x))
        print("positoin y: "+str(msg.pose.pose.position.y)) 
        print("orientation z: "+str(msg.pose.pose.orientation.z))
        print("-----")
        self.xy = ((msg.pose.pose.position.x),(msg.pose.pose.position.y))
        self.x = (msg.pose.pose.position.x)
        self.y = msg.pose.pose.position.y
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
        self.key = msg.data
    
    def timer_1_callback(self):
        # plt.plot(self.xy,"r.")
        self.zxc += 1 
        print(self.zxc)
        theta = -5 *(math.pi/180)
        x_bar = self.x*math.cos(theta) -self.y*math.sin(theta)
        y_bar = self.x*math.sin(theta)+ self.y*math.sin(theta)
        self.ax2.plot(x_bar,y_bar,color=self.color[int(self.key)-1],marker ="1")
        self.ax1.plot(self.x,self.y,"kx")
        if self.key == 7:
            plt.show()
        if self.zxc == 100 : plt.show()

def main(args=None):
    rclpy.init(args=args)

    subscriber = PathP()

    rclpy.spin(subscriber)

    subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

