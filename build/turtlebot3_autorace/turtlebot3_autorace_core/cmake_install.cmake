# Install script for directory: /home/himsangseung/catkin_ws/src/turtlebot3_autorace/turtlebot3_autorace_core

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
  include("/home/himsangseung/catkin_ws/build/turtlebot3_autorace/turtlebot3_autorace_core/catkin_generated/safe_execute_install.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/himsangseung/catkin_ws/build/turtlebot3_autorace/turtlebot3_autorace_core/catkin_generated/installspace/turtlebot3_autorace_core.pc")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/turtlebot3_autorace_core/cmake" TYPE FILE FILES
    "/home/himsangseung/catkin_ws/build/turtlebot3_autorace/turtlebot3_autorace_core/catkin_generated/installspace/turtlebot3_autorace_coreConfig.cmake"
    "/home/himsangseung/catkin_ws/build/turtlebot3_autorace/turtlebot3_autorace_core/catkin_generated/installspace/turtlebot3_autorace_coreConfig-version.cmake"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/turtlebot3_autorace_core" TYPE FILE FILES "/home/himsangseung/catkin_ws/src/turtlebot3_autorace/turtlebot3_autorace_core/package.xml")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/turtlebot3_autorace_core" TYPE PROGRAM FILES "/home/himsangseung/catkin_ws/build/turtlebot3_autorace/turtlebot3_autorace_core/catkin_generated/installspace/core_mode_decider")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/turtlebot3_autorace_core" TYPE PROGRAM FILES "/home/himsangseung/catkin_ws/build/turtlebot3_autorace/turtlebot3_autorace_core/catkin_generated/installspace/core_node_controller")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/turtlebot3_autorace_core" TYPE PROGRAM FILES "/home/himsangseung/catkin_ws/build/turtlebot3_autorace/turtlebot3_autorace_core/catkin_generated/installspace/core_node_mission")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/turtlebot3_autorace_core" TYPE DIRECTORY FILES "/home/himsangseung/catkin_ws/src/turtlebot3_autorace/turtlebot3_autorace_core/launch")
endif()

