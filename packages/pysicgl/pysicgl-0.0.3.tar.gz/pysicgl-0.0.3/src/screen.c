#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <structmember.h>
// python includes must come first

#include <errno.h>
#include <stdio.h>

#include "pysicgl/screen.h"
#include "pysicgl/utilities.h"

// fwd declarations
static PyObject* tp_new(PyTypeObject* type, PyObject* args, PyObject* kwds);

// getset
static PyObject* get_width(PyObject* self_in, void* closure) {
  return PyLong_FromLong(((ScreenObject*)self_in)->screen->width);
}
static PyObject* get_height(PyObject* self_in, void* closure) {
  return PyLong_FromLong(((ScreenObject*)self_in)->screen->height);
}
static PyObject* get_pixels(PyObject* self_in, void* closure) {
  ScreenObject* self = (ScreenObject*)self_in;
  return PyLong_FromLong(self->screen->width * self->screen->height);
}
static PyObject* get_corners(PyObject* self_in, void* closure) {
  ScreenObject* self = (ScreenObject*)self_in;
  return Py_BuildValue(
      "(ii)(ii)", self->screen->u0, self->screen->v0, self->screen->u1,
      self->screen->v1);
}
static PyObject* get_global_corners(PyObject* self_in, void* closure) {
  ScreenObject* self = (ScreenObject*)self_in;
  return Py_BuildValue(
      "(ii)(ii)", self->screen->_gu0, self->screen->_gv0, self->screen->_gu1,
      self->screen->_gv1);
}
static PyObject* get_extent(PyObject* self_in, void* closure) {
  ScreenObject* self = (ScreenObject*)self_in;
  return Py_BuildValue("(ii)", self->screen->width, self->screen->height);
}
static PyObject* get_location(PyObject* self_in, void* closure) {
  ScreenObject* self = (ScreenObject*)self_in;
  return Py_BuildValue("(ii)", self->screen->lu, self->screen->lv);
}

static int set_extent(PyObject* self_in, PyObject* val, void* closure) {
  ScreenObject* self = (ScreenObject*)self_in;
  ext_t width, height;
  if (!PyArg_ParseTuple(val, "(ii)", &width, &height)) {
    return -1;
  }

  int ret = screen_set_extent(self->screen, width, height);
  if (0 != ret) {
    PyErr_SetNone(PyExc_OSError);
    return -1;
  }

  return 0;
}

static int set_location(PyObject* self_in, PyObject* val, void* closure) {
  ScreenObject* self = (ScreenObject*)self_in;

  ext_t lu, lv;
  if (!PyArg_ParseTuple(val, "(ii)", &lu, &lv)) {
    return -1;
  }

  int ret = screen_set_location(self->screen, lu, lv);
  if (0 != ret) {
    PyErr_SetNone(PyExc_OSError);
    return -1;
  }

  return 0;
}

// methods
static PyObject* intersect(PyObject* self, PyObject* args) {
  PyObject* _s0;
  PyObject* _s1;
  if (!PyArg_ParseTuple(args, "O!O!", &ScreenType, &_s0, &ScreenType, &_s1)) {
    return NULL;
  }
  ScreenObject* s0 = (ScreenObject*)_s0;
  ScreenObject* s1 = (ScreenObject*)_s1;

  // create a new screen object as the target
  PyObject* target_obj = tp_new(&ScreenType, NULL, NULL);
  ScreenObject* target = (ScreenObject*)target_obj;

  int ret = screen_intersect(target->screen, s0->screen, s1->screen);
  if (0 != ret) {
    PyErr_SetNone(PyExc_OSError);
    return NULL;
  }

  return target_obj;
}

static PyObject* normalize(PyObject* self_in, PyObject* args) {
  ScreenObject* self = (ScreenObject*)self_in;
  int ret = screen_normalize(self->screen);
  if (0 != ret) {
    PyErr_SetNone(PyExc_OSError);
    return NULL;
  }
  return Py_None;
}

