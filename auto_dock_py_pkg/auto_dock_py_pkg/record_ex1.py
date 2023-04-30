#!/usr/bin/python3
import rclpy
from rclpy.node import Node
import matplotlib.pyplot as plt
from std_msgs.msg import Float32

from geometry_msgs.msg import Twist,PoseStamped
from nav_msgs.msg import Odometry

class SubscriberClass(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        
        self.subscription_1 = self.create_subscription(PoseStamped,'/aruco_pose',self.listener_callback_1,10)
        self.subscription_2 = self.create_subscription(PoseStamped,'/pose_vertrex',self.listener_callback_2,10)
        self.subscription_3 = self.create_subscription(Float32,'/vertex_distance',self.listener_callback_3,10)
        self.subscription_4 = self.create_subscription(Float32,'/vertex_theta',self.listener_callback_4,10)
        # self.subscription_5 = self.create_subscription(Float32,'/blue_distance',self.listener_callback_5,10)
        # self.subscription_6 = self.create_subscription(Float32,'/blue_theta',self.listener_callback_6,10)
        self.subscription7 = self.create_subscription(
            Float32,
            '/finish_plot',
            self.listener_callback_7,
            10)
        self.subscription8 = self.create_subscription(
            Float32,
            '/time_work',
            self.listener_callback_8,
            10)
        
        self.aruco_x = 0.0
        self.aruco_y = 0.0
        self.aruco_z = 0.0
        
        self.pose_vertex_x = 0.0
        self.pose_vertex_y = 0.0
        
        self.vertex_distance = 0.0
        self.vertex_theta = 0.0
        
        time_period_1 = 0.1
        self.timer_1 = self.create_timer(time_period_1,self.timer_1_callback)
        
        self.time_work = 0.0
        self.key_move = 0.0
        # self.subscription  # prevent unused variable warning

    def listener_callback_1(self, msg):
        # print(str(msg.pose.position.x))
        # print(str(msg.pose.position.y))
        # print(str(msg.pose.position.z))
        self.aruco_x =msg.pose.position.x
        self.aruco_y = msg.pose.position.y
        self.aruco_z = msg.pose.position.z
        pass

    def listener_callback_2(self, msg):
    
        # print(str(msg.pose.position.x))
        # print(str(msg.pose.position.y))
        self.pose_vertex_x = msg.pose.position.x
        self.pose_vertex_y = msg.pose.position.y
        pass
    def listener_callback_3(self, msg):
        # print(str(msg.data))
        self.vertex_distance = msg.data
        pass
        
    def listener_callback_4(self, msg):
        # print(str(msg.data))
        self.vertex_theta = msg.data
        pass
    def listener_callback_5(self, msg):
        # print(str(msg.data))
        pass
    def listener_callback_6(self, msg):
        # print(str(msg.data))
        pass
    def listener_callback_7(self, msg):
        # print(str(msg.data))
        self.key_move = msg.data
        pass
    def listener_callback_8(self, msg):
        # print(str(msg.data))
        self.time_work = msg.data
        pass
    
    def timer_1_callback(self):
        # if self.key_move == 0.0:
            print("aruco x : "+str(self.aruco_x))
            print("aruco y : "+str(self.aruco_y))
            print("aruco z : "+str(self.aruco_z))
            print("+")
            print("pose_vertex_x : "+str(self.pose_vertex_x))
            print("pose_vertex_y : "+str(self.pose_vertex_y))
            print("+")
            print("vertex_distance : "+str(self.vertex_distance))
            print("vertex_theta : "+str(self.vertex_theta))
            print("+")
            print("time_work: "+str(self.time_work))
            print("----------------------")
            print(str(self.aruco_x))
            print(str(self.aruco_y))
            print(str(self.aruco_z))
            print(str(self.pose_vertex_x))
            print(str(self.pose_vertex_y))
            print(str(self.vertex_distance))
            print(str(self.vertex_theta))
            print(str(self.time_work))
            print("======================\n")
            pass
    

def main(args=None):
    rclpy.init(args=args)

    subscriber = SubscriberClass()

    rclpy.spin(subscriber)

    subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

