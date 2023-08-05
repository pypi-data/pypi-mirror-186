project (cork64)

cmake_minimum_required (VERSION 3.1)

set (CMAKE_CXX_STANDARD 14)

# set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} ./cmake)
# include(muspectreTools)
# add_external_package(gmp)

if (NOT CMAKE_BUILD_TYPE)
  set(CMAKE_BUILD_TYPE "Release")
endif()


include_directories(
  "."
  "./src/accel"
  "./src/file_formats"
  "./src/isct"
  "./src/math"
  "./src/mpz"
  "./src/mesh"
  "./src/rawmesh"
  "./src/util"
  "./src/tetgen")

# set (CMAKE_STATIC_COMPILER "g++-7)
# set (CMAKE_CC_COMPILER "clang")
set (CMAKE_CC_FLAGS  "-w -Wno-conversion ${INC} -g -fPIC")


# set (CMAKE_CXX_COMPILER "clang++")
set (CMAKE_CXX_FLAGS  "-w -Wno-conversion ${INC} -g -DTETLIBRARY -fPIC")


add_subdirectory("./src")

# add_executable(cork_exe "./src/main.cpp")
# target_link_libraries(cork_exe PUBLIC corkpp)

# add_executable(cork_no "./src/main_no.cpp")
# target_link_libraries(cork_no PUBLIC corkpp)
