from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription(
        [
            Node(
                package='launch_demo_pkg',
                executable='talker_node',
                name='talker_node'
            ),
            Node(
                package = 'launch_demo_pkg',
                executable = 'listener_node',
                name = 'listener_node'
            )
        ]
    )