include_guard()

if (NOT DEFINED ENV{MINGW_ROOT})
    message(FATAL_ERROR "You must provide a path for MINGW.")
endif()

if (EXISTS $ENV{MINGW_ROOT})
    return()
endif()

include(FetchContent)

FetchContent_Declare(
    mingw
    URL https://github.com/Slowgames/toolchains/releases/download/2024.11.1/gcc14-x86_64-w64-mingw32.tar.xz
)

message(STATUS "Downloading mingw")
FetchContent_MakeAvailable(mingw)
