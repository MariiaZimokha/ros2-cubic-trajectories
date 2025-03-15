import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/mnt/hgfs/Uni/Uni/Term2/EMS728P_Advance_Robotic_Systems/ros2-cubic-trajectories/install/ar_test'
