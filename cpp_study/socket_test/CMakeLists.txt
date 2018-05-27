cmake_minimum_required(VERSION 2.8)

# *********************** Required *************************
project(test)
set(BUILD_COMMON_DIR /build/push/build)
set(TARGET kiev_test)
set(KIEV_DIR /build/push)
include(${BUILD_COMMON_DIR}/nebula_common.cmake)
# **********************************************************

set(CMAKE_CXX_COMPILER "g++")
set(CMAKE_CXX_FLAGS "-g -O3 -std=c++0x -Wall -Werror")

include_directories("${KIEV_DIR}/push/proto")
link_directories("${KIEV_DIR}/push/proto")
include_directories("${KIEV_DIR}/stream/proto")
link_directories("${KIEV_DIR}/stream/proto")

AUX_SOURCE_DIRECTORY("${PROJECT_SOURCE_DIR}/src" SRC_LIST)
add_executable(${TARGET} ${SRC_LIST})
target_link_libraries(${TARGET} -lst -lmetaq -lkiev -lmq_push_data_report
    -lpush_data_report -lprotobuf -lsnappy -luuid -pthread -lcurl -lcares
    -lssl -lcrypto -lz -ldl -static)

#ADD_SUBDIRECTORY(gtest)
