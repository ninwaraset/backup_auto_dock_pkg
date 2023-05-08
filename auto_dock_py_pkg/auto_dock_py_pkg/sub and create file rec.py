#!/usr/bin/python3


num_file = 5
import rclpy
from rclpy.node import Node
import matplotlib.pyplot as plt
from std_msgs.msg import Float32

from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from sensor_msgs.msg import LaserScan
import xlwt
class SubscriberClass(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(
            LaserScan,'/scan'
            ,
            self.listener_callback,
            10)
        
    
        self.subscription  # prevent unused variable warning
        self.i = 0
        self.wb = xlwt.Workbook()
        self.ws_r  =  self.wb.add_sheet('ranges')
        self.ws_info  =  self.wb.add_sheet('info')
        self.ws_inten  =  self.wb.add_sheet('inten')
        
        
        

        
    def listener_callback(self, msg):
        print(self.i)
        print(len(msg.ranges))
        print(len(msg.intensities))
        
        self.ws_r.write(0, self.i,self.i)
        self.ws_inten.write(0, self.i,self.i)
        
        for j in range(len(msg.ranges)):
            # print(j)
            self.ws_r.write(j+1, self.i,msg.ranges[j])
            self.ws_inten.write(j+1, self.i,msg.intensities[j])
            
            
            
        self.ws_info.write(0, self.i,self.i)
        self.ws_info.write(1, self.i,msg.angle_min)
        self.ws_info.write(2, self.i,msg.angle_max)
        self.ws_info.write(3, self.i,msg.angle_increment)
        self.ws_info.write(4, self.i,msg.header.stamp.sec)
        self.ws_info.write(5, self.i,msg.header.stamp.nanosec)
        
        
        
        if self.i == 100:
            self.wb.save('lidar_data_chrck_'+str(num_file)+'.xls')
            dd
        # self.wb.save('example.xls')
        self.i = self.i+1

def main(args=None):
    rclpy.init(args=args)

    subscriber = SubscriberClass()

    rclpy.spin(subscriber)

    subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

