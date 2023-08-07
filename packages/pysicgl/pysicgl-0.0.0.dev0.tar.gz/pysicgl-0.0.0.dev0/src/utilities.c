#define PY_SSIZE_T_CLEAN
#include <Python.h>
// python includes must come first

#include <errno.h>

#include "pysicgl/utilities.h"

/**
 * @brief Unpack a Python Tuple object with two elements into ext_t outputs.
 *
 * @param obj
 * @param u
 * @param v
 * @return int
 */
int unpack_ext_t_tuple2(PyObject* obj, ext_t* u, ext_t* v) {
  int ret = 0;

  if (NULL == u) {
    ret = -ENOMEM;
    goto out;
  }

  if (!PyTuple_Check(obj)) {
    ret = -EINVAL;
    goto out;
  }
  if (2 != PyTuple_Size(obj)) {
    ret = -EINVAL;
    goto out;
  }

  *u = PyLong_AsLong(PyTuple_GetItem(obj, 0));
  *v = PyLong_AsLong(PyTuple_GetItem(obj, 1));

out:
  return ret;
}
