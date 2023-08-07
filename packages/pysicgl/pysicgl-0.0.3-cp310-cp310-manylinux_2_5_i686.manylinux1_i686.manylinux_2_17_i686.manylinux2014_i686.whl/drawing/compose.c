#define PY_SSIZE_T_CLEAN
#include <Python.h>
// python includes must come first

#include <errno.h>

#include "pysicgl/drawing/blit.h"
#include "pysicgl/drawing/compose.h"
#include "pysicgl/interface.h"
#include "pysicgl/screen.h"
#include "sicgl/compose.h"

static inline color_t clamp_u8(color_t channel) {
  if (channel > 255) {
    return 255;
  } else if (channel < 0) {
    return 0;
  } else {
    return channel;
  }
}

static void compositor_set(color_t* source, color_t* dest, size_t width) {
  memcpy(dest, source, width * bytes_per_pixel());
}

static void compositor_add_clamped(
    color_t* source, color_t* dest, size_t width) {
  for (size_t idx = 0; idx < width; idx++) {
    dest[idx] = color_from_channels(
        clamp_u8(color_channel_red(dest[idx]) + color_channel_red(source[idx])),
        clamp_u8(
            color_channel_green(dest[idx]) + color_channel_green(source[idx])),
        clamp_u8(
            color_channel_blue(dest[idx]) + color_channel_blue(source[idx])),
        clamp_u8(
            color_channel_alpha(dest[idx]) + color_channel_alpha(source[idx])));
  }
}

static void compositor_subtract_clamped(
    color_t* source, color_t* dest, size_t width) {
  for (size_t idx = 0; idx < width; idx++) {
    dest[idx] = color_from_channels(
        clamp_u8(color_channel_red(dest[idx]) - color_channel_red(source[idx])),
        clamp_u8(
            color_channel_green(dest[idx]) - color_channel_green(source[idx])),
        clamp_u8(
            color_channel_blue(dest[idx]) - color_channel_blue(source[idx])),
        clamp_u8(
            color_channel_alpha(dest[idx]) - color_channel_alpha(source[idx])));
  }
}

static void compositor_multiply_clamped(
    color_t* source, color_t* dest, size_t width) {
  for (size_t idx = 0; idx < width; idx++) {
    dest[idx] = color_from_channels(
        clamp_u8(color_channel_red(dest[idx]) * color_channel_red(source[idx])),
        clamp_u8(
            color_channel_green(dest[idx]) * color_channel_green(source[idx])),
        clamp_u8(
            color_channel_blue(dest[idx]) * color_channel_blue(source[idx])),
        clamp_u8(
            color_channel_alpha(dest[idx]) * color_channel_alpha(source[idx])));
  }
}

static void compositor_AND(color_t* source, color_t* dest, size_t width) {
  for (size_t idx = 0; idx < width; idx++) {
    dest[idx] = color_from_channels(
        color_channel_red(dest[idx]) & color_channel_red(source[idx]),
        color_channel_green(dest[idx]) & color_channel_green(source[idx]),
        color_channel_blue(dest[idx]) & color_channel_blue(source[idx]),
        color_channel_alpha(dest[idx]) & color_channel_alpha(source[idx]));
  }
}

static void compositor_OR(color_t* source, color_t* dest, size_t width) {
  for (size_t idx = 0; idx < width; idx++) {
    dest[idx] = color_from_channels(
        color_channel_red(dest[idx]) | color_channel_red(source[idx]),
        color_channel_green(dest[idx]) | color_channel_green(source[idx]),
        color_channel_blue(dest[idx]) | color_channel_blue(source[idx]),
        color_channel_alpha(dest[idx]) | color_channel_alpha(source[idx]));
  }
}

static void compositor_XOR(color_t* source, color_t* dest, size_t width) {
  for (size_t idx = 0; idx < width; idx++) {
    dest[idx] = color_from_channels(
        color_channel_red(dest[idx]) ^ color_channel_red(source[idx]),
        color_channel_green(dest[idx]) ^ color_channel_green(source[idx]),
        color_channel_blue(dest[idx]) ^ color_channel_blue(source[idx]),
        color_channel_alpha(dest[idx]) ^ color_channel_alpha(source[idx]));
  }
}

PyObject* compose(PyObject* self_in, PyObject* args) {
  InterfaceObject* self = (InterfaceObject*)self_in;
  ScreenObject* screen;
  Py_buffer sprite;
  int mode;
  if (!PyArg_ParseTuple(args, "O!y*i", &ScreenType, &screen, &sprite, &mode)) {
    return NULL;
  }

  compositor_fn compositor = NULL;
  switch (mode) {
    case 0:
      compositor = compositor_set;
      break;

    case 1:
      compositor = compositor_add_clamped;
      break;

    case 2:
      compositor = compositor_subtract_clamped;
      break;

    case 3:
      compositor = compositor_multiply_clamped;
      break;

    case 4:
      compositor = compositor_AND;
      break;

    case 5:
      compositor = compositor_OR;
      break;

    case 6:
      compositor = compositor_XOR;
      break;

    default:
      PyErr_SetNone(PyExc_ValueError);
      return NULL;
      break;
  }

  int ret =
      sicgl_compose(&self->interface, screen->screen, sprite.buf, compositor);
  if (0 != ret) {
    PyErr_SetNone(PyExc_OSError);
    return NULL;
  }
  return Py_None;
}
