from setuptools import find_packages, setup, Extension

from Cython.Build import cythonize
import Cython.Compiler.Options

extensions = [
    # A single module that is stand alone and has no special requisites
    Extension("test_sys_executable_vs_capi.test_sys_executable", ["test_sys_executable_vs_capi/test_sys_executable.pyx"]),
]

# See https://cython.readthedocs.io/en/latest/src/userguide/source_files_and_compilation.html
# for a deeper explanation of the choices here
Cython.Compiler.Options.docstring = False
Cython.Compiler.Options.error_on_uninitialized = True
directives = {
    "language_level": "3",  # We assume Python 3 code
    "boundscheck": False,  # Do not check array access
    "wraparound": False,  # a[-1] does not work
    "embedsignature": False,  # Do not save typing / docstring
    "always_allow_keywords": False,  # Faster calling conventions
    "initializedcheck": False,  # We assume memory views are initialized
}

setup(
    name="test_sys_executable_vs_capi",
    version="0.1.1",
    packages=["test_sys_executable_vs_capi"],
    author="Florian Finkernagel",
    author_email="finkernagel@imt.uni-marburg.de",
    description="Verify that sys.executable and Py_GetProgramFullPath are in agreement",
    url="https://github.com/TyberiusPrime/test_sys_executable_vs_capi",
    ext_modules=cythonize(extensions, compiler_directives=directives),
    install_requires=[
    ],
)
