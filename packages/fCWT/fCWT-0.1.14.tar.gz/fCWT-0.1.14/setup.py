#!/usr/bin/env python

"""
setup.py file for SWIG
"""

from setuptools import Extension, setup, find_packages
import distutils.command.build
import sysconfig
import numpy
import os
import shutil


# Obtain the numpy include directory.  This logic works across numpy versions.
try:
    numpy_include = numpy.get_include()
except AttributeError:
    numpy_include = numpy.get_numpy_include()

libraries = ['fftw3f']
comp_args = ["/arch:AVX","/O2","/openmp"]
link_args = []
files2 = [  "omp.h",
            "fftw3.h",
            "fftw3f.dll",
            "fftw3f.lib",
            "libfftw3fmac.a",
            "libfftw3f_ompmac.a",
            "libfftw3fl.so",
            "libfftw3f_ompl.so",
            "libomp.a"
        ]
files = [
            "fcwt.h",
            "fcwt.cpp"
]


if "macosx" in sysconfig.get_platform() or "darwin" in sysconfig.get_platform():
    libraries = ['fftw3fmac','fftw3f_ompmac']
    comp_args = ["-mavx","-O3"]
    link_args = ["-lomp"]

if "linux" in sysconfig.get_platform():
    libraries = ['fftw3fl','fftw3f_ompl']
    comp_args = ["-mavx","-O3"]
    link_args = ["-lomp"]

import distutils.command.build
import distutils.command.build_ext

# Override build command
class BuildCommand(distutils.command.build_ext.build_ext):

    def run(self):
        # Run the original build command
        
        print("Copying files")

        #get extension directory
        ext_dir = os.path.abspath(os.path.dirname(self.get_ext_fullpath("fcwt._fcwt")))
        print(ext_dir)

        for f in files2:
            shutil.copyfile("libs/"+f,"src/fcwt/"+f)

        distutils.command.build_ext.build_ext.run(self)

        # Custom build stuff goes here


setup (ext_modules=[
            Extension('fcwt._fcwt',
                sources=[
                    'src/fcwt/fcwt.cpp',
                    'src/fcwt/fcwt_wrap.cxx'
                ],
                library_dirs = ['src/fcwt','src'],
                include_dirs = ['src/fcwt','src',numpy_include],
                libraries = libraries,
                extra_compile_args = comp_args,
                extra_link_args = link_args
            )
        ],
        cmdclass={"build_ext": BuildCommand},
        packages=find_packages(where='src') + ['fcwt.libs'],
        package_dir={'fcwt': 'src/fcwt',
                     'fcwt.libs': 'libs'},
        package_data={'fcwt':files,
                      'fcwt.libs':files2}
        )

#swig -c++ -python fcwt-swig.i