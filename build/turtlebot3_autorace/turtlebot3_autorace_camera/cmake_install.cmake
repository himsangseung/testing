# Install script for directory: /home/himsangseung/catkin_ws/src/turtlebot3_autorace/turtlebot3_autorace_camera

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/himsangseung/catkin_ws/install")
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

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  include("/home/himsangseung/catkin_ws/build/turtlebot3_autorace/turtlebot3_autorace_camera/catkin_generated/safe_execute_install.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/turtlebot3_autorace_camera" TYPE FILE FILES "/home/himsangseung/catkin_ws/devel/include/turtlebot3_autorace_camera/ImageProjectionParamsConfig.h")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/turtlebot3_autorace_camera" TYPE FILE FILES "/home/himsangseung/catkin_ws/devel/include/turtlebot3_autorace_camera/ImageCompensationParamsConfig.h")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  execute_process(COMMAND "/usr/bin/python" -m compileall "/home/himsangseung/catkin_ws/devel/lib/python2.7/dist-packages/turtlebot3_autorace_camera/cfg")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/turtlebot3_autorace_camera" TYPE DIRECTORY FILES "/home/himsangseung/catkin_ws/devel/lib/python2.7/dist-packages/turtlebot3_autorace_camera/cfg")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/himsangseung/catkin_ws/build/turtlebot3_autorace/turtlebot3_autorace_camera/catkin_generated/installspace/turtlebot3_autorace_camera.pc")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/turtlebot3_autorace_camera/cmake" TYPE FILE FILES
    "/home/himsangseung/catkin_ws/build/turtlebot3_autorace/turtlebot3_autorace_camera/catkin_generated/installspace/turtlebot3_autorace_cameraConfig.cmake"
    "/home/himsangseung/catkin_ws/build/turtlebot3_autorace/turtlebot3_autorace_camera/catkin_generated/installspace/turtlebot3_autorace_cameraConfig-version.cmake"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/turtlebot3_autorace_camera" TYPE FILE FILES "/home/himsangseung/catkin_ws/src/turtlebot3_autorace/turtlebot3_autorace_camera/package.xml")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/turtlebot3_autorace_camera" TYPE PROGRAM FILES "/home/himsangseung/catkin_ws/build/turtlebot3_autorace/turtlebot3_autorace_camera/catkin_generated/installspace/image_compensation")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/turtlebot3_autorace_camera" TYPE PROGRAM FILES "/home/himsangseung/catkin_ws/build/turtlebot3_autorace/turtlebot3_autorace_camera/catkin_generated/installspace/image_projection")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/turtlebot3_autorace_camera" TYPE DIRECTORY FILES
    "/home/himsangseung/catkin_ws/src/turtlebot3_autorace/turtlebot3_autorace_camera/calibration"
    "/home/himsangseung/catkin_ws/src/turtlebot3_autorace/turtlebot3_autorace_camera/cfg"
    "/home/himsangseung/catkin_ws/src/turtlebot3_autorace/turtlebot3_autorace_camera/data"
    "/home/himsangseung/catkin_ws/src/turtlebot3_autorace/turtlebot3_autorace_camera/launch"
    )
endif()

