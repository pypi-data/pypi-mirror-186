#define PY_SSIZE_T_CLEAN
#include <Python.h>
// python includes must come first

#include "pysicgl/drawing/blit.h"
#include "pysicgl/interface.h"
#include "pysicgl/screen.h"
#include "sicgl/blit.h"

PyObject* blit(PyObject* self_in, PyObject* args) {
  InterfaceObject* self = (InterfaceObject*)self_in;
  ScreenObject* screen;
  Py_buffer sprite;
  if (!PyArg_ParseTuple(args, "O!y*", &ScreenType, &screen, &sprite)) {
    return NULL;
  }

  int ret = sicgl_blit(&self->interface, screen->screen, sprite.buf);

  PyBuffer_Release(&sprite);

  if (0 != ret) {
    PyErr_SetNone(PyExc_OSError);
    return NULL;
  }

  return Py_None;
}
