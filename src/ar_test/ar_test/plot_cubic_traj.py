import rclpy
from rclpy.node import Node
from ar_interface.msg import CubicTrajCoeffs
from std_msgs.msg import Float64
import numpy as np

class PlotCubicTraj(Node):
    """
    Subscribes to the topic `cubic_traj_coeffs`.
    Computes position, velocity, and acceleration trajectories.
    Publishes them as separate topics for visualization in rqt_plot.
    """
    def __init__(self):
        super().__init__('plot_cubic_traj')
        
        # subscriber to get the cubic coefficients
        self.subscription = self.create_subscription(
            CubicTrajCoeffs,
            'cubic_traj_coeffs',
            self.callback,
            10)
        
        # publishers for position, velocity, and acceleration trajectories
        self.position_pub = self.create_publisher(Float64, 'position_trajectory', 10)
        self.velocity_pub = self.create_publisher(Float64, 'velocity_trajectory', 10)
        self.acceleration_pub = self.create_publisher(Float64, 'acceleration_trajectory', 10)

 
    def callback(self, data):
        t = np.linspace(data.t0, data.tf, num=100)

        # position, velocity, and acceleration
        pos = data.a0 + data.a1 * t + data.a2 * t**2 + data.a3 * t**3
        vel = data.a1 + 2 * data.a2 * t + 3 * data.a3 * t**2
        acc = 2 * data.a2 + 6 * data.a3 * t

        for i in range(100):
            # position
            pos_msg = Float64()
            pos_msg.data = float(pos[i])
            self.position_pub.publish(pos_msg)

            # velocity
            vel_msg = Float64()
            vel_msg.data = float(vel[i])
            self.velocity_pub.publish(vel_msg)

            # acceleration
            acc_msg = Float64()
            acc_msg.data = float(acc[i])
            self.acceleration_pub.publish(acc_msg)


def main(args=None):
    rclpy.init(args=args)
    plot_cubic_traj = PlotCubicTraj()
    rclpy.spin(plot_cubic_traj)
    plot_cubic_traj.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()