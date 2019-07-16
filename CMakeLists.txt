cmake_minimum_required(VERSION 2.8.3)
project(ros_apio)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  sensor_msgs
  std_msgs
  message_generation
)

add_service_files(
  FILES
  RosApio.srv
)

catkin_package(
  CATKIN_DEPENDS roscpp rospy sensor_msgs std_msgs message_runtime
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)
