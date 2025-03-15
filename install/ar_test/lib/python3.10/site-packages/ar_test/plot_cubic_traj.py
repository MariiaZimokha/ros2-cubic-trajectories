import rclpy
from rclpy.node import Node
from ar_interface.msg import CubicTrajCoeffs
import numpy as np
import matplotlib.pyplot as plt

class PlotCubicTraj(Node):
    def __init__(self):
        super().__init__('plot_cubic_traj')
        self.subscription = self.create_subscription(
            CubicTrajCoeffs,
            'cubic_traj_coeffs',
            self.listener_callback,
            10)
        self.fig, self.ax = plt.subplots()
        self.lines = []

    def listener_callback(self, msg):
        t = np.linspace(msg.t0, msg.tf, 100)
        p = msg.a0 + msg.a1*t + msg.a2*t**2 + msg.a3*t**3
        v = msg.a1 + 2*msg.a2*t + 3*msg.a3*t**2
        a = 2*msg.a2 + 6*msg.a3*t

        if not self.lines:
            line1, = self.ax.plot(t, p, label='Position')
            line2, = self.ax.plot(t, v, label='Velocity')
            line3, = self.ax.plot(t, a, label='Acceleration')
            self.lines = [line1, line2, line3]
            self.ax.legend()
        else:
            self.lines[0].set_data(t, p)
            self.lines[1].set_data(t, v)
            self.lines[2].set_data(t, a)

        self.ax.relim()
        self.ax.autoscale_view()
        plt.draw()
        plt.pause(0.01)

def main(args=None):
    rclpy.init(args=args)
    plot_cubic_traj = PlotCubicTraj()
    rclpy.spin(plot_cubic_traj)
    plot_cubic_traj.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()