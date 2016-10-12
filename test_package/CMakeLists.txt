project(testproj)
cmake_minimum_required(VERSION 3.0)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

# This will produce 'relocatable' binaries under OS X on 'make install', that will look for dylibs
# in the executable path.
set(CMAKE_SKIP_RPATH OFF)
set(CMAKE_INSTALL_RPATH "@executable_path")

add_executable(testproj test.cpp)

target_link_libraries(testproj ${CONAN_LIBS})
