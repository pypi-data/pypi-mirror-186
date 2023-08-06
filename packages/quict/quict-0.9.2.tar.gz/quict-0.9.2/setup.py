"""
Some codes below are from pybind11 cmake example:
https://github.com/pybind/cmake_example/blob/0baee7e073a9b3738052f543e6bed412aaa22750/setup.py
"""

import os
import platform
import subprocess
import sys
from os import getcwd, path
from typing import List, Tuple
from glob import glob

import pybind11
from setuptools import Extension, find_packages, setup
from setuptools.command.build_ext import build_ext

pybind11_cmake_dir = pybind11.__path__[0]
for p in ["share", "cmake", "pybind11"]:
    pybind11_cmake_dir = path.join(pybind11_cmake_dir, p)

# print helpers
def print_segment():
    print("\033[92m", "=" * 80, "\033[39m", sep="")


def print_cyan(segment):
    print(f"\033[36m{segment}\033[39m")


def print_magenta(segment):
    print(f"\033[95m{segment}\033[39m")


def print_yellow(segment):
    print(f"\033[33m{segment}\033[39m")


def print_if_not_none(segment):
    if segment:
        print(segment)


def print_with_wrapper(header, out_obj):
    if header[0] != "\033":
        if len(header) > 12:
            header = header[:9] + "..."
        if len(header) < 12:
            for _ in range(12 - len(header)):
                header += "."

        header = f"\033[36m[{header}]\033[39m "

    if out_obj is None:
        return
    if isinstance(out_obj, str):
        print(header, out_obj)
    else:
        for line in iter(out_obj.readline, b""):
            print(header, line.decode("utf-8"), sep="", end="")


def run_with_output_wrapper(header, args, cwd, shell=(platform.system() == "Windows")):
    if len(header) > 12:
        header = header[:9] + "..."
    if len(header) < 12:
        for _ in range(12 - len(header)):
            header += "."

    header = f"\033[36m[{header}]\033[39m "

    with subprocess.Popen(
        args=args,
        cwd=cwd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        # In Linux, execute in shell cause cmake errors...
        shell=shell,
        # universal_newlines=True,
    ) as proc:
        print_with_wrapper(header, proc.stdout)
        ret_code = proc.wait()
    if ret_code:
        raise subprocess.CalledProcessError(ret_code, args)


# Detect if I'm in `root` or `root/build`
PY_FILE_PATH = path.dirname(path.abspath(__file__))

PRJ_ROOT_RELATIVE = "." if getcwd() == PY_FILE_PATH else ".."
PRJ_ROOT = path.abspath(PRJ_ROOT_RELATIVE)

# Convert distutils Windows platform specifiers to CMake -A arguments
PLAT_TO_CMAKE = {
    "win32": "Win32",
    "win-amd64": "x64",
    "win-arm32": "ARM",
    "win-arm64": "ARM64",
}


# A CMakeExtension needs a source dir instead of a file list.
# The name must be the _single_ output extension from the CMake build.
class CMakeExtension(Extension):
    def __init__(self, name, source_dir, extra_cmake_macro=None):
        Extension.__init__(self, name, sources=[])
        self.source_dir = os.path.abspath(source_dir)
        self.extra_cmake_macro = extra_cmake_macro


