FROM ros:noetic-ros-base

RUN apt-get update && apt-get install -y \
    ros-noetic-openni2-camera \
    ros-noetic-openni2-launch \
    libusb-1.0-0-dev \
    && rm -rf /var/lib/apt/lists/*

RUN /bin/bash -c "source /opt/ros/noetic/setup.bash"

COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

CMD ["roslaunch", "openni2_launch", "openni2.launch"]

