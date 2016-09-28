cmake_minimum_required(VERSION 2.8)

project (cpp_example)
set(CMAKE_BUILD_TYPE Release)

execute_process(COMMAND bash "-c" "python -c 'import tensorflow as tf; print(tf.sysconfig.get_include())'" OUTPUT_VARIABLE TF_INC)

set(CMAKE_CXX_FLAGS  "-fPIC -D_GLIBCXX_USE_CXX11_ABI=0")
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")

message(STATUS ${TF_INC})

include_directories(${TF_INC})
add_library(cpp_example SHARED example.cc)
