#! /bin/bash

set -e

cmake -B build/shadercross \
      -S src/SDL_gpu_shadercross \
      -G 'Ninja Multi-Config' \
      -DCMAKE_DEBUG_POSTFIX="_debug" \
      -DCMAKE_PREFIX_PATH=`pwd`/dist/x86_64-linux \
      -DCMAKE_INSTALL_PREFIX=`pwd`/dist/x86_64-linux \
      -DENABLE_INSTALL=ON \
      -DENABLE_INSTALL_DEPS=ON

cmake --build build/shadercross --config Debug --target install

cmake --build build/shadercross --config Release --target install

