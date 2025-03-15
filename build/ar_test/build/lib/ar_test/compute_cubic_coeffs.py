import rclpy
from rclpy.node import Node
from ar_interface.srv import ComputeCubicTraj
from numpy.linalg import solve

class ComputeCubicCoeffs(Node):
    def __init__(self):
        super().__init__('compute_cubic_coeffs')
        self.srv = self.create_service(ComputeCubicTraj, 'compute_cubic_traj', self.compute_cubic_traj_callback)

    def compute_cubic_traj_callback(self, request, response):
        t0 = request.t0
        tf = request.tf
        dt = tf - t0

        A = [
            [1, t0, t0**2, t0**3],
            [0, 1, 2*t0, 3*t0**2],
            [1, tf, tf**2, tf**3],
            [0, 1, 2*tf, 3*tf**2]
        ]

        B = [request.p0, request.v0, request.pf, request.vf]

        # Solve the linear system to find the coefficients
        coeffs = solve(A, B)

        response.a0 = coeffs[0]
        response.a1 = coeffs[1]
        response.a2 = coeffs[2]
        response.a3 = coeffs[3]

        return response

def main(args=None):
    rclpy.init(args=args)
    compute_cubic_coeffs = ComputeCubicCoeffs()
    rclpy.spin(compute_cubic_coeffs)
    compute_cubic_coeffs.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()