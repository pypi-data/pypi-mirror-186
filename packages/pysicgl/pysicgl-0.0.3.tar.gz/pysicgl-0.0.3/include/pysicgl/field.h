#pragma once

#define PY_SSIZE_T_CLEAN
#include <Python.h>
// python includes must come first

#include "sicgl/field.h"

// declare the type
extern PyTypeObject ScalarFieldType;

typedef struct {
  PyObject_HEAD Py_buffer _scalars_buffer;
} ScalarFieldObject;

int scalar_field_get_scalars(
    ScalarFieldObject* self, size_t* len, double** scalars);
