cmake_minimum_required(VERSION 3.0)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

FILE(GLOB SRC_FILES wiringPi/wiringPi/*.c)

add_library(wiringPi ${SRC_FILES})
target_include_directories(wiringPi PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/wiringPi/wiringPi)
target_link_libraries(wiringPi ${CONAN_LIBS})
