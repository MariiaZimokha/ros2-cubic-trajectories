from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='ar_test',
            executable='points_generator',
            output='screen'),
        Node(
            package='ar_test',
            executable='cubic_traj_planner',
            output='screen'),
        Node(
            package='ar_test',
            executable='compute_cubic_coeffs',
            output='screen'),
        Node(
            package='ar_test',
            executable='plot_cubic_traj',
            output='screen'),
    ])

# output='screen' - output is printed in console