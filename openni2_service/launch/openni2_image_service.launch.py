# xtion_service_launch.py
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    openni2_launch_path = os.path.join(
        get_package_share_directory('openni2_camera'), 'launch', 'camera_with_cloud.launch.py'
    )

    openni2_camera_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(openni2_launch_path)
    )

    xtion_service_server = Node(
        package='openni2_service',
        executable='xtion_service_server',
        name='xtion_service_server',
        output='screen'
    )

    return LaunchDescription([
        openni2_camera_launch,
        xtion_service_server
    ])

