# -*- coding: utf-8 -*-
from distutils.core import setup
import libnmap

with open("README.rst") as rfile:
    long_description = rfile.read()

setup(
    name="python-libnmap",
    version=libnmap.__version__,
    author="0xdade",
    author_email="dade@actualcrimes.org",
    packages=["libnmap", "libnmap.plugins", "libnmap.objects"],
    url="http://pypi.python.org/pypi/python-libnmap/",
    license='Creative Common "Attribution" license (CC-BY) v3',
    description=(
        "Python NMAP library enabling you to start async nmap tasks, "
        "parse and compare/diff scan results"
    ),
    long_description=long_description,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: System :: Networking",
    ],
    install_requires=["defusedxml"],
)
