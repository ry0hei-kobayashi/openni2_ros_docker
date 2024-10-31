FROM ros:humble-ros-base

RUN apt-get update && apt-get install -y \
    libusb-1.0-0-dev \
    libopenni2-dev \
    ros-humble-camera-info-manager \
    ros-humble-image-transport \
    ros-humble-openni2-camera \
    && rm -rf /var/lib/apt/lists/*

COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

