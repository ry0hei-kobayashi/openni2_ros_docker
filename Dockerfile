FROM ros:humble-ros-base

RUN apt-get update && apt-get install -y \
    libusb-1.0-0-dev \
    libopenni2-dev \
    ros-humble-camera-info-manager \
    ros-humble-image-transport \
    ros-humble-openni2-camera \
    ros-humble-ament-cmake \ 
    python3-colcon-common-extensions \
    && rm -rf /var/lib/apt/lists/*

RUN cd / && mkdir -p /colcon_ws/src

COPY ./openni2_interfaces /colcon_ws/src/openni2_interfaces
COPY ./openni2_service    /colcon_ws/src/openni2_service

RUN bash -c ". /opt/ros/humble/setup.bash && cd /colcon_ws && colcon build && . /colcon_ws/install/setup.bash"

COPY ./entrypoint.sh /colcon_ws/entrypoint.sh
RUN chmod +x /colcon_ws/entrypoint.sh
ENTRYPOINT ["/colcon_ws/entrypoint.sh"]

WORKDIR /colcon_ws
