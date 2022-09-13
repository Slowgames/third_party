# third_party

Scripts and docs for building/collecting third_party dependencies.

## Building

You generally need to have all dependencies and possess a toolchain for compiling software. The build script here
isn't going to perform any magic tricks. The entire idea here is that we build with some consistency.


```bash
git clone --recursive https://github.com/slowgames/third_party.git

cd third_party

python3 build.py
```

### Windows

In all likelihood you will need to run this from a visual studio developer shell. (I personally use Powershell)


## Using released builds in a CMake project

```cmake
include(FetchContent)

set(_version v2022.02)

set(_github_release "https://github.com/Slowgames/third_party/releases/download/${_version}")

set(_platform ${CMAKE_HOST_SYSTEM_NAME})
set(_arch ${CMAKE_HOST_SYSTEM_PROCESSOR})
set(_archive_ext tar.bz2)
if (WIN32)
    set(_archive_ext zip)
endif()

macro(ThirdParty_Declare NAME)
    FetchContent_Declare(
        ${NAME}
        URL "${_github_release}/${NAME}-${_platform}-${_arch}.${_archive_ext}"
    )
    list(APPEND CMAKE_PREFIX_PATH ${CMAKE_BINARY_DIR}/_deps/${NAME}-src)
endmacro(ThirdParty_Declare)

ThirdParty_Declare(argparse)
ThirdParty_Declare(cglm)
ThirdParty_Declare(flecs)
ThirdParty_Declare(sdl2)
ThirdParty_Declare(bgfx)

FetchContent_MakeAvailable(argparse cglm flecs sdl2 bgfx)

find_package(SDL2 CONFIG REQUIRED GLOBAL)
find_package(cglm CONFIG REQUIRED GLOBAL)
find_package(flecs CONFIG REQUIRED GLOBAL)
find_package(bgfx CONFIG REQUIRED GLOBAL)
find_package(argparse CONFIG REQUIRED GLOBAL)
```

## Ideas?

One thing that sure seems pretty interesting to me is to build everything with `zig cc`.
