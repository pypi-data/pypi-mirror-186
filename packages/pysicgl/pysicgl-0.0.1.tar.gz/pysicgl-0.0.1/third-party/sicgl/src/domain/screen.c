#include "sicgl/domain/screen.h"

#include "sicgl/debug.h"
#include "sicgl/domain/interface.h"
#include "sicgl/translate.h"

/**
 * @brief Screen-relative drawing functions.
 * Coordinates are taken in screen frame.
 * Intersection of the screen and interface's display is the valid drawing area.
 *
 */

int sicgl_screen_fill(interface_t* interface, screen_t* screen, color_t color) {
  int ret = 0;
  ret = sicgl_screen_rectangle_filled(
      interface, screen, color, screen->u0, screen->v0, screen->u1, screen->v1);
out:
  return ret;
}

int sicgl_screen_pixel(
    interface_t* interface, screen_t* screen, color_t color, ext_t u0,
    ext_t v0) {
  int ret = 0;

  // translate coordinates from screen to display
  ret = translate_screen_to_screen(screen, interface->screen, &u0, &v0);
  if (0 != ret) {
    goto out;
  }

  // draw pixel to display
  ret = sicgl_interface_pixel(interface, color, u0, v0);

out:
  return ret;
}

int sicgl_screen_line(
    interface_t* interface, screen_t* screen, color_t color, ext_t u0, ext_t v0,
    ext_t u1, ext_t v1) {
  int ret = 0;
  ret = translate_screen_to_screen(screen, interface->screen, &u0, &v0);
  if (0 != ret) {
    goto out;
  }
  ret = translate_screen_to_screen(screen, interface->screen, &u1, &v1);
  if (0 != ret) {
    goto out;
  }
  ret = sicgl_interface_line(interface, color, u0, v0, u1, v1);

out:
  return ret;
}

int sicgl_screen_rectangle(
    interface_t* interface, screen_t* screen, color_t color, ext_t u0, ext_t v0,
    ext_t u1, ext_t v1) {
  int ret = 0;
  ret = translate_screen_to_screen(screen, interface->screen, &u0, &v0);
  if (0 != ret) {
    goto out;
  }
  ret = translate_screen_to_screen(screen, interface->screen, &u1, &v1);
  if (0 != ret) {
    goto out;
  }
  ret = sicgl_interface_rectangle(interface, color, u0, v0, u1, v1);

out:
  return ret;
}

int sicgl_screen_rectangle_filled(
    interface_t* interface, screen_t* screen, color_t color, ext_t u0, ext_t v0,
    ext_t u1, ext_t v1) {
  int ret = 0;

  ret = translate_screen_to_screen(screen, interface->screen, &u0, &v0);
  if (0 != ret) {
    goto out;
  }
  ret = translate_screen_to_screen(screen, interface->screen, &u1, &v1);
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

int sicgl_screen_circle_bresenham(
    interface_t* interface, screen_t* screen, color_t color, ext_t u0, ext_t v0,
    ext_t diameter) {
  int ret = 0;
  ret = translate_screen_to_screen(screen, interface->screen, &u0, &v0);
  if (0 != ret) {
    goto out;
  }
  ret = sicgl_interface_circle_bresenham(interface, color, u0, v0, diameter);

out:
  return ret;
}

int sicgl_screen_circle_ellipse(
    interface_t* interface, screen_t* screen, color_t color, ext_t u0, ext_t v0,
    ext_t diameter) {
  int ret = 0;
  ret = translate_screen_to_screen(screen, interface->screen, &u0, &v0);
  if (0 != ret) {
    goto out;
  }
  ret = sicgl_interface_circle_ellipse(interface, color, u0, v0, diameter);

out:
  return ret;
}

int sicgl_screen_ellipse(
    interface_t* interface, screen_t* screen, color_t color, ext_t u0, ext_t v0,
    ext_t semiu, ext_t semiv) {
  int ret = 0;
  ret = translate_screen_to_screen(screen, interface->screen, &u0, &v0);
  if (0 != ret) {
    goto out;
  }
  ret = sicgl_interface_ellipse(interface, color, u0, v0, semiu, semiv);

out:
  return ret;
}
