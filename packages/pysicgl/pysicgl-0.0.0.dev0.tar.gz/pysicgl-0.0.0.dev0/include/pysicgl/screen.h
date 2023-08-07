#pragma once

#define PY_SSIZE_T_CLEAN
#include <Python.h>
// python includes must come first

#include <stdbool.h>

#include "sicgl/screen.h"

// declare the type
extern PyTypeObject ScreenType;

typedef struct {
  PyObject_HEAD
      /* Type-specific fields go here. */
      screen_t* screen;
  screen_t _screen;

  // a flag to explicitly indicate whether this is an object or reference
  bool _is_reference;
} ScreenObject;

// publicly accessible constructors
ScreenObject* new_screen_object(screen_t* ref);
