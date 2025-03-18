import rclpy
from rclpy.node import Node
from ar_interface.msg import CubicTrajParams
import random


class PointsGenerator(Node):
    """
    The class generates the random values:
    - initial and final posions
    - initial and final velocities
    - initial and final time
    """
    def __init__(self):
        super().__init__('points_generator')

        # creating a publisher - message Type, topic name, time
        self.publisher_ = self.create_publisher(CubicTrajParams, 'cubic_traj_params', 10)
        
        # calling a callback function (points generation) every 10 seconds
        self.timer = self.create_timer(10.0, self.timer_callback)

    def timer_callback(self):
        # instances of interface CubicTrajParams 
        msg = CubicTrajParams()

        # randomly generate values - the ranges are given 
        msg.p0 = random.uniform(-10, 10)
        msg.pf = random.uniform(-10, 10)
        msg.v0 = random.uniform(-10, 10)
        msg.vf = random.uniform(-10, 10)
        
        # time
        msg.t0 = 0.0
        dt = random.uniform(4, 8)
        msg.tf = msg.t0 + dt

        # publishing the message to the topic
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: {msg}')

def main(args=None):
    rclpy.init(args=args)
    # creating and running the publish node
    points_generator = PointsGenerator()
    rclpy.spin(points_generator)


    points_generator.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()