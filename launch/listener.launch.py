from launch import LaunchDescription, launchDescription
from launch_ros.actions import Node

def generate_launch_descriptions():
    return LaunchDescription(
        Node(
            package='demo_nodes_py',
            executable='listener'
        )
    )