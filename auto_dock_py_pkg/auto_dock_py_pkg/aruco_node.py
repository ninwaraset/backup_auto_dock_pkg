#!/usr/bin/env python3
import cv2
import numpy as np
import tf2_ros

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from geometry_msgs.msg import PoseStamped, TransformStamped
from std_msgs.msg import Int16
from sensor_msgs.msg import CameraInfo

class ArucoDetector(Node):
    def __init__(self):
        super().__init__('aruco_detector')

        # Subscribe to the camera topic
        self.subscription = self.create_subscription(Image, '/camera/color/image_raw', self.detect_aruco, 10)
        self.subscription = self.create_subscription(CameraInfo, '/camera/color/camera_info', self.camera_info_callback, 10)

        # Initialize OpenCV aruco dictionary
        self.aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_5X5_250)

        # Initialize OpenCV aruco parameters
        self.aruco_params = cv2.aruco.DetectorParameters()

        # Initialize the ROS image converter
        self.bridge = CvBridge()

        # publisher to publish pose of the detected ArUco marker from camera_color_optical_frame
        self.publisher_pose = self.create_publisher(PoseStamped, 'aruco_pose', 10)
        
        # Initialize the publisher to publish id of the detected ArUco marker
        self.publisher_id = self.create_publisher(Int16, 'aruco_id', 10)

        # Set the pose frame id
        self.pose_frame_id = 'marker_frame'

        # Initialize the transform broadcaster for aruco pose
        self.tf_broadcaster = tf2_ros.TransformBroadcaster(self)

        # Subscribe to the aruco pose topic
        self.pose_subscription = self.create_subscription(PoseStamped, 'aruco_pose', self.publish_transform, 10)
        self.K = 0
    
    def camera_info_callback(self, msg):
        self.K = msg.k
        self.K = list(self.K)
    
    def publish_transform(self, pose_msg):
        transform_msg = TransformStamped()
        transform_msg.header.stamp = self.get_clock().now().to_msg()
        transform_msg.header.frame_id = 'camera_color_optical_frame'
        transform_msg.child_frame_id = self.pose_frame_id
        transform_msg.transform.translation.x = pose_msg.pose.position.x      # SI Unit: Mater,Radian
        transform_msg.transform.translation.y = pose_msg.pose.position.y
        transform_msg.transform.translation.z = pose_msg.pose.position.z
        transform_msg.transform.rotation.x = pose_msg.pose.orientation.x
        transform_msg.transform.rotation.y = pose_msg.pose.orientation.y
        transform_msg.transform.rotation.z = pose_msg.pose.orientation.z
        transform_msg.transform.rotation.w = pose_msg.pose.orientation.w
        self.tf_broadcaster.sendTransform(transform_msg)   # Publish the transform

    def detect_aruco(self, data):
        cv_image = self.bridge.imgmsg_to_cv2(data, 'bgr8')      # Convert ROS Image message to OpenCV image
        gray = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)       # Convert to grayscale
        corners, ids, _ = cv2.aruco.detectMarkers(gray, self.aruco_dict, parameters=self.aruco_params)    # Detect aruco markers

        # If markers are detected, estimate pose
        if ids is not None and len(ids) > 0:
            id = ids[0][0]   # Get the id of the first detected marker
            id_msg = Int16()
            id_msg.data = int(id)
            self.publisher_id.publish(id_msg)

            # Initialize camera matrix and distortion coefficients
            self.camera_matrix = np.array([[self.K[0],0,self.K[2]], [0, self.K[4], self.K[5]], [0, 0, 1]])
            self.dist_coeffs = np.array([0.0, 0.0, 0.0, 0.0, 0.0])
            marker_size = 0.10 # (meter)
            # rvecs: orientation (radian), tvecs: position (meter)
            rvecs, tvecs, _ = cv2.aruco.estimatePoseSingleMarkers(corners,marker_size,self.camera_matrix, self.dist_coeffs)
            
            pose_msg = PoseStamped()
            pose_msg.header.stamp = self.get_clock().now().to_msg()
            pose_msg.header.frame_id = 'camera_color_optical_frame'
            pose_msg.pose.position.x = tvecs[0][0][0]
            pose_msg.pose.position.y = tvecs[0][0][1] 
            pose_msg.pose.position.z = tvecs[0][0][2] 
            pose_msg.pose.orientation.x = rvecs[0][0][0] 
            pose_msg.pose.orientation.y = rvecs[0][0][1] 
            pose_msg.pose.orientation.z = rvecs[0][0][2] 
            pose_msg.pose.orientation.w = 1.0
            self.publisher_pose.publish(pose_msg)
            self.publish_transform(pose_msg)
            print("x: "+str(pose_msg.pose.position.x ))
            print("y: "+str(pose_msg.pose.position.y ))
            print("z: "+str(pose_msg.pose.position.z ))
            
            print("-------")
            # print(str(000))
            # print(" ")


def main(args=None):
    rclpy.init(args=args)
    aruco_detector = ArucoDetector()
    rclpy.spin(aruco_detector)
    aruco_detector.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()