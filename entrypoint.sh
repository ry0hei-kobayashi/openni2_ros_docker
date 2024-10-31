#!/bin/bash
set -e

source /opt/ros/humble/setup.bash

# allowing access to the usb device 
exec "$@"

