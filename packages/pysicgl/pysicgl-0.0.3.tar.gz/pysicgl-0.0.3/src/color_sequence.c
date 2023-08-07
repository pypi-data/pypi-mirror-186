#define PY_SSIZE_T_CLEAN
#include <Python.h>
// python includes must come first

#include <errno.h>

#include "pysicgl/color_sequence.h"

// fwd declarations
static Py_ssize_t mp_length(PyObject* self_in);

// data
/**
 * @brief interpolation type names.
 * These names each correspond to a particular interpolation style that can
 * be used by the color sequence.
 */
typedef struct _interp_type_entry {
  char* name;
  sequence_map_fn map;
} interp_type_enty_t;
static const interp_type_enty_t interp_types[] = {
    {.name = "CONTINUOUS_CIRCULAR",
     .map = color_sequence_interpolate_color_continuous_circular},
    {.name = "CONTINUOUS_LINEAR",
     .map = color_sequence_interpolate_color_continuous_linear},
    {.name = "DISCRETE_CIRCULAR",
     .map = color_sequence_interpolate_color_discrete_circular},
    {.name = "DISCRETE_LINEAR",
     .map = color_sequence_interpolate_color_discrete_linear},
};
static const size_t num_interp_types =
    sizeof(interp_types) / sizeof(interp_type_enty_t);

// utilities for C consumers
int ColorSequence_get(
    ColorSequenceObject* self, size_t* len, color_t* colors_out,
    size_t colors_out_len) {
  int ret = 0;
  if (NULL == self) {
    ret = -1;
    goto out;
  }

  // provide the length of the sequence
  size_t length = mp_length((PyObject*)self);
  if (NULL != len) {
    *len = length;
  }

  // fill the color output buffer
  if (NULL != colors_out) {
    size_t elements_out = colors_out_len;
    if (elements_out > length) {
      elements_out = length;
    }
    for (size_t idx = 0; idx < elements_out; idx++) {
      colors_out[idx] = PyLong_AsLong(PyList_GetItem(self->_colors, idx));
    }
  }

out:
  return ret;
}

int ColorSequence_get_interp_map_fn(
    size_t interp_type, sequence_map_fn* fn_out) {
  int ret = 0;
  // determine the interpolation function
  if (interp_type > num_interp_types) {
    ret = -EINVAL;
    goto out;
  }
  if (NULL == fn_out) {
    ret = -ENOMEM;
    goto out;
  }

  // provide the corresponding map function
  *fn_out = interp_types[interp_type].map;

out:
  return ret;
}

// getset
static PyObject* get_colors(PyObject* self_in, void* closure) {
  ColorSequenceObject* self = (ColorSequenceObject*)self_in;
  Py_INCREF(self->_colors);
  return self->_colors;
}

static int set_colors(PyObject* self_in, PyObject* value, void* closure) {
  ColorSequenceObject* self = (ColorSequenceObject*)self_in;
  if (!PyObject_IsInstance((PyObject*)value, (PyObject*)&PyList_Type)) {
    PyErr_SetNone(PyExc_TypeError);
    return -1;
  }

  if (NULL != self->_colors) {
    Py_DECREF(self->_colors);
  }

  self->_colors = value;
  Py_INCREF(self->_colors);

  return 0;
}

// methods
static PyObject* interpolate(
    PyObject* self_in, PyObject* args, PyObject* kwds) {
  int ret = 0;
  ColorSequenceObject* self = (ColorSequenceObject*)self_in;
  PyObject* samples_obj;
  unsigned int interp_type = 0;
  char* keywords[] = {
      "samples",
      "interp_type",
      NULL,
  };
  if (!PyArg_ParseTupleAndKeywords(
          args, kwds, "O|I", keywords, &samples_obj, &interp_type)) {
    return NULL;
  }

  if (interp_type > num_interp_types) {
    PyErr_SetNone(PyExc_ValueError);
    return NULL;
  }

  // determine color sequence length
  size_t len;
  ret = ColorSequence_get(self, &len, NULL, 0);
  if (0 != ret) {
    PyErr_SetNone(PyExc_OSError);
    return NULL;
  }

  // allocate space on the stack for the colors
  color_t colors[len];
  ret = ColorSequence_get(self, NULL, colors, len);
  if (0 != ret) {
    PyErr_SetNone(PyExc_OSError);
    return NULL;
  }

  // create the color_sequence_t for sicgl
  color_sequence_t sequence = {
      .colors = colors,
      .length = len,
  };

  // determine the interpolation function
  sequence_map_fn interp_fn;
  ret = ColorSequence_get_interp_map_fn(interp_type, &interp_fn);
  if (0 != ret) {
    PyErr_SetNone(PyExc_OSError);
    return NULL;
  }

  // use this sequences' interpolation method to handle the input
  PyObject* result = NULL;
  if (PyLong_Check(samples_obj)) {
    // input is a single sample, return the interpolated color directly
    color_t color;
    ret = interp_fn(&sequence, (double)PyLong_AsLong(samples_obj), &color);
    if (0 != ret) {
      PyErr_SetNone(PyExc_OSError);
      return NULL;
    }
    result = PyLong_FromLong(color);

  } else if (PyFloat_Check(samples_obj)) {
    // input is a single sample, return the interpolated color directly
    color_t color;
    ret = interp_fn(&sequence, PyFloat_AsDouble(samples_obj), &color);
    if (0 != ret) {
      PyErr_SetNone(PyExc_OSError);
      return NULL;
    }
    result = PyLong_FromLong(color);
  } else if (PyList_Check(samples_obj)) {
    // input is a list of samples, return a tuple of interpolated colors
    size_t num_samples = PyList_Size(samples_obj);
    result = PyTuple_New(num_samples);
    for (size_t idx = 0; idx < num_samples; idx++) {
      color_t color;
      ret = interp_fn(
          &sequence, PyFloat_AsDouble(PyList_GetItem(samples_obj, idx)),
          &color);
      if (0 != ret) {
        PyErr_SetNone(PyExc_OSError);
        return NULL;
      }
      ret = PyTuple_SetItem(result, idx, PyLong_FromLong(color));
      if (0 != ret) {
        return NULL;
      }
    }
  } else if (PyTuple_Check(samples_obj)) {
    // input is a tuple of samples, return a tuple of interpolated colors
    size_t num_samples = PyTuple_Size(samples_obj);
    result = PyTuple_New(num_samples);
    for (size_t idx = 0; idx < num_samples; idx++) {
      color_t color;
      ret = interp_fn(
          &sequence, PyFloat_AsDouble(PyTuple_GetItem(samples_obj, idx)),
          &color);
      if (0 != ret) {
        PyErr_SetNone(PyExc_OSError);
        return NULL;
      }
      ret = PyTuple_SetItem(result, idx, PyLong_FromLong(color));
      if (0 != ret) {
        return NULL;
      }
    }
  } else {
    PyErr_SetNone(PyExc_TypeError);
    return NULL;
  }

  return result;
}

