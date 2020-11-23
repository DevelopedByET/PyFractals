from setuptools import setup
from Cython.Build import cythonize

setup(
    name='JuliaSet using Cython',
    ext_modules=cythonize("juliasetcython.pyx"),
    zip_safe=False,
)