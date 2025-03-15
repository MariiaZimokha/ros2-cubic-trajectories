from setuptools import find_packages, setup
import os
import glob

package_name = 'ar_test'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # Include the launch file
        (os.path.join('share', package_name, 'launch'), glob.glob('launch/*.launch.py'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Mariia Zimokha',
    maintainer_email='m.zimokha@se24.qmul.ac.uk',
    description='ROS2 package for generating and plotting cubic trajectories.',
    license='Apache-2.0',
    # tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            # all executable nodes here
            'points_generator = ar_test.points_generator:main',
            'cubic_traj_planner = ar_test.cubic_traj_planner:main',
            'compute_cubic_coeffs = ar_test.compute_cubic_coeffs:main',
            'plot_cubic_traj = ar_test.plot_cubic_traj:main',
        ],
    },
)
