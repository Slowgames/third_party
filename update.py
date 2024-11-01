import sys, os
import subprocess

SUBTREES = [
    ("src/SDL3", "https://github.com/libsdl-org/SDL", "main"),
    ("src/msdf-atlas-gen", "https://github.com/Chlumsky/msdf-atlas-gen", "master"),
    ("src/msdfgen", "https://github.com/Chlumsky/msdfgen", "master"),
    ("src/glslang", "https://github.com/KhronosGroup/glslang", "main"),
    ("src/SPIRV-Headers", "https://github.com/KhronosGroup/SPIRV-Headers", "main"),
    ("src/SPIRV-Tools", "https://github.com/KhronosGroup/SPIRV-Tools", "main"),
    ("src/shaderc", "https://github.com/google/shaderc", "main"),
    ("src/SPIRV-Cross", "https://github.com/KhronosGroup/SPIRV-Cross", "main"),
    ("src/SDL_gpu_shadercross", "https://github.com/libsdl-org/SDL_gpu_shadercross", "master"),
]

SUBTREE_ADD_TMPL = 'git subtree add --prefix {prefix} {repo_url} {branch} --squash'
SUBTREE_PULL_TMPL = 'git subtree pull --prefix {prefix} {repo_url} {branch} --squash'


def main() -> int:
    for (prefix, repo_url, branch) in SUBTREES:
        format_args = {'prefix': prefix, 'repo_url': repo_url, 'branch': branch}

        if os.path.exists(prefix):
            cmd = SUBTREE_PULL_TMPL.format(**format_args)
        else:
            cmd = SUBTREE_ADD_TMPL.format(**format_args)

        subprocess.check_call(cmd.split())
    return 0


if __name__ == "__main__":
    sys.exit(main())
