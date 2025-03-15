# import rclpy
# from rclpy.node import Node
# from ar_interface.msg import CubicTrajCoeffs
# import numpy as np
# import matplotlib.pyplot as plt


# class PlotCubicTraj(Node):
#     """
#     Subscribes to the topic `cubic_traj_coeffs` 
#     input data: 
#         a0, a1, a2, a3 - cubic coefficients
    
        
#     """
#     def __init__(self):
#         super().__init__('plot_cubic_traj')
#         self.subscription = self.create_subscription(
#             CubicTrajCoeffs,
#             'cubic_traj_coeffs',
#             self.listener_callback,
#             10)
#         self.fig, self.ax = plt.subplots()
#         self.lines = []

#     def listener_callback(self, msg):
#         t = np.linspace(msg.t0, msg.tf, 100)
#         p = msg.a0 + msg.a1*t + msg.a2*t**2 + msg.a3*t**3
#         v = msg.a1 + 2*msg.a2*t + 3*msg.a3*t**2
#         a = 2*msg.a2 + 6*msg.a3*t

#         if not self.lines:
#             line1, = self.ax.plot(t, p, label='Position')
#             line2, = self.ax.plot(t, v, label='Velocity')
#             line3, = self.ax.plot(t, a, label='Acceleration')
#             self.lines = [line1, line2, line3]
#             self.ax.legend()
#         else:
#             self.lines[0].set_data(t, p)
#             self.lines[1].set_data(t, v)
#             self.lines[2].set_data(t, a)

#         self.ax.relim()
#         self.ax.autoscale_view()
#         plt.draw()
#         plt.pause(0.01)

# def main(args=None):
#     rclpy.init(args=args)
#     plot_cubic_traj = PlotCubicTraj()
#     rclpy.spin(plot_cubic_traj)
#     plot_cubic_traj.destroy_node()
#     rclpy.shutdown()

# if __name__ == '__main__':
#     main()





# import rclpy
# from rclpy.node import Node
# from ar_interface.msg import CubicTrajCoeffs
# from std_msgs.msg import Float64MultiArray
# import numpy as np

# class PlotCubicTraj(Node):
#     """
#     Subscribes to the topic `cubic_traj_coeffs`.
#     Computes position, velocity, and acceleration trajectories.
#     Publishes them as separate topics for visualization in rqt_plot.
#     """
#     def __init__(self):
#         super().__init__('plot_cubic_traj')
        
#         # Subscriber to get the cubic coefficients
#         self.subscription = self.create_subscription(
#             CubicTrajCoeffs,
#             'cubic_traj_coeffs',
#             self.listener_callback,
#             10)
        
#         # Publishers for position, velocity, and acceleration trajectories
#         self.position_pub = self.create_publisher(Float64MultiArray, 'position_trajectory', 10)
#         self.velocity_pub = self.create_publisher(Float64MultiArray, 'velocity_trajectory', 10)
#         self.acceleration_pub = self.create_publisher(Float64MultiArray, 'acceleration_trajectory', 10)

#     def listener_callback(self, msg):
#         self.get_logger().info(f'listener_callback -------------------------------------------')
#         # Time vector from t0 to tf
#         t = np.linspace(msg.t0, msg.tf, 100)
        
#         # Compute position, velocity, and acceleration
#         p = msg.a0 + msg.a1*t + msg.a2*t**2 + msg.a3*t**3  # Position
#         v = msg.a1 + 2*msg.a2*t + 3*msg.a3*t**2           # Velocity
#         a = 2*msg.a2 + 6*msg.a3*t                         # Acceleration

#         # Publish position trajectory
#         position_msg = Float64MultiArray()
#         position_msg.data = p.tolist()

#         self.position_pub.publish(position_msg)

#         # Publish velocity trajectory
#         velocity_msg = Float64MultiArray()
#         velocity_msg.data = v.tolist()
#         self.velocity_pub.publish(velocity_msg)

#         # Publish acceleration trajectory
#         acceleration_msg = Float64MultiArray()
#         acceleration_msg.data = a.tolist()
#         self.acceleration_pub.publish(acceleration_msg)

#         # Log for debugging
#         self.get_logger().info('Published trajectories')

# def main(args=None):
#     rclpy.init(args=args)
#     plot_cubic_traj = PlotCubicTraj()
#     rclpy.spin(plot_cubic_traj)
#     plot_cubic_traj.destroy_node()
#     rclpy.shutdown()

# if __name__ == '__main__':
    # main()


#!/usr/bin/env python3

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
        
        # Subscriber to get the cubic coefficients
        self.subscription = self.create_subscription(
            CubicTrajCoeffs,
            'cubic_traj_coeffs',
            self.callback,
            10)
        
        # Publishers for position, velocity, and acceleration trajectories
        self.position_pub = self.create_publisher(Float64, 'position_trajectory', 10)
        self.velocity_pub = self.create_publisher(Float64, 'velocity_trajectory', 10)
        self.acceleration_pub = self.create_publisher(Float64, 'acceleration_trajectory', 10)

        self.get_logger().info("Reading Coefficients: receiving messages on topic: 'cubic_traj_coeffs', "
                              "publishing messages on topics 'position_trajectory', 'velocity_trajectory', "
                              "'acceleration_trajectory'")

    def callback(self, data):
        # Log received coefficients
        self.get_logger().info(f"Received coefficients: t0={data.t0}, tf={data.tf}")

        # Ensure tf is valid
        # if data.tf <= data.t0:
        #     self.get_logger().error(f"Invalid tf value: tf={data.tf} must be greater than t0={data.t0}.")
        #     return

        # Time vector from t0 to tf
        nint = 100  # Number of points (fixed for smooth plotting)
        t = np.linspace(data.t0, data.tf, num=nint)

        # Compute position, velocity, and acceleration
        pos = data.a0 + data.a1 * t + data.a2 * t**2 + data.a3 * t**3
        vel = data.a1 + 2 * data.a2 * t + 3 * data.a3 * t**2
        acc = 2 * data.a2 + 6 * data.a3 * t

        # Publish trajectories point-by-point
        # rate = self.create_rate(int(nint / (data.tf)))  # Rate for publishing
        for i in range(nint):
            # Publish position
            pos_msg = Float64()
            pos_msg.data = float(pos[i])
            self.position_pub.publish(pos_msg)

            # Publish velocity
            vel_msg = Float64()
            vel_msg.data = float(vel[i])
            self.velocity_pub.publish(vel_msg)

            # Publish acceleration
            acc_msg = Float64()
            acc_msg.data = float(acc[i])
            self.acceleration_pub.publish(acc_msg)

            # self.get_logger().info(f'Publishing PLOTS ---------------------------------------')


            # rate.sleep()  # Maintain the publishing rate

def main(args=None):
    rclpy.init(args=args)
    plot_cubic_traj = PlotCubicTraj()
    rclpy.spin(plot_cubic_traj)
    plot_cubic_traj.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()