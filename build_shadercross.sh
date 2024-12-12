#! /bin/bash

set -e

cmake -B build/shadercross \
      -S src/SDL_shadercross \
      -G 'Ninja Multi-Config' \
      -DCMAKE_DEBUG_POSTFIX="_debug" \
      -DCMAKE_PREFIX_PATH=`pwd`/dist/x86_64-linux \
      -DCMAKE_INSTALL_PREFIX=`pwd`/dist/shadercross/x86_64-linux \
      -DSDLSHADERCROSS_SPIRVCROSS_SHARED=OFF \
      -DSDLSHADERCROSS_VENDORED=ON \
      -DSDLSHADERCROSS_INSTALL=ON \
      -DSDLSHADERCROSS_SHARED=ON \
      -DSDLSHADERCROSS_INSTALL_RUNTIME=ON

# cmake --build build/shadercross --config Debug --target install

cmake --build build/shadercross --config Release --target install

