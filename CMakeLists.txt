cmake_minimum_required(VERSION 3.0 FATAL_ERROR)
project(TwoLayerNetwork)

find_package(Torch REQUIRED)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${TORCH_CXX_FLAGS}")

add_executable(TwoLayerNetwork TwoLayerNetwork.cpp)
target_link_libraries(TwoLayerNetwork "${TORCH_LIBRARIES}")
set_property(TARGET TwoLayerNetwork PROPERTY CXX_STANDARD 14)
