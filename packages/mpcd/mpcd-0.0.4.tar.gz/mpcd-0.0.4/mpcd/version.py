from os.path import join as pjoin

# Format expected by setup.py and doc/source/conf.py: string of form "X.Y.Z"
_version_major = 0
_version_minor = 1
_version_micro = 1  # use '' for first of series, number for 1 and above
_version_extra = None  # Uncomment this for full releases

# Construct full version string from these.
_ver = [_version_major, _version_minor]
if _version_micro:
    _ver.append(_version_micro)
if _version_extra:
    _ver.append(_version_extra)

__version__ = '.'.join(map(str, _ver))

CLASSIFIERS = ["Development Status :: 3 - Alpha",
               "Environment :: Console",
               "Intended Audience :: Science/Research",
               "License :: OSI Approved :: MIT License",
               "Operating System :: OS Independent",
               "Programming Language :: Python",
               "Topic :: Scientific/Engineering"]

# Description should be a one-liner:
description = "Pure Python PCD reader/writer"

# Long description will go up on the pypi page
long_description = """\
mpcd
========
Folk from pypcd, https://github.com/dimatura/pypcd

Pure Python reader/writer for the PCL ``pcd`` data format for point clouds.

Please go to the repository README_.

License
=======
``mpcd`` is licensed under the terms of the MIT license. See the file
"LICENSE" for information on the history of this software, terms & conditions
for usage, and a DISCLAIMER OF ALL WARRANTIES.

All trademarks referenced herein are property of their respective holders.

Copyright (c) 2015--, Yuehao Wang
"""

NAME = "mpcd"
MAINTAINER = "Yuehao Wang"
MAINTAINER_EMAIL = "mail@yuehao.wang"
DESCRIPTION = description
LONG_DESCRIPTION = long_description
URL = ""
DOWNLOAD_URL = ""
LICENSE = "MIT"
AUTHOR = "Yuehao Wang"
AUTHOR_EMAIL = "mail@yuehao.wang"
PLATFORMS = "OS Independent"
MAJOR = _version_major
MINOR = _version_minor
MICRO = _version_micro
VERSION = __version__
PACKAGES = ['mpcd',
            'mpcd.tests']
PACKAGE_DATA = {'mpcd': [pjoin('data', '*')]}
INSTALL_REQUIRES = ["numpy", "python-lzf","Pillow","opencv-python"]
