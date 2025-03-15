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

        # p(t) = a0 + a1*t + a2*t^2 + a3*t^3
        # q0 = a0 + a1*t_0 + a2*t_0^2 + a3*t_0^3
        # v0 = q0'=  a1 + 2*a2*t_0 + 3*a3*t_0^2
        # qf = a0 + a1*t_f + a2*t_f^2 + a3*t_f^3
        # vf = qf'=  a1 + 2*a2*t_f + 3*a3*t_f^2
        M = [
            [1, t0, t0**2, t0**3], # q0
            [0, 1, 2*t0, 3*t0**2], # v0
            [1, tf, tf**2, tf**3], # qf
            [0, 1, 2*tf, 3*tf**2]  # vf
        ]

        C = [request.p0, request.v0, request.pf, request.vf]
        # M*a = C
        # a = M^-1 * C

        # Solve the linear system to find the coefficients
        a = solve(M, C)

        response.a0 = a[0]
        response.a1 = a[1]
        response.a2 = a[2]
        response.a3 = a[3]

        return response

def main(args=None):
    rclpy.init(args=args)
    compute_cubic_coeffs = ComputeCubicCoeffs()
    
    rclpy.spin(compute_cubic_coeffs)
    compute_cubic_coeffs.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()