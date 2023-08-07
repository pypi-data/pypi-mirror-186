#pragma once

#define PY_SSIZE_T_CLEAN
#include <Python.h>
// python includes must come first

PyObject* interface_fill(PyObject* self_in, PyObject* args);
PyObject* interface_pixel(PyObject* self_in, PyObject* args);
PyObject* interface_line(PyObject* self_in, PyObject* args);
PyObject* interface_rectangle(PyObject* self_in, PyObject* args);
PyObject* interface_rectangle_filled(PyObject* self_in, PyObject* args);
PyObject* interface_circle(PyObject* self_in, PyObject* args);
PyObject* interface_ellipse(PyObject* self_in, PyObject* args);
