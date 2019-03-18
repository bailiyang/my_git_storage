cmake_minimum_required(VERSION 2.8)

# *********************** Required *************************
project(test)
set(TARGET kiev_test)
# **********************************************************

set(CMAKE_CXX_COMPILER "g++")
set(CMAKE_CXX_FLAGS "-g -O3 -std=c++0x -Wall -Werror")

add_executable(kiev_test src/test.cpp)
target_link_libraries(kiev_test -lsnappy -lopenssl -luuid -pthread -lssl -lcrypto -lz -ldl -static)
