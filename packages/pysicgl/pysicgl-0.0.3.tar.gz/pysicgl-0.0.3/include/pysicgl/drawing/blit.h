#pragma once

#define PY_SSIZE_T_CLEAN
#include <Python.h>
// python includes must come first

PyObject* blit(PyObject* self, PyObject* args);
