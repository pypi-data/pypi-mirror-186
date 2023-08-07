#include "sicgl/domain/global.h"

#include "sicgl/debug.h"
#include "sicgl/domain/interface.h"
#include "sicgl/translate.h"

/**
 * @brief Global-relative drawing functions.
 * Coordinates are taken in global frame.
 * Valid drawing area is the interface's display only.
 *
 */

int sicgl_global_pixel(
    interface_t* interface, color_t color, ext_t u0, ext_t v0) {
  int ret = 0;
  ret = translate_global_to_screen(interface->screen, &u0, &v0);
  if (0 != ret) {
    goto out;
  }
  ret = sicgl_interface_pixel(interface, color, u0, v0);

out:
  return ret;
}

int sicgl_global_line(
    interface_t* interface, color_t color, ext_t u0, ext_t v0, ext_t u1,
    ext_t v1) {
  int ret = 0;
  ret = translate_global_to_screen(interface->screen, &u0, &v0);
  if (0 != ret) {
    goto out;
  }
  ret = translate_global_to_screen(interface->screen, &u1, &v1);
  if (0 != ret) {
    goto out;
  }
  ret = sicgl_interface_line(interface, color, u0, v0, u1, v1);

out:
  return ret;
}

int sicgl_global_rectangle(
    interface_t* interface, color_t color, ext_t u0, ext_t v0, ext_t u1,
    ext_t v1) {
  int ret = 0;
  ret = translate_global_to_screen(interface->screen, &u0, &v0);
  if (0 != ret) {
    goto out;
  }
  ret = translate_global_to_screen(interface->screen, &u1, &v1);
  if (0 != ret) {
    goto out;
  }
  ret = sicgl_interface_rectangle(interface, color, u0, v0, u1, v1);

out:
  return ret;
}

int sicgl_global_rectangle_filled(
    interface_t* interface, color_t color, ext_t u0, ext_t v0, ext_t u1,
    ext_t v1) {
  int ret = 0;

  ret = translate_global_to_screen(interface->screen, &u0, &v0);
  if (0 != ret) {
    goto out;
  }
  ret = translate_global_to_screen(interface->screen, &u1, &v1);
  if (0 != ret) {
    goto out;
  }

  ret = sicgl_interface_rectangle_filled(interface, color, u0, v0, u1, v1);
  if (0 != ret) {
    goto out;
  }

out:
  return ret;
}

int sicgl_global_circle_bresenham(
    interface_t* interface, color_t color, ext_t u0, ext_t v0, ext_t diameter) {
  int ret = 0;
  ret = translate_global_to_screen(interface->screen, &u0, &v0);
  if (0 != ret) {
    goto out;
  }
  ret = sicgl_interface_circle_bresenham(interface, color, u0, v0, diameter);

out:
  return ret;
}

int sicgl_global_circle_ellipse(
    interface_t* interface, color_t color, ext_t u0, ext_t v0, ext_t diameter) {
  int ret = 0;
  ret = translate_global_to_screen(interface->screen, &u0, &v0);
  if (0 != ret) {
    goto out;
  }
  ret = sicgl_interface_circle_ellipse(interface, color, u0, v0, diameter);

out:
  return ret;
}

int sicgl_global_ellipse(
    interface_t* interface, color_t color, ext_t u0, ext_t v0, ext_t semiu,
    ext_t semiv) {
  int ret = 0;
  ret = translate_global_to_screen(interface->screen, &u0, &v0);
  if (0 != ret) {
    goto out;
  }
  ret = sicgl_interface_ellipse(interface, color, u0, v0, semiu, semiv);

out:
  return ret;
}
