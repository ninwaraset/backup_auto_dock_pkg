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
            Twist,
            '/cmd_vel',
            self.listener_callback,
            10)
        
        self.subscription2 = self.create_subscription(
            Float32,
            '/finish_plot',
            self.listener_callback2,
            10)
        
        # self.subscription  # prevent unused variable warning
        self.linear = 0.0
        self.angular = 0.0
        self.linear_list = []
        self.angular_list = []
        
        self.x = 0.0
        self.y = 0.0
        self.time_period_1 = 0.2
        self.timer_1 = self.create_timer(self.time_period_1,self.timer_1_callback)
        
        self.key = 0.0
        self.color = ["pink","red","orange","yellow","green","cyan","purple","k"]
        self.zxc = 0.0
        fig, ( self.ax1, self.ax2) = plt.subplots(2,1)
        self.ax1.set_title('linear velocity')
        self.ax2.set_title('angular velocity')
        self.t_c =0
        self.t_c_list = []
    def listener_callback(self, msg):
        self.linear = msg.linear.x
        self.angular = msg.angular.z
        
        
        
    def listener_callback2(self, msg):
        # print(msg)
        self.key = msg.data
    
    def timer_1_callback(self):
        self.zxc += 1 
        if self.key > 0 :
            self.t_c +=self.time_period_1
            
            self.linear_list.append(self.linear)
            self.angular_list.append(self.angular)
            self.t_c_list.append(self.t_c)
            
        if self.key == 7:
            print("min,max linear vel = "+ str((max(self.linear_list),min(self.linear_list))))
            print("min,max angular vel = "+ str((max(self.angular_list),min(self.angular_list))))
            # for j in range(len( self.linear_list)-1):
            #     self.ax1.plot(self.t_c_list[0],self.linear,"r")
            self.ax1.plot(self.t_c_list,self.linear_list,"r")
            self.ax2.plot(self.t_c_list,self.angular_list,"b")
            
            plt.show()

        
        # self.ax1.plot(self.t_c,self.linear,"r")
        # self.ax2.plot(self.t_c,self.angular,"b")
        print("linear : "+str(self.linear))
        print("angular : "+ str(self.angular))
        print("+")
        print("time : "+str(self.t_c))
        print("key : "+str(self.key))
        print("zxc : "+str(self.zxc))
        print("-------------------")
        
        # if self.zxc == 100 : plt.show()
        pass

def main(args=None):
    rclpy.init(args=args)

    subscriber = PathP()

    rclpy.spin(subscriber)

    subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

