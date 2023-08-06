cimport cython
import sys
from cpython.ref cimport PyObject 
from libc.stddef cimport wchar_t


cdef extern from "Python.h":
    # Imports definitions from a c header file
    # Corresponding source file (cfunc.c) must be added to
    # the extension definition in setup.py for proper compiling & linking

    wchar_t* Py_GetProgramFullPath()
    PyObject* PyUnicode_FromWideChar(wchar_t *w, Py_ssize_t size)
    

def wrapped_get_program_full_path():
    cdef PyObject* pystr = PyUnicode_FromWideChar(Py_GetProgramFullPath(),-1)
    return <object>pystr


def inspect():
    # Exposes a c function to python
    print("sys.executable: ", sys.executable)
    print("Py_GetProgramFullPath", wrapped_get_program_full_path())



def check():
    a = sys.executable
    b = wrapped_get_program_full_path()

    if a != b:
        raise ValueError("sys.executable and Py_GetProgramFullPath were different")
