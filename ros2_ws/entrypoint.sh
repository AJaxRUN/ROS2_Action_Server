#!/bin/bash

# Source ROS2 setup
source /opt/ros/humble/setup.bash
source /ros2_ws/install/setup.bash

# Add ROS2 workspace to PYTHONPATH
# export PYTHONPATH="/ros2_ws/install/lib/python3.10/site-packages:$PYTHONPATH"

# Start FastAPI in the background
uvicorn rest_api:app --host 0.0.0.0 --port 8080 &

# Start ROS2 nodes
ros2 launch launch.py
tail -f /dev/null