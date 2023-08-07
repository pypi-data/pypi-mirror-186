from distutils.core import setup, Extension
from pathlib import Path, PurePath

# source files for sicgl
sicgl_root_dir = "third-party/sicgl"
sicgl_include_dirs = list(
    str(PurePath(sicgl_root_dir, include))
    for include in [
        "include",
    ]
)
sicgl_sources = list(
    str(PurePath(sicgl_root_dir, "src", source))
    for source in [
        "blit.c",
        "color_sequence.c",
        "compose.c",
        "field.c",
        "gamma.c",
        "iter.c",
        "screen.c",
        "translate.c",
        "domain/global.c",
        "domain/interface.c",
        "domain/screen.c",
        "private/direct.c",
        "private/interpolation.c",
    ]
)

pysicgl_root_dir = "."
pysicgl_include_dirs = list(
    str(PurePath(pysicgl_root_dir, include))
    for include in [
        "include",
    ]
)
pysicgl_sources = list(
    str(PurePath(pysicgl_root_dir, "src", source))
    for source in [
        "module.c",
        "color.c",
        "color_sequence.c",
        "field.c",
        "interface.c",
        "screen.c",
        "utilities.c",
        "drawing/blit.c",
        "drawing/compose.c",
        "drawing/field.c",
        "drawing/interface.c",
        "drawing/screen.c",
        "drawing/global.c",
    ]
)

pysicgl = Extension(
    "pysicgl",
    include_dirs=[*pysicgl_include_dirs, *sicgl_include_dirs],
    sources=[*pysicgl_sources, *sicgl_sources],
)

setup(
    ext_modules=[pysicgl],
    setup_requires=["setuptools_scm"],
)
