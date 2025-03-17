
**Code developed by Mariia Zimokha**  
**Student ID:** 240129639

---

## Prerequisites

- **Python 3.10**  
- **ROS 2 (Humble)**

---

## Installation and Build Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/MariiaZimokha/ros2-cubic-trajectories.git
   ```

2. **Source the ROS 2 Environment**

   ```bash
   source /opt/ros/humble/setup.bash
   ```

3. **Build th e Packages**

    ```bash
    cd ros2-cubic-trajectories
    colcon build
    ```

4. **Source the Wotkspace**

    ```bash
    source install/setup.bash
    ```

## Running the packages

Launch the package with:

```bash
ros2 launch ar_test cubic_traj_gen.launch.py
```


