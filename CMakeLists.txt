cmake_minimum_required(VERSION 3.28)

project(third_party)

add_subdirectory(src/SDL3)

add_subdirectory(src/shaderc)

add_subdirectory(src/SPIRV-Cross)

if (NOT CMAKE_CROSS_COMPILING)
    add_subdirectory(src/msdfgen)
    add_subdirectory(src/msdf-atlas-gen)
endif()
