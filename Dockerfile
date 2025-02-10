# Use ROS2 Humble as the base image
FROM ros:humble

# Set working directory
WORKDIR /ros2_ws

# Install system dependencies and ROS2 packages
RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-colcon-common-extensions \
    ros-humble-rclpy \
    ros-humble-ros2action \
    ros-humble-action-msgs \
    && rm -rf /var/lib/apt/lists/* 

# Copy Python dependencies
COPY requirements.txt /ros2_ws/

# Remove rclpy from requirements.txt before installing Python packages
RUN sed -i '/rclpy/d' requirements.txt && pip3 install --no-cache-dir -r requirements.txt

RUN . /opt/ros/humble/setup.sh
# RUN . /opt/ros/humble/setup.sh && \
    # ros2 pkg create rn1 --build-type ament_python && \
    # ros2 pkg create rn2 --build-type ament_python

# Copy all source code into the container
COPY ./ros2_ws /ros2_ws
# RUN chmod +x /ros2_ws/src/rn1/rn1/talker.py

# Build ROS2 workspace
RUN /bin/bash -c "source /opt/ros/humble/setup.bash && colcon build --symlink-install"

# Set environment variables
ENV ROS_DOMAIN_ID=0
# ENV PYTHONPATH="/ros2_ws/install/lib/python3.10/site-packages:$PYTHONPATH"

# Expose FastAPI port
EXPOSE 8000

# Copy entrypoint script
COPY entrypoint.sh /ros2_ws/
RUN chmod +x /ros2_ws/entrypoint.sh

# Run entrypoint script
ENTRYPOINT ["/ros2_ws/entrypoint.sh"]
