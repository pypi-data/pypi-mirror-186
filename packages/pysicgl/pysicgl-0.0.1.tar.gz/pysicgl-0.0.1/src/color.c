#define PY_SSIZE_T_CLEAN
#include <Python.h>
// python includes must come first

#include <errno.h>
#include <stdio.h>

#include "pysicgl/color.h"
#include "sicgl/color.h"

// methods
static PyObject* get_rgba(PyObject* self, PyObject* input) {
  color_t color = PyLong_AsLong(input);
  return PyTuple_Pack(
      4, PyLong_FromLong(color_channel_red(color)),
      PyLong_FromLong(color_channel_green(color)),
      PyLong_FromLong(color_channel_blue(color)),
      PyLong_FromLong(color_channel_alpha(color)));
}

static PyObject* from_rgba(PyObject* self, PyObject* input) {
  return PyLong_FromLong(color_from_channels(
      PyLong_AsLong(PyTuple_GetItem(input, 0)),
      PyLong_AsLong(PyTuple_GetItem(input, 1)),
      PyLong_AsLong(PyTuple_GetItem(input, 2)),
      PyLong_AsLong(PyTuple_GetItem(input, 3))));
}

static PyMethodDef tp_methods[] = {
    {"get_rgba", (PyCFunction)get_rgba, METH_O | METH_STATIC,
     "return the individual RGBA components of the input color as a 4-tuple"},
    {"from_rgba", (PyCFunction)from_rgba, METH_O | METH_STATIC,
     "return the color comprised of the RGBA input 4-tuple"},
    {NULL},
};

PyTypeObject ColorType = {
    PyVarObject_HEAD_INIT(NULL, 0).tp_name = "pysicgl.Color",
    .tp_doc = PyDoc_STR("sicgl color"),
    .tp_basicsize = sizeof(ColorObject),
    .tp_itemsize = 0,
    .tp_flags = Py_TPFLAGS_DEFAULT,
    .tp_new = PyType_GenericNew,
    .tp_methods = tp_methods,
};
