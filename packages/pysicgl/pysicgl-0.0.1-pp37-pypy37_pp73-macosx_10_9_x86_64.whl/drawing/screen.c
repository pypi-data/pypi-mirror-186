#include "pysicgl/drawing/screen.h"

#include "pysicgl/interface.h"
#include "pysicgl/screen.h"
#include "pysicgl/utilities.h"
#include "sicgl/domain/screen.h"

PyObject* screen_fill(PyObject* self_in, PyObject* args) {
  InterfaceObject* self = (InterfaceObject*)self_in;
  ScreenObject* screen_obj;
  int color;
  if (!PyArg_ParseTuple(args, "O!i", &ScreenType, &screen_obj, &color)) {
    return NULL;
  }

  int ret = sicgl_screen_fill(&self->interface, screen_obj->screen, color);
  if (0 != ret) {
    PyErr_SetNone(PyExc_OSError);
    return NULL;
  }
  return Py_None;
}

PyObject* screen_pixel(PyObject* self_in, PyObject* args) {
  InterfaceObject* self = (InterfaceObject*)self_in;
  ScreenObject* screen_obj;
  int color;
  ext_t u, v;
  if (!PyArg_ParseTuple(
          args, "O!i(ii)", &ScreenType, &screen_obj, &color, &u, &v)) {
    return NULL;
  }

  int ret =
      sicgl_screen_pixel(&self->interface, screen_obj->screen, color, u, v);
  if (0 != ret) {
    PyErr_SetNone(PyExc_OSError);
    return NULL;
  }
  return Py_None;
}

PyObject* screen_line(PyObject* self_in, PyObject* args) {
  InterfaceObject* self = (InterfaceObject*)self_in;
  ScreenObject* screen_obj;
  int color;
  ext_t u0, v0, u1, v1;
  if (!PyArg_ParseTuple(
          args, "O!i(ii)(ii)", &ScreenType, &screen_obj, &color, &u0, &v0, &u1,
          &v1)) {
    return NULL;
  }

  int ret = sicgl_screen_line(
      &self->interface, screen_obj->screen, color, u0, v0, u1, v1);
  if (0 != ret) {
    PyErr_SetNone(PyExc_OSError);
    return NULL;
  }
  return Py_None;
}

PyObject* screen_rectangle(PyObject* self_in, PyObject* args) {
  InterfaceObject* self = (InterfaceObject*)self_in;
  ScreenObject* screen_obj;
  int color;
  ext_t u0, v0, u1, v1;
  if (!PyArg_ParseTuple(
          args, "O!i(ii)(ii)", &ScreenType, &screen_obj, &color, &u0, &v0, &u1,
          &v1)) {
    return NULL;
  }

  int ret = sicgl_screen_rectangle(
      &self->interface, screen_obj->screen, color, u0, v0, u1, v1);
  if (0 != ret) {
    PyErr_SetNone(PyExc_OSError);
    return NULL;
  }
  return Py_None;
}

PyObject* screen_rectangle_filled(PyObject* self_in, PyObject* args) {
  InterfaceObject* self = (InterfaceObject*)self_in;
  ScreenObject* screen_obj;
  int color;
  ext_t u0, v0, u1, v1;
  if (!PyArg_ParseTuple(
          args, "O!i(ii)(ii)", &ScreenType, &screen_obj, &color, &u0, &v0, &u1,
          &v1)) {
    return NULL;
  }

  int ret = sicgl_screen_rectangle_filled(
      &self->interface, screen_obj->screen, color, u0, v0, u1, v1);
  if (0 != ret) {
    PyErr_SetNone(PyExc_OSError);
    return NULL;
  }
  return Py_None;
}

PyObject* screen_circle(PyObject* self_in, PyObject* args) {
  InterfaceObject* self = (InterfaceObject*)self_in;
  ScreenObject* screen_obj;
  int color;
  ext_t u0, v0, diameter;
  if (!PyArg_ParseTuple(
          args, "O!i(ii)i", &ScreenType, &screen_obj, &color, &u0, &v0,
          &diameter)) {
    return NULL;
  }

  int ret = sicgl_screen_circle_ellipse(
      &self->interface, screen_obj->screen, color, u0, v0, diameter);
  if (0 != ret) {
    PyErr_SetNone(PyExc_OSError);
    return NULL;
  }
  return Py_None;
}

PyObject* screen_ellipse(PyObject* self_in, PyObject* args) {
  InterfaceObject* self = (InterfaceObject*)self_in;
  ScreenObject* screen_obj;
  int color;
  ext_t u0, v0, semiu, semiv;
  if (!PyArg_ParseTuple(
          args, "O!i(ii)(ii)", &ScreenType, &screen_obj, &color, &u0, &v0,
          &semiu, &semiv)) {
    return NULL;
  }
  int ret = sicgl_screen_ellipse(
      &self->interface, screen_obj->screen, color, u0, v0, semiu, semiv);
  if (0 != ret) {
    PyErr_SetNone(PyExc_OSError);
    return NULL;
  }
  return Py_None;
}
