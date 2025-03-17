from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess

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

        # rqt_graph
        ExecuteProcess(
            cmd=['rqt_graph'],
            output='screen'
        ),

        # rqt_plot for graphs
        ExecuteProcess(
            cmd=['ros2', 'run', 'rqt_plot', 'rqt_plot', '/position_trajectory/data', '/velocity_trajectory/data', '/acceleration_trajectory/data'],
            output='screen'
        ),
    ])

