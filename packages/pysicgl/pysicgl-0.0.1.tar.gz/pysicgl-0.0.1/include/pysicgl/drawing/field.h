#pragma once

#define PY_SSIZE_T_CLEAN
#include <Python.h>
// python includes must come first

PyObject* scalar_field(PyObject* self_in, PyObject* args);
