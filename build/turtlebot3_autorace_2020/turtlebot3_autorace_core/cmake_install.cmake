# Install script for directory: /home/ros/catkin_ws/src/turtlebot3_autorace_2020/turtlebot3_autorace_core

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/ros/catkin_ws/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  include("/home/ros/catkin_ws/build/turtlebot3_autorace_2020/turtlebot3_autorace_core/catkin_generated/safe_execute_install.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/ros/catkin_ws/build/turtlebot3_autorace_2020/turtlebot3_autorace_core/catkin_generated/installspace/turtlebot3_autorace_core.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/turtlebot3_autorace_core/cmake" TYPE FILE FILES
    "/home/ros/catkin_ws/build/turtlebot3_autorace_2020/turtlebot3_autorace_core/catkin_generated/installspace/turtlebot3_autorace_coreConfig.cmake"
    "/home/ros/catkin_ws/build/turtlebot3_autorace_2020/turtlebot3_autorace_core/catkin_generated/installspace/turtlebot3_autorace_coreConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/turtlebot3_autorace_core" TYPE FILE FILES "/home/ros/catkin_ws/src/turtlebot3_autorace_2020/turtlebot3_autorace_core/package.xml")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/turtlebot3_autorace_core" TYPE PROGRAM FILES "/home/ros/catkin_ws/build/turtlebot3_autorace_2020/turtlebot3_autorace_core/catkin_generated/installspace/core_node_mission")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/turtlebot3_autorace_core" TYPE PROGRAM FILES "/home/ros/catkin_ws/build/turtlebot3_autorace_2020/turtlebot3_autorace_core/catkin_generated/installspace/construction_core_mode_decider")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/turtlebot3_autorace_core" TYPE PROGRAM FILES "/home/ros/catkin_ws/build/turtlebot3_autorace_2020/turtlebot3_autorace_core/catkin_generated/installspace/construction_core_node_controller")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/turtlebot3_autorace_core" TYPE PROGRAM FILES "/home/ros/catkin_ws/build/turtlebot3_autorace_2020/turtlebot3_autorace_core/catkin_generated/installspace/intersection_core_mode_decider")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/turtlebot3_autorace_core" TYPE PROGRAM FILES "/home/ros/catkin_ws/build/turtlebot3_autorace_2020/turtlebot3_autorace_core/catkin_generated/installspace/intersection_core_node_controller")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/turtlebot3_autorace_core" TYPE PROGRAM FILES "/home/ros/catkin_ws/build/turtlebot3_autorace_2020/turtlebot3_autorace_core/catkin_generated/installspace/level_crossing_core_mode_decider")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/turtlebot3_autorace_core" TYPE PROGRAM FILES "/home/ros/catkin_ws/build/turtlebot3_autorace_2020/turtlebot3_autorace_core/catkin_generated/installspace/level_crossing_core_node_controller")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/turtlebot3_autorace_core" TYPE PROGRAM FILES "/home/ros/catkin_ws/build/turtlebot3_autorace_2020/turtlebot3_autorace_core/catkin_generated/installspace/parking_core_mode_decider")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/turtlebot3_autorace_core" TYPE PROGRAM FILES "/home/ros/catkin_ws/build/turtlebot3_autorace_2020/turtlebot3_autorace_core/catkin_generated/installspace/parking_core_node_controller")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/turtlebot3_autorace_core" TYPE PROGRAM FILES "/home/ros/catkin_ws/build/turtlebot3_autorace_2020/turtlebot3_autorace_core/catkin_generated/installspace/traffic_light_core_mode_decider")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/turtlebot3_autorace_core" TYPE PROGRAM FILES "/home/ros/catkin_ws/build/turtlebot3_autorace_2020/turtlebot3_autorace_core/catkin_generated/installspace/traffic_light_core_node_controller")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/turtlebot3_autorace_core" TYPE PROGRAM FILES "/home/ros/catkin_ws/build/turtlebot3_autorace_2020/turtlebot3_autorace_core/catkin_generated/installspace/tunnel_core_mode_decider")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/turtlebot3_autorace_core" TYPE PROGRAM FILES "/home/ros/catkin_ws/build/turtlebot3_autorace_2020/turtlebot3_autorace_core/catkin_generated/installspace/tunnel_core_node_controller")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/turtlebot3_autorace_core" TYPE DIRECTORY FILES "/home/ros/catkin_ws/src/turtlebot3_autorace_2020/turtlebot3_autorace_core/launch")
endif()

