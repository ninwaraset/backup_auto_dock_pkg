from setuptools import setup
import os
from glob import glob
from setuptools import setup

package_name = 'auto_dock_py_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        
        # (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*.launch.py'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='carver',
    maintainer_email='carver@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        '01_pub = auto_dock_py_pkg.01_pub:main',
        '01_sub = auto_dock_py_pkg.01_sub:main',
        'st_scan = auto_dock_py_pkg.st_scan:main',
        'st_move = auto_dock_py_pkg.st_move:main',
        'aruco_node = auto_dock_py_pkg.aruco_node:main',
        'turtle_tf2_listener = learning_tf2_py.turtle_tf2_listener:main',
        ],
    },
)
