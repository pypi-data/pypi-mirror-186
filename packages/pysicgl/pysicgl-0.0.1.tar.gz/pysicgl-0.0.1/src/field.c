#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <structmember.h>
// python includes must come first

#include <errno.h>
#include <stdio.h>

#include "pysicgl/field.h"

// utilities for C consumers
int scalar_field_get_scalars(
    ScalarFieldObject* self, size_t* len, double** scalars) {
  int ret = 0;

  // provide the length of the scalars
  if (NULL != len) {
    *len = self->_scalars_buffer.len;
  }

  // provide the pointer to the scalars
  if (NULL != scalars) {
    *scalars = (double*)self->_scalars_buffer.buf;
  }

out:
  return ret;
}

// getset
static PyObject* get_pixels(PyObject* self_in, void* closure) {
  ScalarFieldObject* self = (ScalarFieldObject*)self_in;
  size_t pixels = 0;
  if (NULL == self->_scalars_buffer.obj) {
    goto out;
  }

  pixels = self->_scalars_buffer.len / sizeof(double);

out:
  return PyLong_FromLong(pixels);
}

static PyObject* get_memory(PyObject* self_in, void* closure) {
  ScalarFieldObject* self = (ScalarFieldObject*)self_in;
  return PyMemoryView_FromBuffer(&self->_scalars_buffer);
}

static int set_memory(PyObject* self_in, PyObject* value, void* closure) {
  ScalarFieldObject* self = (ScalarFieldObject*)self_in;
  if (!PyObject_IsInstance((PyObject*)value, (PyObject*)&PyByteArray_Type)) {
    PyErr_SetNone(PyExc_TypeError);
    return -1;
  }
  PyByteArrayObject* bytearray_obj = (PyByteArrayObject*)value;

  // clean up old buffer
  if (NULL != self->_scalars_buffer.obj) {
    PyBuffer_Release(&self->_scalars_buffer);
  }

  // reassign the buffer
  int ret = PyObject_GetBuffer(
      (PyObject*)bytearray_obj, &self->_scalars_buffer, PyBUF_WRITABLE);
  if (0 != ret) {
    return -1;
  }

  return 0;
}

// methods
static PyObject* allocate_scalar_memory(PyObject* self, PyObject* scalars_in) {
  size_t scalars;
  if (PyLong_Check(scalars_in)) {
    scalars = PyLong_AsSize_t(scalars_in);
  } else {
    PyErr_SetNone(PyExc_TypeError);
    return NULL;
  }

  return PyByteArray_FromObject(PyLong_FromSize_t(scalars * sizeof(double)));
}

static Py_ssize_t mp_length(PyObject* self_in) {
  ScalarFieldObject* self = (ScalarFieldObject*)self_in;

  size_t len;
  int ret = scalar_field_get_scalars(self, &len, NULL);
  if (0 != ret) {
    PyErr_SetNone(PyExc_OSError);
    return NULL;
  }

  return PyLong_FromLong(len);
}

static PyObject* mp_subscript(PyObject* self_in, PyObject* key) {
  ScalarFieldObject* self = (ScalarFieldObject*)self_in;
  size_t len;
  double* scalars;
  int ret = scalar_field_get_scalars(self, &len, &scalars);
  if (0 != ret) {
    PyErr_SetNone(PyExc_OSError);
    return NULL;
  }
  size_t idx = PyLong_AsSize_t(key);

  if (idx > (len - 1)) {
    PyErr_SetNone(PyExc_IndexError);
    return NULL;
  }

  return PyFloat_FromDouble(scalars[idx]);
}

static int mp_ass_subscript(PyObject* self_in, PyObject* key, PyObject* v) {
  ScalarFieldObject* self = (ScalarFieldObject*)self_in;
  size_t len;
  double* scalars;
  int ret = scalar_field_get_scalars(self, &len, &scalars);
  if (0 != ret) {
    PyErr_SetNone(PyExc_OSError);
    return -1;
  }
  size_t idx = PyLong_AsSize_t(key);

  if (idx > (len - 1)) {
    PyErr_SetNone(PyExc_IndexError);
    return -1;
  }

  // set the double here
  scalars[idx] = PyFloat_AsDouble(v);

  return 0;
}

static void tp_dealloc(PyObject* self_in) {
  ScalarFieldObject* self = (ScalarFieldObject*)self_in;
  PyBuffer_Release(&self->_scalars_buffer);
  Py_TYPE(self)->tp_free(self);
}

static int tp_init(PyObject* self_in, PyObject* args, PyObject* kwds) {
  ScalarFieldObject* self = (ScalarFieldObject*)self_in;
  char* keywords[] = {
      "memory",
      NULL,
  };
  PyByteArrayObject* memory_bytearray_obj;
  if (!PyArg_ParseTupleAndKeywords(
          args, kwds, "Y", keywords, &memory_bytearray_obj)) {
    return -1;
  }

  // set memory
  int ret = set_memory((PyObject*)self, (PyObject*)memory_bytearray_obj, NULL);
  if (0 != ret) {
    PyErr_SetNone(PyExc_OSError);
    return -1;
  }

  return 0;
}

static PyMethodDef tp_methods[] = {
    {"allocate_scalar_memory", (PyCFunction)allocate_scalar_memory,
     METH_O | METH_STATIC, "allocate memory for the given number of scalars"},
    {NULL},
};

static PyGetSetDef tp_getset[] = {
    {"pixels", get_pixels, NULL, "number of scalar values in memory", NULL},
    {"memory", get_memory, set_memory, "scalar memory", NULL},
    {NULL},
};

static PyMappingMethods tp_as_mapping = {
    .mp_length = mp_length,
    .mp_subscript = mp_subscript,
    .mp_ass_subscript = mp_ass_subscript,
};

PyTypeObject ScalarFieldType = {
    PyVarObject_HEAD_INIT(NULL, 0).tp_name = "pysicgl.ScalarField",
    .tp_doc = PyDoc_STR("sicgl ScalarField"),
    .tp_basicsize = sizeof(ScalarFieldObject),
    .tp_itemsize = 0,
    .tp_flags = Py_TPFLAGS_DEFAULT,
    .tp_new = PyType_GenericNew,
    .tp_dealloc = tp_dealloc,
    .tp_init = tp_init,
    .tp_methods = tp_methods,
    .tp_getset = tp_getset,
    .tp_as_mapping = &tp_as_mapping,
};
