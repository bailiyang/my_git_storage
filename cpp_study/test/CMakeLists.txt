cmake_minimum_required(VERSION 2.8)

# *********************** Required *************************
project(test)
set(TARGET kiev_test)
# **********************************************************

set(CMAKE_CXX_COMPILER "g++")
set(CMAKE_CXX_FLAGS "-g -O3 -std=c++0x -Wall -Werror")

AUX_SOURCE_DIRECTORY("${PROJECT_SOURCE_DIR}/src" SRC_LIST)
add_executable(${TARGET} ${SRC_LIST})
target_link_libraries(${TARGET} -lsnappy -luuid -pthread -lcurl -lssl -lcrypto -lz -ldl -static)
