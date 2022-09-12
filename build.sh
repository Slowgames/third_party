#!/bin/bash

mkdir -p build
mkdir -p install
mkdir -p release

_repo_root=`pwd`

_build_root=${_repo_root}/build
_install_root=${_repo_root}/install

_release_dir=${_repo_root}/release
mkdir -p ${_release_dir}

_platform=`uname -s`
_arch=`uname -m`



function build_repo {
    _source_dir=${_repo_root}/$1
    _build_dir=${_build_root}/$1
    _install_dir=${_install_root}/$1

    mkdir -p ${_build_dir}

    pushd ${_build_dir}

    cmake -GNinja -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=${_install_dir} ${@:2} ${_source_dir} && \
    ninja install

    popd
}


function package_release {
    _install_dir=${_install_root}/$1

    pushd ${_install_dir} && \
    tar -Jcvf ${_release_dir}/$1-${_platform}-${_arch}.tar.bz2 * && \
    popd
}



for repo in cglm flecs argparse SDL2; do
    build_repo $repo
done

build_repo bgfx.cmake -DBX_DIR=${_repo_root}/bx -DBIMG_DIR=${_repo_root}/bimg -DBGFX_DIR=${_repo_root}/bgfx

for repo in cglm flecs argparse SDL2 bgfx.cmake; do
    package_release $repo
done

mv ${_release_dir}/bgfx.cmake-${_platform}-${_arch}.tar.bz2 ${_release_dir}/bgfx-${_platform}-${_arch}.tar.bz2
