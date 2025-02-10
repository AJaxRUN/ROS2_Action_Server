FROM ros:humble

WORKDIR /ros2_ws

RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-colcon-common-extensions \
    ros-humble-rclpy \
    ros-humble-ros2action \
    ros-humble-action-msgs \
    && rm -rf /var/lib/apt/lists/* 

COPY requirements.txt /ros2_ws/

RUN sed -i '/rclpy/d' requirements.txt && pip3 install --no-cache-dir -r requirements.txt

RUN . /opt/ros/humble/setup.sh

COPY ./ros2_ws /ros2_ws

RUN /bin/bash -c "source /opt/ros/humble/setup.bash && colcon build --symlink-install"

ENV ROS_DOMAIN_ID=0

EXPOSE 8080

RUN chmod +x /ros2_ws/entrypoint.sh

ENTRYPOINT ["/ros2_ws/entrypoint.sh"]
