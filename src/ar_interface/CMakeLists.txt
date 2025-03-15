# cmake_minimum_required(VERSION 3.8)
# project(ar_interface)

# if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
#   add_compile_options(-Wall -Wextra -Wpedantic)
# endif()

# # find dependencies
# find_package(ament_cmake REQUIRED)

# find_package(rosidl_default_generators REQUIRED)
# # uncomment the following section in order to fill in
# # further dependencies manually.
# # find_package(<dependency> REQUIRED)

# # MUST BE ADDED
# # Generate interfaces
# rosidl_generate_interfaces(${PROJECT_NAME}
#   "msg/CubicTrajCoeffs.msg"
#   "msg/CubicTrajParams.msg"
#   "srv/ComputeCubicTraj.srv"
# )
# # Important note!
# #   rosidl_adapter.parser.InvalidResourceName: 'cubic_traj_coeffs' is an
# #invalid message name.  It should have the pattern '^[A-Z][A-Za-z0-9]*$'


# if(BUILD_TESTING)
#   find_package(ament_lint_auto REQUIRED)
#   # the following line skips the linter which checks for copyrights
#   # comment the line when a copyright and license is added to all source files
#   set(ament_cmake_copyright_FOUND TRUE)
#   # the following line skips cpplint (only works in a git repo)
#   # comment the line when this package is in a git repo and when
#   # a copyright and license is added to all source files
#   set(ament_cmake_cpplint_FOUND TRUE)
#   ament_lint_auto_find_test_dependencies()
# endif()

# ament_package()
cmake_minimum_required(VERSION 3.5)
project(ar_interface)

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

# Find dependencies
find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)
find_package(rosidl_default_runtime REQUIRED)
find_package(std_msgs REQUIRED)

# Define messages and services
rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/CubicTrajParams.msg"
  "msg/CubicTrajCoeffs.msg"
  "srv/ComputeCubicTraj.srv"
)

# Install the messages and services
ament_export_dependencies(rosidl_default_runtime)
install(DIRECTORY msg DESTINATION share/${PROJECT_NAME})
install(DIRECTORY srv DESTINATION share/${PROJECT_NAME})

ament_package()