class ExtensionBuild(build_ext):
    def build_extension(self, ext):
        if isinstance(ext, CMakeExtension):
            self.cmake_build_extension(ext)

    def prepare_cmake_args(
        self, cmake_generator: str, ext_dir: str, cfg: str
    ) -> Tuple[List[str], List[str]]:
        configure_args = []
        build_args = []
        # Set Python_EXECUTABLE instead if you use PYBIND11_FINDPYTHON
        # EXAMPLE_VERSION_INFO shows you how to pass a value into the C++ code
        # from Python.
        configure_args = [
            f"-DCMAKE_LIBRARY_OUTPUT_DIRECTORY={ext_dir}",
            f"-DPYTHON_EXECUTABLE={sys.executable}",
            f'-DBUILD_VERSION_INFO="{self.distribution.get_version()}"',
            f"-DCMAKE_BUILD_TYPE={cfg}",  # not used on MSVC, but no harm
            f"-Dpybind11_DIR={pybind11_cmake_dir}",
        ]
        build_args = []

        if self.compiler.compiler_type != "msvc":
            if not cmake_generator:
                configure_args += ["-GUnix Makefiles"]
        else:
            # Ensure CC/CXX is set. This is a fix for Windows PowerShell
            if "CC" in os.environ:
                configure_args += [
                    f"\"-DCMAKE_C_COMPILER:FILEPATH={os.environ['CC']}\""
                ]
            if "CXX" in os.environ:
                configure_args += [
                    f"\"-DCMAKE_CXX_COMPILER:FILEPATH={os.environ['CXX']}\""
                ]
            # Single config generators are handled "normally"
            single_config = any(x in cmake_generator for x in ("NMake", "Ninja"))

            # CMake allows an arch-in-generator style for backward compatibility
            contains_arch = any(x in cmake_generator for x in ("ARM", "Win64"))

            # Specify the arch if using MSVC generator, but only if it doesn't
            # contain a backward-compatibility arch spec already in the
            # generator name.
            if not single_config and not contains_arch:
                configure_args += ["-A", PLAT_TO_CMAKE[self.plat_name]]

            # Multi-config generators have a different way to specify configs
            if not single_config:
                configure_args += [
                    f"-DCMAKE_LIBRARY_OUTPUT_DIRECTORY_{cfg.upper()}={ext_dir}"
                ]
                build_args += ["--config", cfg]
            # Set CMAKE_BUILD_PARALLEL_LEVEL to control the parallel build level
            # across all generators.
            if "CMAKE_BUILD_PARALLEL_LEVEL" not in os.environ:
                # self.parallel is a Python 3 only way to set parallel jobs by hand
                # using -j in the build_ext call, not supported by pip or PyPA-build.
                if hasattr(self, "parallel") and self.parallel:
                    # CMake 3.12+ only.
                    build_args += [f"-j{self.parallel}"]
        return configure_args, build_args

    def cmake_build_extension(self, ext):
        ext_dir = os.path.abspath(os.path.dirname(self.get_ext_fullpath(ext.name)))

        # required for auto-detection of auxiliary "native" libs
        if not ext_dir.endswith(os.path.sep):
            ext_dir += os.path.sep

        cfg = "Debug" if self.debug else "Release"

        # CMake lets you override the generator - we need to check this.
        # Can be set with Conda-Build, for example.
        cmake_generator = os.environ.get("CMAKE_GENERATOR", "")

        configure_args, build_args = self.prepare_cmake_args(
            cmake_generator, ext_dir, cfg
        )

        ext_name = ext.name
        if ext_name[-1] == ".":
            ext_name = ext_name[:-1]
        build_temp = f"{self.build_temp}.{ext_name}"
        ext_name_split = ext_name.split(".")
        ext_name = ext_name_split[-1]

        if not os.path.exists(build_temp):
            os.makedirs(build_temp)

        if hasattr(self, "parallel") and self.parallel:
            print_yellow(
                "Extensions are built in parallel. Shell output might be messed up."
            )
        print_cyan(f"[{ext_name}]")
        cmake_cmd = ["cmake"] + configure_args + [f"-S{ext.source_dir}"]
        print_with_wrapper(ext_name, " ".join(cmake_cmd))
        print_with_wrapper(ext_name, "Configuring...")
        run_with_output_wrapper(
            header=ext_name,
            args=cmake_cmd,
            cwd=build_temp,
        )
        print_with_wrapper(ext_name, "Building...")
        run_with_output_wrapper(
            header=ext_name,
            args=["cmake", "--build", "."] + build_args,
            cwd=build_temp,
        )
        libs = []
        for file in os.listdir(ext_dir):
            if file.endswith(".so") or file.endswith(".pyd"):
                libs.append(f"{ext_dir}{file}")
        print_with_wrapper(ext_name, f"Copying back {libs}...")
        run_with_output_wrapper(
            header=ext_name,
            args=["cp", " ".join(libs), ext.source_dir],
            cwd=build_temp,
        )


