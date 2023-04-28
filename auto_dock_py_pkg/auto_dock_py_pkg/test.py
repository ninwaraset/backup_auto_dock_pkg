#!/usr/bin/python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from rclpy.clock import Clock
import math
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Float32

class MOVE(Node):
    def __init__(self):
        super().__init__('node_name')
        
        self.cmd_publisher = self.create_publisher(Twist,'/cmd_vel',10)

        self.subscription_2 = self.create_subscription(Float32,'/vertex_theta',self.listener_callback_1,10)
        self.subscription_1 = self.create_subscription(Float32,'/vertex_distance',self.listener_callback_2,10)
        self.subscription_4 = self.create_subscription(Float32,'/blue_theta',self.listener_callback_3,10)
        self.subscription_3 = self.create_subscription(Float32,'/blue_distance',self.listener_callback_4,10)
        
        self.lock_blue_pub = self.create_publisher(Float32,'/lock_blue',10)
        self.finish_plot_pub = self.create_publisher(Float32,'/finish_plot',10)
        

        time_period_1 = 0.1
        self.timer_1 = self.create_timer(time_period_1,self.timer_1_callback)
        


        self.avg_vertex_theta = 0.0
        self.avg_vertex_distance = 0.0
        

        self.avg_blue_distance = 0.0
        self.avg_blue_theta = 0.0
        


        self.key_st = 0
        self.key_timer = 0
        self.time_d = 0.0
        self.t_i = 0
        self.t_c = 0
        self.zxc = 0
        


##########################################################################################################################################################################
##########################################################################################################################################################################       
##########################################################################################################################################################################
########################################################################################################################################################################## 

    def listener_callback_1(self,msg):
        # print("msg_recived 1 : " + str(msg))
        self.avg_vertex_theta = msg.data
        
        if self.key_st == 0:
            self.key_st = 1
        pass

    def listener_callback_2(self,msg):
        # print("msg_recived 2 : " + str(msg))
        self.avg_vertex_distance = msg.data
        pass
    

    def listener_callback_3(self,msg):
        # print("msg_recived 2 : " + str(msg))
        self.avg_blue_theta = msg.data
        pass

    def listener_callback_4(self,msg):
        # print("msg_recived 4 : " + str(msg))
        self.avg_blue_distance = msg.data
        pass

    
##########################################################################################################################################################################
##########################################################################################################################################################################       
##########################################################################################################################################################################
########################################################################################################################################################################## 


    def timer_1_callback(self):
        if self.key_timer == 0:
            self.t_i = Clock().now().nanoseconds/((10**9))
            self.key_timer = 1
         
        self.t_c =  Clock().now().nanoseconds/((10**9))
        self.time_d = self.t_c-self.t_i
        
        print(self.t_i)
        print(self.t_c)
        print(self.time_d)

        





    
def main(args=None):
    
    
    rclpy.init(args=args)
    controller = MOVE()
    rclpy.spin(controller)
    controller.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()




