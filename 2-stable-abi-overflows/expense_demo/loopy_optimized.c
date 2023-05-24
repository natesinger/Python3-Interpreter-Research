/* Include the approperiate API for reference, must install libraries if not available 
 command like (debian): sudo apt-get install python3.X-dev */

#include <Python.h>

// The function we want to expose to Python
static PyObject* loopy_optimized(PyObject* self, PyObject* args)
{
    int i;
    for (i = 0; i < 1000000000; i++) { int x = i / 5; }

    Py_RETURN_NONE;
    return 0;
}

// Define a method table actually exposing the function itself
static PyMethodDef LoopyOptimizedMethods[] = {
    {"loopy_optimized",  loopy_optimized, METH_VARARGS, "Demonstrates C speed in loops'"},
    {NULL, NULL, 0, NULL}
};

// Create and define the module
static struct PyModuleDef loopyoptimizedmodule = {
    PyModuleDef_HEAD_INIT,
    "loopyoptimized",
    NULL,
    -1,
    LoopyOptimizedMethods
};

// Export the function so Python can call it
PyMODINIT_FUNC
PyInit_loopy_optimized(void)
{
    return PyModule_Create(&loopyoptimizedmodule);
}
