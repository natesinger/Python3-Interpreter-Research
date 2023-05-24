/* Include the approperiate API for reference, must install libraries if not available 
 command like (debian): sudo apt-get install python3.X-dev */

#include <Python.h>

// The function we want to expose to Python
static PyObject* hello_world(PyObject* self, PyObject* args)
{
    printf("Hello, World!\n");
    Py_RETURN_NONE;
}

// Define a method table actually exposing the function itself
static PyMethodDef HelloWorldMethods[] = {
    {"hello_world",  hello_world, METH_VARARGS, "Print 'Hello, World!'"},
    {NULL, NULL, 0, NULL}
};

// Create and define the module
static struct PyModuleDef helloworldmodule = {
    PyModuleDef_HEAD_INIT,
    "helloworld",
    NULL,
    -1,
    HelloWorldMethods
};

// Export the function so Python can call it
PyMODINIT_FUNC
PyInit_hello_world(void)
{
    return PyModule_Create(&helloworldmodule);
}
