#!/bin/bash
set -e

source /opt/ros/humble/setup.bash
source /colcon_ws/install/setup.bash

# allowing access to the usb device 
exec "$@"

