#pragma once

#define PY_SSIZE_T_CLEAN
#include <Python.h>
// python includes must come first

#include "sicgl/color.h"

// declare the type
extern PyTypeObject ColorType;

typedef struct {
  PyObject_HEAD
} ColorObject;
