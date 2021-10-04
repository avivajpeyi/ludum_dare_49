#!/usr/bin/env python
# Inspired by:
# https://hynek.me/articles/sharing-your-labor-of-love-pypi-quick-and-dirty/

import os

from setuptools import find_packages, setup

# PROJECT SPECIFIC

PROJ_NAME = "dot_blaster"


SRC_CODE_DIR = "gamelib"
PACKAGES = find_packages(SRC_CODE_DIR)
print(PACKAGES)

CLASSIFIERS = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "Intended Audience :: Science/Research",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
]
INSTALL_REQUIRES = ["pygame>2.0.0", "package_version", "pygame-menu", "numpy"]
EXTRA_REQUIRES = [
    "pyinstaller",
    "interrogate",
    "pytest>=3.6",
    "pre-commit",
    "flake8",
    "black",
    "isort",
]


def version():
    """Method to help set version"""
    v = os.getenv("PYTHON_PACKAGE_VERSION")
    if v is None:
        try:
            from package_version import PackageVersion

            pv = PackageVersion()
            v = pv.generate_next_stable(package_name=PROJ_NAME)
        except ImportError:
            v = "1.0.0"
    return v


setup(
    name=PROJ_NAME,
    version=version(),
    description="Ludum Dare 49 game",
    author="Avi + Reinhold",
    author_email="avi.vajpeyi@gmail.com",
    url="https://github.com/avivajpeyi/dot_blaster",
    packages=PACKAGES,
    package_data={PROJ_NAME: ["assets/*"]},
    # When your source code is in a subdirectory under the project root, e.g.
    # `src/`, it is necessary to specify the `package_dir` argument.
    package_dir={"": SRC_CODE_DIR},
    include_package_data=True,
    install_requires=INSTALL_REQUIRES,
    classifiers=CLASSIFIERS,
    zip_safe=True,
    entry_points={
        "console_scripts": [
            f"play_dot_blaster={PROJ_NAME}.main:main",
        ]
    },
)