# static file
file_data = [
    ("QuICT/lib/qasm/libs", [f"{PRJ_ROOT_RELATIVE}/QuICT/lib/qasm/libs/qelib1.inc"]),
    ("QuICT/simulation/utils", [f"{PRJ_ROOT_RELATIVE}/QuICT/simulation/utils/simulator_parameters.json"]),
    ("QuICT/tools/cli/template", [f"{PRJ_ROOT_RELATIVE}/QuICT/tools/cli/template/quict_job.yml"]),
    ("QuICT/lib/circuitlib", [f"{PRJ_ROOT_RELATIVE}/QuICT/lib/circuitlib/circuit_library.db"]),
    ("QuICT/lib/circuitlib/template", glob(f"{PRJ_ROOT_RELATIVE}/QuICT/lib/circuitlib/template/*")),
    ("QuICT/lib/circuitlib/algorithm/adder", glob(f"{PRJ_ROOT_RELATIVE}/QuICT/lib/circuitlib/algorithm/adder/*")),
    ("QuICT/lib/circuitlib/algorithm/clifford", glob(f"{PRJ_ROOT_RELATIVE}/QuICT/lib/circuitlib/algorithm/clifford/*")),
    ("QuICT/lib/circuitlib/algorithm/cnf", glob(f"{PRJ_ROOT_RELATIVE}/QuICT/lib/circuitlib/algorithm/cnf/*")),
    ("QuICT/lib/circuitlib/algorithm/grover", glob(f"{PRJ_ROOT_RELATIVE}/QuICT/lib/circuitlib/algorithm/grover/*")),
    ("QuICT/lib/circuitlib/algorithm/maxcut", glob(f"{PRJ_ROOT_RELATIVE}/QuICT/lib/circuitlib/algorithm/maxcut/*")),
    ("QuICT/lib/circuitlib/algorithm/qft", glob(f"{PRJ_ROOT_RELATIVE}/QuICT/lib/circuitlib/algorithm/qft/*")),
    ("QuICT/lib/circuitlib/algorithm/qnn", glob(f"{PRJ_ROOT_RELATIVE}/QuICT/lib/circuitlib/algorithm/qnn/*")),
    ("QuICT/lib/circuitlib/algorithm/quantum_walk", glob(f"{PRJ_ROOT_RELATIVE}/QuICT/lib/circuitlib/algorithm/quantum_walk/*")),
    ("QuICT/lib/circuitlib/algorithm/vqe", glob(f"{PRJ_ROOT_RELATIVE}/QuICT/lib/circuitlib/algorithm/vqe/*")),
    ("QuICT/lib/circuitlib/random/aspen-4", glob(f"{PRJ_ROOT_RELATIVE}/QuICT/lib/circuitlib/random/aspen-4/*")),
    ("QuICT/lib/circuitlib/random/ourense", glob(f"{PRJ_ROOT_RELATIVE}/QuICT/lib/circuitlib/random/ourense/*")),
    ("QuICT/lib/circuitlib/random/rochester", glob(f"{PRJ_ROOT_RELATIVE}/QuICT/lib/circuitlib/random/rochester/*")),
    ("QuICT/lib/circuitlib/random/sycamore", glob(f"{PRJ_ROOT_RELATIVE}/QuICT/lib/circuitlib/random/sycamore/*")),
    ("QuICT/lib/circuitlib/random/tokyo", glob(f"{PRJ_ROOT_RELATIVE}/QuICT/lib/circuitlib/random/tokyo/*")),
]

setup(
    name="quict",
    version="0.9.2",
    description="Quantum Compute Platform of Institute of Computing Technology",
    author="Library for Quantum Computation and Theoretical Computer Science, ICT, CAS",
    author_email="likaiqi@ict.ac.cn",
    license="Apache License 2.0",
    platforms=["Windows", "Linux", "macOS"],
    url="https://e.gitee.com/quictucas/repos/quictucas/quict",
    package_dir={"QuICT": f"{PRJ_ROOT_RELATIVE}/QuICT"},
    entry_points={
        "console_scripts": [
            "quict = QuICT.tools.cli.quict:main",
        ],
    },
    install_requires=[
        "contourpy==1.0.5",
        "cycler==0.11.0",
        "fonttools==4.37.4",
        "kiwisolver==1.4.4",
        "llvmlite==0.39.1",
        "matplotlib==3.6.1",
        "networkx==2.8.7",
        "numba==0.56.3",
        "numpy==1.23.4",
        "packaging==21.3",
        "Pillow==9.2.0",
        "ply==3.11",
        "pybind11==2.10.0",
        "pyparsing==3.0.9",
        "python-dateutil==2.8.2",
        "scipy==1.9.2",
        "six==1.16.0",
        "ujson==5.5.0",
        "pyjwt==2.6.0",
        "pycryptodome==3.16.0"
    ],
    ext_modules=[
        CMakeExtension(
            "QuICT.simulation.state_vector.cpu_simulator.",
            f"{PRJ_ROOT}/QuICT/simulation/state_vector/cpu_simulator/",
        ),
    ],
    cmdclass={"build_ext": ExtensionBuild},
    packages=find_packages(where=PRJ_ROOT_RELATIVE),
    data_files=file_data,
    include_package_data=True,
    python_requires=">=3.8",
    zip_safe=False,
)
print_segment()
