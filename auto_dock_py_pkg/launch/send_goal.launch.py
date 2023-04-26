import launch
import launch_ros.actions

def generate_launch_description():
    return launch.LaunchDescription([
        launch_ros.actions.Node(
            package='auto_dock_py_pkg',
            executable='aruco_node',
            # name='goal2'
            ),

           
        launch_ros.actions.Node(
            package='realsense2_camera',
            executable='rs_launch.py',
            # name='goal2'
        )
    ])
