import os
import shutil
import subprocess
import tarfile
import urllib.request
from dataclasses import dataclass
from pathlib import Path

PWD = Path(os.path.dirname(os.path.abspath(__file__)))
DST = PWD / ".ext_deps"

CMAKE_OPTS = [
    "-DCMAKE_PREFIX_PATH=",
    "-DCMAKE_BUILD_TYPE=Release",
    "-DBUILD_SHARED_LIBS=ON",
]

CPM_OPTS = ["-DCPM_USE_LOCAL_PACKAGES=ON"]


@dataclass
class Dependency:
    user: str
    project: str
    version: str
    cmake_opts: list[str]


DEPS = [
    Dependency("horta", "logaddexp", "2.1.14", CMAKE_OPTS),
    Dependency("horta", "elapsed", "3.1.2", CMAKE_OPTS),
    Dependency("EBI-Metagenomics", "lip", "0.5.0", CMAKE_OPTS),
    Dependency("EBI-Metagenomics", "hmr", "0.6.0", CMAKE_OPTS),
    Dependency("EBI-Metagenomics", "imm", "2.1.10", CMAKE_OPTS + CPM_OPTS),
    Dependency("EBI-Metagenomics", "deciphon", "0.3.6", CMAKE_OPTS + CPM_OPTS),
]


def rm(folder: Path, pattern: str):
    for filename in folder.glob(pattern):
        filename.unlink()


def get_cmake_bin():
    from cmake import CMAKE_BIN_DIR

    bins = [str(v) for v in Path(CMAKE_BIN_DIR).glob("cmake*")]
    return bins[0]


def cleanup_intree_artifacts():
    rm(PWD / "deciphon", "cffi.*")
    rm(PWD / "deciphon", "*.o")
    rm(PWD / "deciphon", "*.so")
    rm(PWD / "deciphon", "*.dylib")


def cleanup_ext_deps():
    shutil.rmtree(DST, ignore_errors=True)


def build_dep(dep: Dependency):
    ext_dir = DST

    prj_dir = ext_dir / f"{dep.project}-{dep.version}"
    build_dir = prj_dir / "build"
    os.makedirs(build_dir, exist_ok=True)

    url = f"https://github.com/{dep.user}/{dep.project}/archive/refs/tags/v{dep.version}.tar.gz"

    with urllib.request.urlopen(url) as rf:
        data = rf.read()

    tar_filename = f"{dep.project}-{dep.version}.tar.gz"

    with open(ext_dir / tar_filename, "wb") as lf:
        lf.write(data)

    with tarfile.open(ext_dir / tar_filename) as tf:
        tf.extractall(ext_dir)

    cmake_bin = get_cmake_bin()
    subprocess.check_call(
        [cmake_bin, "-S", str(prj_dir), "-B", str(build_dir)] + dep.cmake_opts
    )
    subprocess.check_call([cmake_bin, "--build", str(build_dir), "--config", "Release"])
    subprocess.check_call(
        [cmake_bin, "--install", str(build_dir), "--prefix", str(ext_dir)]
    )


if __name__ == "__main__":
    from cffi import FFI

    ffibuilder = FFI()

    cleanup_intree_artifacts()
    cleanup_ext_deps()

    for dep in DEPS:
        build_dep(dep)

    library_dirs = [DST / "lib", DST / "lib64"]
    include_dirs = [DST / "include"]

    with open(PWD / "deciphon" / "interface.h", "r") as f:
        interface_h = f.read()

    ffibuilder.cdef(interface_h)
    ffibuilder.set_source(
        "deciphon.cffi",
        """
        #include "deciphon/deciphon.h"
        """,
        language="c",
        libraries=["deciphon"],
        library_dirs=[str(d) for d in library_dirs if d.exists()],
        include_dirs=[str(d) for d in include_dirs if d.exists()],
    )
    ffibuilder.compile(verbose=True)
