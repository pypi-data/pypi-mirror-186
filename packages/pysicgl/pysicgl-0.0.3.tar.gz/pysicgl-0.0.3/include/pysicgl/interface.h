#pragma once

#define PY_SSIZE_T_CLEAN
#include <Python.h>
// python includes must come first

#include "pysicgl/screen.h"
#include "sicgl/interface.h"
#include "sicgl/screen.h"

// declare the type
extern PyTypeObject InterfaceType;

typedef struct {
  PyObject_HEAD
      // the underlying sicgl type
      interface_t interface;

  // a ScreenObject which is linked to
  // the interface screen by reference
  ScreenObject* _screen;

  // a buffer backs up the interface memory
  Py_buffer _memory_buffer;
} InterfaceObject;
