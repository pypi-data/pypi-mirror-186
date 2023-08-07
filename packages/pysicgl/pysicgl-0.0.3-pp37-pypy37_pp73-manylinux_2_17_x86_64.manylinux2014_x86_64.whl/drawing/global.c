#include "pysicgl/drawing/global.h"

#include <stdio.h>

#include "pysicgl/interface.h"
#include "sicgl/domain/global.h"

PyObject* global_pixel(PyObject* self_in, PyObject* args) {
  InterfaceObject* self = (InterfaceObject*)self_in;
  int color;
  ext_t u, v;
  if (!PyArg_ParseTuple(args, "i(ii)", &color, &u, &v)) {
    return NULL;
  }

  int ret = sicgl_global_pixel(&self->interface, color, u, v);
  if (0 != ret) {
    PyErr_SetNone(PyExc_OSError);
    return NULL;
  }
  return Py_None;
}

PyObject* global_line(PyObject* self_in, PyObject* args) {
  InterfaceObject* self = (InterfaceObject*)self_in;
  int color;
  ext_t u0, v0, u1, v1;
  if (!PyArg_ParseTuple(args, "O!i(ii)(ii)", &color, &u0, &v0, &u1, &v1)) {
    return NULL;
  }

  int ret = sicgl_global_line(&self->interface, color, u0, v0, u1, v1);
  if (0 != ret) {
    PyErr_SetNone(PyExc_OSError);
    return NULL;
  }
  return Py_None;
}

PyObject* global_rectangle(PyObject* self_in, PyObject* args) {
  InterfaceObject* self = (InterfaceObject*)self_in;
  int color;
  ext_t u0, v0, u1, v1;
  if (!PyArg_ParseTuple(args, "O!i(ii)(ii)", &color, &u0, &v0, &u1, &v1)) {
    return NULL;
  }

  int ret = sicgl_global_rectangle(&self->interface, color, u0, v0, u1, v1);
  if (0 != ret) {
    PyErr_SetNone(PyExc_OSError);
    return NULL;
  }
  return Py_None;
}

PyObject* global_rectangle_filled(PyObject* self_in, PyObject* args) {
  InterfaceObject* self = (InterfaceObject*)self_in;
  int color;
  ext_t u0, v0, u1, v1;
  if (!PyArg_ParseTuple(args, "O!i(ii)(ii)", &color, &u0, &v0, &u1, &v1)) {
    return NULL;
  }

  int ret =
      sicgl_global_rectangle_filled(&self->interface, color, u0, v0, u1, v1);
  if (0 != ret) {
    PyErr_SetNone(PyExc_OSError);
    return NULL;
  }
  return Py_None;
}

PyObject* global_circle(PyObject* self_in, PyObject* args) {
  InterfaceObject* self = (InterfaceObject*)self_in;
  int color;
  ext_t u0, v0, diameter;
  if (!PyArg_ParseTuple(args, "O!i(ii)(ii)", &color, &u0, &v0, &diameter)) {
    return NULL;
  }

  int ret =
      sicgl_global_circle_ellipse(&self->interface, color, u0, v0, diameter);
  if (0 != ret) {
    PyErr_SetNone(PyExc_OSError);
    return NULL;
  }
  return Py_None;
}

PyObject* global_ellipse(PyObject* self_in, PyObject* args) {
  InterfaceObject* self = (InterfaceObject*)self_in;
  int color;
  ext_t u0, v0, semiu, semiv;
  if (!PyArg_ParseTuple(
          args, "O!i(ii)(ii)", &color, &u0, &v0, &semiu, &semiv)) {
    return NULL;
  }

  int ret = sicgl_global_ellipse(&self->interface, color, u0, v0, semiu, semiv);
  if (0 != ret) {
    PyErr_SetNone(PyExc_OSError);
    return NULL;
  }
  return Py_None;
}
