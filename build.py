#!python3

import os
import sys
from pathlib import Path
from typing import List
import subprocess


class Builder(object):
    def __init__(self):
        self.repo_root = Path(__file__).parent
        self.build_root = self.__make_output_dir("build")
        self.install_root = self.__make_output_dir("install")
        self.release_dir = self.__make_output_dir("release")

    def __make_output_dir(self, name: str) -> Path:
        output_dir = self.repo_root / name
        output_dir.mkdir(exist_ok=True)
        return output_dir

    def build_repo(self, name: str, extra_cmake_options: List[str] = []) -> bool:
        result = True

        source_dir = self.repo_root / name
        build_dir = self.build_root / name
        install_dir = self.install_root / name

        if build_dir.exists():
            from shutil import rmtree
            rmtree(build_dir)

        build_dir.mkdir(exist_ok=True)

        configure_cmd = [
            "cmake",
            "-G", "\"Visual Studio 17 2022\"",
            "-A", "x64",
            f"-DCMAKE_INSTALL_PREFIX={str(install_dir)}",
        ] + extra_cmake_options
        configure_cmd.append(str(source_dir))
        configure_cmd = " ".join(configure_cmd)

        try:
            os.chdir(build_dir)

            print(f"===== Configuring {name} =====")
            print(configure_cmd)

            configure_res = subprocess.run(configure_cmd)
            configure_res.check_returncode()

            build_res = subprocess.run("cmake --build . --config Release --target INSTALL")
            build_res.check_returncode()

        except Exception as err:
            import traceback
            result = False
            traceback.print_exception(err)
            sys.stderr.writelines(f"*** Failed to build {name} ***\n")
        finally:
            os.chdir(self.repo_root)

        print("\n")
        return result

    def package_release(self, name: str) -> bool:
        result = True

        install_dir = self.install_root / name

        try:
            os.chdir(install_dir)
            subprocess.run(f"powershell Compress-Archive . {name}-Windows-x64.zip")
        except Exception as err:
            import traceback
            result = False
            traceback.print_exception(err)
            sys.stderr.writelines(f"*** Failed to build {name} release archive ***\n")
        finally:
            os.chdir(self.repo_root)

        return result


def main() -> int:
    builder = Builder()

    bx_dir = str(builder.repo_root / 'bx').replace('\\','/')
    bimg_dir = str(builder.repo_root / 'bimg').replace('\\','/')
    bgfx_dir = str(builder.repo_root / 'bgfx').replace('\\','/')

    projects = [
        ("argparse", []),
        ("cglm", ["-DCGLM_STATIC=ON", "-DCGLM_SHARED=OFF"]),
        ("SDL2", []),
        ("flecs", []),
        ("bgfx.cmake", [
            f"-DBX_DIR={bx_dir}",
            f"-DBIMG_DIR={bimg_dir}",
            f"-DBGFX_DIR={bgfx_dir}",
        ]),
    ]

    for name, extra_args in projects:
        # if not builder.build_repo(name, extra_args):
        #     return 1
        if not builder.package_release(name):
            return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
