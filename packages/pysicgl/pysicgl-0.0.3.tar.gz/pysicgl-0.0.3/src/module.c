#define PY_SSIZE_T_CLEAN
#include <Python.h>
// python includes must come first

#include "pysicgl/color.h"
#include "pysicgl/color_sequence.h"
#include "pysicgl/field.h"
#include "pysicgl/interface.h"
#include "pysicgl/screen.h"
#include "sicgl.h"

static PyObject* allocate_pixel_memory(PyObject* self, PyObject* pixels_in) {
  size_t pixels;
  if (PyLong_Check(pixels_in)) {
    pixels = PyLong_AsSize_t(pixels_in);
  } else {
    PyErr_SetNone(PyExc_TypeError);
    return NULL;
  }

  size_t bpp = bytes_per_pixel();
  return PyByteArray_FromObject(PyLong_FromSize_t(pixels * bpp));
}

static PyObject* gamma_correct(PyObject* self, PyObject* args) {
  PyObject* input_obj;
  PyObject* output_obj;
  if (!PyArg_ParseTuple(
          args, "O!O!", &InterfaceType, &input_obj, &InterfaceType,
          &output_obj)) {
    return NULL;
  }

  InterfaceObject* input = (InterfaceObject*)input_obj;
  InterfaceObject* output = (InterfaceObject*)output_obj;

  int ret = sicgl_gamma_correct(&input->interface, &output->interface);
  if (0 != ret) {
    PyErr_SetNone(PyExc_OSError);
    return NULL;
  }

  return Py_None;
}

PyMethodDef pysicgl_funcs[] = {
    {"allocate_pixel_memory", (PyCFunction)allocate_pixel_memory, METH_O,
     "Allocate memory for the specified number of pixels"},
    {"gamma_correct", (PyCFunction)gamma_correct, METH_VARARGS,
     "perform gamma correction on interface memory"},
    {NULL},
};

static PyModuleDef module = {
    PyModuleDef_HEAD_INIT,
    "pysicgl",
    "sicgl in Python",
    -1,
    pysicgl_funcs,
    NULL,
    NULL,
    NULL,
    NULL,
};

// collect type definitions for the module
typedef struct _type_entry_t {
  const char* name;
  PyTypeObject* type;
} type_entry_t;
type_entry_t pysicgl_types[] = {
    {"Interface", &InterfaceType},         {"Color", &ColorType},
    {"ColorSequence", &ColorSequenceType}, {"Screen", &ScreenType},
    {"ScalarField", &ScalarFieldType},
};
size_t num_types = sizeof(pysicgl_types) / sizeof(type_entry_t);

PyMODINIT_FUNC PyInit_pysicgl(void) {
  // ensure that types are ready
  for (size_t idx = 0; idx < num_types; idx++) {
    type_entry_t entry = pysicgl_types[idx];
    if (PyType_Ready(entry.type) < 0) {
      return NULL;
    }
  }

  // run additional initialization for types
  int ret = ColorSequence_post_ready_init();
  if (0 != ret) {
    PyErr_SetString(PyExc_OSError, "failed ColorSequence post-ready init");
    return NULL;
  }

  // create the module
  PyObject* m = PyModule_Create(&module);

  // register types into the module
  for (size_t idx = 0; idx < num_types; idx++) {
    type_entry_t entry = pysicgl_types[idx];
    Py_INCREF(entry.type);
    if (PyModule_AddObject(m, entry.name, (PyObject*)entry.type) < 0) {
      Py_DECREF(entry.type);
      Py_DECREF(m);
      return NULL;
    }
  }

  // return the module
  return m;
}
