from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

import numpy

ext = Extension(
    "mdb", ["mdb.pyx"],
    include_dirs=[numpy.get_include()]
)

setup(
    ext_modules=[ext],
    name='Mandelbrot using Cython',
    cmdclass={'build_ext': build_ext},
    zip_safe=False
)