static PyObject* set_corners(PyObject* self_in, PyObject* args) {
  ScreenObject* self = (ScreenObject*)self_in;
  ext_t u0, v0, u1, v1;
  if (!PyArg_ParseTuple(args, "(ii)(ii)", &u0, &v0, &u1, &v1)) {
    return NULL;
  }

  int ret = screen_set_corners(self->screen, u0, v0, u1, v1);
  if (0 != ret) {
    PyErr_SetNone(PyExc_OSError);
    return NULL;
  }
  ret = screen_normalize(self->screen);
  if (0 != ret) {
    PyErr_SetNone(PyExc_OSError);
    return NULL;
  }

  return Py_None;
}

/**
 * @brief Create a new screen reference.
 * When the reference is NULL the screen will refer to
 * its own internal structure and be a standalone object.
 *
 * @param ref
 * @return PyObject*
 */
ScreenObject* new_screen_object(screen_t* ref) {
  ScreenObject* self = (ScreenObject*)(ScreenType.tp_alloc(&ScreenType, 0));
  if (self != NULL) {
    if (NULL == ref) {
      self->screen = &self->_screen;
      self->_is_reference = false;
    } else {
      self->screen = ref;
      self->_is_reference = true;
    }
    int ret = screen_normalize(self->screen);
    if (0 != ret) {
      PyErr_SetNone(PyExc_OSError);
      Py_DECREF(self);
      return NULL;
    }
  }

  return self;
}

/**
 *
 * @brief Create a new screen object.
 *
 * @param type
 * @param args
 * @param kwds
 * @return PyObject*
 */
static PyObject* tp_new(PyTypeObject* type, PyObject* args, PyObject* kwds) {
  ScreenObject* self = new_screen_object(NULL);
  return (PyObject*)self;
}

static int tp_init(PyObject* self_in, PyObject* args, PyObject* kwds) {
  ScreenObject* self = (ScreenObject*)self_in;
  int ret = 0;
  char* keywords[] = {
      "extent",
      "location",
      NULL,
  };
  ext_t width, height;
  ext_t lu = 0;
  ext_t lv = 0;
  if (!PyArg_ParseTupleAndKeywords(
          args, kwds, "(ii)|(ii)", keywords, &width, &height, &lu, &lv)) {
    return -1;
  }

  ret = screen_set_extent(self->screen, width, height);
  if (0 != ret) {
    PyErr_SetNone(PyExc_OSError);
    return -1;
  }

  ret = screen_set_location(self->screen, lu, lv);
  if (0 != ret) {
    PyErr_SetNone(PyExc_OSError);
    return -1;
  }

  ret = screen_normalize(self->screen);
  if (0 != ret) {
    PyErr_SetNone(PyExc_OSError);
    return -1;
  }

  return 0;
}

static PyMethodDef tp_methods[] = {
    {"intersect", (PyCFunction)intersect, METH_VARARGS | METH_STATIC,
     "return the intersection of two screens in global space"},
    {"normalize", (PyCFunction)normalize, METH_NOARGS,
     "normalize the screen to satisy constraints"},
    {"set_corners", (PyCFunction)set_corners, METH_VARARGS,
     "set the coordinates of screen corners in screen-relative system"},
    {NULL},
};

static PyGetSetDef tp_getset[] = {
    {"width", get_width, NULL, "width in pixels", NULL},
    {"height", get_height, NULL, "height in pixels", NULL},
    {"pixels", get_pixels, NULL, "total number of pixels", NULL},
    {"corners", get_corners, NULL,
     "coordinates of corners in screen-relative system", NULL},
    {"global_corners", get_global_corners, NULL,
     "coordinates of corners in global system", NULL},
    {"extent", get_extent, set_extent, "dimensions in pixels (width, height)",
     NULL},
    {"location", get_location, set_location,
     "location of screen in global system", NULL},
    {NULL},
};

PyTypeObject ScreenType = {
    PyVarObject_HEAD_INIT(NULL, 0).tp_name = "pysicgl.Screen",
    .tp_doc = PyDoc_STR("sicgl screen"),
    .tp_basicsize = sizeof(ScreenObject),
    .tp_itemsize = 0,
    .tp_flags = Py_TPFLAGS_DEFAULT,
    .tp_new = tp_new,
    .tp_init = tp_init,
    .tp_methods = tp_methods,
    .tp_getset = tp_getset,
};
