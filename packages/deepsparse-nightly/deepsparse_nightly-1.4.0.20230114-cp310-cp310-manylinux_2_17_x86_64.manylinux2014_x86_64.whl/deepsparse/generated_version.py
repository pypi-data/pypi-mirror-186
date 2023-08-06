# neuralmagic: no copyright
# flake8: noqa
# fmt: off
# isort: skip_file
__all__ = ["__version__", "version", "version_major", "version_minor", "version_bug", "version_build", "version_major_minor", "optimized", "is_release", "revision", "splash", "is_nightly", "build_date"]
__version__ = "1.4.0.20230114"

version = __version__
version_major, version_minor, version_bug, version_build = version.split(".") + (
    [None] if len(version.split(".")) < 4 else []
) # handle conditional for version being 3 parts or 4 
version_major_minor = f"{version_major}.{version_minor}"
optimized = 1
is_release = 0
is_nightly = 1
is_enterprise = 0
revision = "bdd72343"
splash = "DeepSparse, Copyright 2021-present / Neuralmagic, Inc. version: 1.4.0.20230114 (bdd72343) (release) (optimized) (system=avx2, binary=avx2)"
build_date = "20230114"
