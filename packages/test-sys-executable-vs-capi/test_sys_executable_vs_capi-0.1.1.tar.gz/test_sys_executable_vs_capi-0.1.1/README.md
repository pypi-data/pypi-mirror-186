test_sys_executable_vs_Py_GetProgramFullPath
=======================

Wrapped python interpreters sometimes
only adjust sys.executable but neglect to adjust the c API's concept of
'what's my interpreter filename'

This module can expose that.


```
import test_sys_executable_vs_py_getprogramfullpath

# print both.
test_sys_executable_vs_py_getprogramfullpath.inspect()

# raise if unequal
test_sys_executable_vs_py_getprogramfullpath.check()
```
