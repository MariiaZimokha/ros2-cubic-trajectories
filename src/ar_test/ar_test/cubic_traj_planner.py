import rclpy
from rclpy.node import Node
from ar_interface.msg import CubicTrajParams, CubicTrajCoeffs
from ar_interface.srv import ComputeCubicTraj

class CubicTrajPlanner(Node):
    def __init__(self):
        super().__init__('cubic_traj_planner')
        
        # reading fro the topic to get the generated parameters
        self.subscription = self.create_subscription(
            CubicTrajParams,
            'cubic_traj_params',
            self.listener_callback,
            10)
        # publishing the calculated coefficients
        self.publisher_ = self.create_publisher(CubicTrajCoeffs, 'cubic_traj_coeffs', 10)
        # instance of the service
        self.client = self.create_client(ComputeCubicTraj, 'compute_cubic_traj')

    def listener_callback(self, msg):
        request = ComputeCubicTraj.Request()
        request.p0 = msg.p0
        request.pf = msg.pf
        request.v0 = msg.v0
        request.vf = msg.vf
        request.t0 = msg.t0
        request.tf = msg.tf

        # Pass the request to the future_callback using a lambda function
        future = self.client.call_async(request)
        future.add_done_callback(lambda future: self.future_callback(future, request))

    def future_callback(self, future, request):
        try:
            
            response = future.result()
            msg = CubicTrajCoeffs()
            msg.a0 = response.a0
            msg.a1 = response.a1
            msg.a2 = response.a2
            msg.a3 = response.a3

            msg.t0 = request.t0
            msg.tf = request.tf

            self.publisher_.publish(msg)
            self.get_logger().info(f'Publishing: {msg}')
            # self.get_logger().warn(f'request: {request}')
        except Exception as e:
            self.get_logger().error(f'Service call failed {e}')

def main(args=None):
    rclpy.init(args=args)
    cubic_traj_planner = CubicTrajPlanner()
    rclpy.spin(cubic_traj_planner)
    cubic_traj_planner.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()