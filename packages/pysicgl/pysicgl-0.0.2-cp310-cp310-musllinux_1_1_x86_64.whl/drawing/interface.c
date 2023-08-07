#include "pysicgl/interface.h"

#include "pysicgl/utilities.h"
#include "sicgl/domain/interface.h"

PyObject* interface_fill(PyObject* self_in, PyObject* args) {
  InterfaceObject* self = (InterfaceObject*)self_in;
  int color;
  if (!PyArg_ParseTuple(args, "i", &color)) {
    return NULL;
  }

  int ret = sicgl_interface_fill(&self->interface, color);
  if (0 != ret) {
    PyErr_SetNone(PyExc_OSError);
    return NULL;
  }
  return Py_None;
}

PyObject* interface_pixel(PyObject* self_in, PyObject* args) {
  InterfaceObject* self = (InterfaceObject*)self_in;
  int color;
  ext_t u, v;
  if (!PyArg_ParseTuple(args, "i(ii)", &color, &u, &v)) {
    return NULL;
  }

  int ret = sicgl_interface_pixel(&self->interface, color, u, v);
  if (0 != ret) {
    PyErr_SetNone(PyExc_OSError);
    return NULL;
  }
  return Py_None;
}

PyObject* interface_line(PyObject* self_in, PyObject* args) {
  InterfaceObject* self = (InterfaceObject*)self_in;
  int color;
  ext_t u0, v0, u1, v1;
  if (!PyArg_ParseTuple(args, "i(ii)(ii)", &color, &u0, &v0, &u1, &v1)) {
    return NULL;
  }

  int ret = sicgl_interface_line(&self->interface, color, u0, v0, u1, v1);
  if (0 != ret) {
    PyErr_SetNone(PyExc_OSError);
    return NULL;
  }
  return Py_None;
}

PyObject* interface_rectangle(PyObject* self_in, PyObject* args) {
  InterfaceObject* self = (InterfaceObject*)self_in;
  int color;
  ext_t u0, v0, u1, v1;
  if (!PyArg_ParseTuple(args, "i(ii)(ii)", &color, &u0, &v0, &u1, &v1)) {
    return NULL;
  }

  int ret = sicgl_interface_rectangle(&self->interface, color, u0, v0, u1, v1);
  if (0 != ret) {
    PyErr_SetNone(PyExc_OSError);
    return NULL;
  }
  return Py_None;
}

PyObject* interface_rectangle_filled(PyObject* self_in, PyObject* args) {
  InterfaceObject* self = (InterfaceObject*)self_in;
  int color;
  ext_t u0, v0, u1, v1;
  if (!PyArg_ParseTuple(args, "i(ii)(ii)", &color, &u0, &v0, &u1, &v1)) {
    return NULL;
  }

  int ret =
      sicgl_interface_rectangle_filled(&self->interface, color, u0, v0, u1, v1);
  if (0 != ret) {
    PyErr_SetNone(PyExc_OSError);
    return NULL;
  }
  return Py_None;
}

PyObject* interface_circle(PyObject* self_in, PyObject* args) {
  InterfaceObject* self = (InterfaceObject*)self_in;
  int color;
  ext_t u0, v0, diameter;
  if (!PyArg_ParseTuple(args, "i(ii)i", &color, &u0, &v0, &diameter)) {
    return NULL;
  }

  int ret =
      sicgl_interface_circle_ellipse(&self->interface, color, u0, v0, diameter);
  if (0 != ret) {
    PyErr_SetNone(PyExc_OSError);
    return NULL;
  }
  return Py_None;
}

PyObject* interface_ellipse(PyObject* self_in, PyObject* args) {
  InterfaceObject* self = (InterfaceObject*)self_in;
  int color;
  ext_t u0, v0, semiu, semiv;
  if (!PyArg_ParseTuple(args, "i(ii)(ii)", &color, &u0, &v0, &semiu, &semiv)) {
    return NULL;
  }

  int ret =
      sicgl_interface_ellipse(&self->interface, color, u0, v0, semiu, semiv);
  if (0 != ret) {
    PyErr_SetNone(PyExc_OSError);
    return NULL;
  }
  return Py_None;
}
