from setuptools import setup
from Cython.Build import cythonize

setup(
	name = "CustomTkinterTitlebar",
	ext_modules = cythonize("custom.pyx"),
	zip_safe = False
)