static Py_ssize_t mp_length(PyObject* self_in) {
  ColorSequenceObject* self = (ColorSequenceObject*)self_in;
  return PyList_Size(self->_colors);
}

static PyObject* mp_subscript(PyObject* self_in, PyObject* key) {
  ColorSequenceObject* self = (ColorSequenceObject*)self_in;
  return PyList_GetItem(self->_colors, PyLong_AsLong(key));
}

static int mp_ass_subscript(PyObject* self_in, PyObject* key, PyObject* v) {
  ColorSequenceObject* self = (ColorSequenceObject*)self_in;
  if (!PyLong_Check(v)) {
    PyErr_SetNone(PyExc_TypeError);
    return -1;
  }
  return PyList_SetItem(self->_colors, PyLong_AsLong(key), v);
}

static void tp_dealloc(PyObject* self_in) {
  ColorSequenceObject* self = (ColorSequenceObject*)self_in;
  Py_XDECREF(self->_colors);
  Py_TYPE(self)->tp_free(self);
}

static int tp_init(PyObject* self_in, PyObject* args, PyObject* kwds) {
  ColorSequenceObject* self = (ColorSequenceObject*)self_in;
  char* keywords[] = {
      "colors",
      NULL,
  };
  PyObject* colors_obj = PyList_New(0);
  if (!PyArg_ParseTupleAndKeywords(args, kwds, "|O", keywords, &colors_obj)) {
    return -1;
  }

  int ret = set_colors((PyObject*)self, colors_obj, NULL);
  if (0 != ret) {
    PyErr_SetNone(PyExc_OSError);
    return -1;
  }

  return 0;
}

static PyGetSetDef tp_getset[] = {
    {"colors", get_colors, set_colors, "list of colors in this sequence", NULL},
    {NULL},
};

static PyMethodDef tp_methods[] = {
    {"interpolate", (PyCFunctionWithKeywords)interpolate,
     METH_VARARGS | METH_KEYWORDS,
     "interpolate the color sequence at one or more points using the given "
     "interpolation type"},
    {NULL},
};

static PyMappingMethods tp_as_mapping = {
    .mp_length = mp_length,
    .mp_subscript = mp_subscript,
    .mp_ass_subscript = mp_ass_subscript,
};

PyTypeObject ColorSequenceType = {
    PyVarObject_HEAD_INIT(NULL, 0).tp_name = "pysicgl.ColorSequence",
    .tp_doc = PyDoc_STR("sicgl color"),
    .tp_basicsize = sizeof(ColorSequenceObject),
    .tp_itemsize = 0,
    .tp_flags = Py_TPFLAGS_DEFAULT,
    .tp_new = PyType_GenericNew,
    .tp_dealloc = tp_dealloc,
    .tp_init = tp_init,
    .tp_getset = tp_getset,
    .tp_methods = tp_methods,
    .tp_as_mapping = &tp_as_mapping,
};

// additional initialization for this type
int ColorSequence_post_ready_init() {
  int ret = 0;

  // add INTERP constants to class dict
  for (size_t idx = 0; idx < num_interp_types; idx++) {
    ret = PyDict_SetItem(
        ColorSequenceType.tp_dict,
        PyUnicode_FromFormat("INTERP_%s", interp_types[idx].name),
        PyLong_FromLong(idx));
    if (0 != ret) {
      return ret;
    }
  }

  return ret;
}
