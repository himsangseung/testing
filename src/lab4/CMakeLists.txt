cmake_minimum_required(VERSION 2.8.3)
project(lab4)


find_package(OpenCV REQUIRED)

find_package(catkin REQUIRED COMPONENTS
  cv_bridge
  image_transport
  roscpp
  rospy
)



catkin_package()


include_directories(
# include
  ${catkin_INCLUDE_DIRS}
  ${OpenCV_INCLUDE_DIRS}
)



add_executable(test_cv src/test_cv.cpp)       
add_dependencies(test_cv ${test_cv_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
target_link_libraries(test_cv
   ${catkin_LIBRARIES}
   ${OpenCV_LIBRARIES}
 )

