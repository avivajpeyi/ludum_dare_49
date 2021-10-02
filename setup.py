#!/usr/bin/env python
# Inspired by:
# https://hynek.me/articles/sharing-your-labor-of-love-pypi-quick-and-dirty/

import os

from setuptools import find_packages, setup

# PROJECT SPECIFIC

NAME = "ludum_dare_49"
PACKAGES = find_packages(where="gamelib")
SRC = "gamelib"
CLASSIFIERS = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "Intended Audience :: Science/Research",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
]
INSTALL_REQUIRES = ["pygame>2.0.0"]
EXTRA_REQUIRE = {"test": ["pytest>=3.6"]}
EXTRA_REQUIRE["dev"] = EXTRA_REQUIRE["test"] + [
    "pre-commit",
    "flake8",
    "black",
    "isort",
    "package_version",
]


def version():
    """Method to help set version"""
    v = os.getenv("PYTHON_PACKAGE_VERSION")
    if v is None:
        try:
            from package_version import PackageVersion

            pv = PackageVersion()
            v = pv.generate_next_stable(package_name=NAME)
        except ImportError:
            v = "1.0.0"
    return v


setup(
    name=NAME,
    version=version(),
    description="Ludum Dare 49 game",
    author="Avi + Reinhold",
    author_email="avi.vajpeyi@gmail.com",
    url="https://github.com/avivajpeyi/ludum_dare_49",
    packages=PACKAGES,
    package_data={SRC: ["assets/*"]},
    package_dir={"": SRC},
    include_package_data=True,
    install_requires=INSTALL_REQUIRES,
    extras_require=EXTRA_REQUIRE,
    classifiers=CLASSIFIERS,
    zip_safe=True,
)
