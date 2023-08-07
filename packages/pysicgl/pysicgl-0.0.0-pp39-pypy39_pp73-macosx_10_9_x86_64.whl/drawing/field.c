#define PY_SSIZE_T_CLEAN
#include <Python.h>
// python includes must come first

#include "pysicgl/color_sequence.h"
#include "pysicgl/drawing/blit.h"
#include "pysicgl/field.h"
#include "pysicgl/interface.h"
#include "pysicgl/screen.h"
#include "sicgl/blit.h"

PyObject* scalar_field(PyObject* self_in, PyObject* args, PyObject* kwds) {
  int ret = 0;
  InterfaceObject* self = (InterfaceObject*)self_in;
  ScreenObject* field_obj;
  ScalarFieldObject* scalar_field_obj;
  ColorSequenceObject* color_sequence_obj;
  unsigned int interp_type = 0;
  double offset = 0.0;
  char* keywords[] = {
      "field", "scalars", "color_sequence", "interp_type", "offset", NULL,
  };
  if (!PyArg_ParseTupleAndKeywords(
          args, kwds, "O!O!O!|Id", keywords, &ScreenType, &field_obj,
          &ScalarFieldType, &scalar_field_obj, &ColorSequenceType,
          &color_sequence_obj, &interp_type, &offset)) {
    return NULL;
  }

  // determine color sequence length
  size_t len;
  ret = ColorSequence_get(color_sequence_obj, &len, NULL, 0);
  if (0 != ret) {
    PyErr_SetNone(PyExc_OSError);
    return NULL;
  }

  // allocate space on the stack for the colors
  color_t colors[len];
  ret = ColorSequence_get(color_sequence_obj, NULL, colors, len);
  if (0 != ret) {
    PyErr_SetNone(PyExc_OSError);
    return NULL;
  }

  // create the color_sequence_t for sicgl
  color_sequence_t sequence = {
      .colors = colors,
      .length = len,
  };

  // get the scalars
  double* scalars;
  size_t scalars_length;
  ret = scalar_field_get_scalars(scalar_field_obj, &scalars_length, &scalars);
  if (0 != ret) {
    PyErr_SetNone(PyExc_OSError);
    return NULL;
  }

  sequence_map_fn interp_map_fn;
  ret = ColorSequence_get_interp_map_fn(interp_type, &interp_map_fn);
  if (0 != ret) {
    PyErr_SetNone(PyExc_OSError);
    return NULL;
  }

  // apply the field
  ret = sicgl_scalar_field(
      &self->interface, field_obj->screen, scalars, offset, &sequence,
      interp_map_fn);
  if (0 != ret) {
    PyErr_SetNone(PyExc_OSError);
    return NULL;
  }

  return Py_None;
}
