cmake_minimum_required(VERSION 3.8)
project(openni2_interfaces)

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)
find_package(sensor_msgs REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
  "srv/GetXtionImage.srv"
  DEPENDENCIES sensor_msgs
)

ament_package()
