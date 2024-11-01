#!/bin/bash
set -e

source /opt/ros/noetic/setup.bash

# allowing access to the usb device 
exec "$@"

