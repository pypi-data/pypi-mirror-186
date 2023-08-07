#pragma once

#define PY_SSIZE_T_CLEAN
#include <Python.h>
// python includes must come first

PyObject* screen_fill(PyObject* self_in, PyObject* args);
PyObject* screen_pixel(PyObject* self_in, PyObject* args);
PyObject* screen_line(PyObject* self_in, PyObject* args);
PyObject* screen_rectangle(PyObject* self_in, PyObject* args);
PyObject* screen_rectangle_filled(PyObject* self_in, PyObject* args);
PyObject* screen_circle(PyObject* self_in, PyObject* args);
PyObject* screen_ellipse(PyObject* self_in, PyObject* args);
