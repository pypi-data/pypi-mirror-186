#pragma once

#define PY_SSIZE_T_CLEAN
#include <Python.h>
// python includes must come first

#include "sicgl/color_sequence.h"

// declare the type
extern PyTypeObject ColorSequenceType;

typedef struct {
  PyObject_HEAD PyObject* _colors;
  int _type;
  sequence_map_fn _interpolation_map_fn;
} ColorSequenceObject;

int ColorSequence_post_ready_init();

int ColorSequence_get(
    ColorSequenceObject* self, size_t* len, color_t* colors_out,
    size_t colors_out_len);
int ColorSequence_get_interp_map_fn(
    size_t interp_type, sequence_map_fn* fn_out);
