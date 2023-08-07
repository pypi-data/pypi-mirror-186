#include <errno.h>
#include <stddef.h>

#include "sicgl/debug.h"
#include "sicgl/interface.h"

void sicgl_direct_hrun(
    interface_t* interface, color_t color, uext_t u, uext_t v, ext_t du) {
  if (NULL == interface->screen) {
    goto out;
  }
  int increment = (du > 0) ? 1 : -1;
  int count = (du > 0) ? du : -du;
  size_t offset = interface->screen->width * v + u;
  while (count-- > 0) {
    interface->memory[offset] = color;
    offset += increment;
  }
out:
  return;
}

void sicgl_direct_vrun(
    interface_t* interface, color_t color, uext_t u, uext_t v, ext_t dv) {
  if (NULL == interface->screen) {
    goto out;
  }
  uext_t width = interface->screen->width;
  int increment = (dv > 0) ? width : -width;
  int count = (dv > 0) ? dv : -dv;
  size_t offset = width * v + u;
  while (count-- > 0) {
    interface->memory[offset] = color;
    offset += increment;
  }
out:
  return;
}

void sicgl_direct_hline(
    interface_t* interface, color_t color, uext_t u0, uext_t v, uext_t u1) {
  if (NULL == interface->screen) {
    goto out;
  }
  int increment;
  size_t distance;
  if (u0 < u1) {
    increment = 1;
    distance = u1 - u0 + 1;
  } else {
    increment = -1;
    distance = u0 - u1 + 1;
  }

  size_t offset = interface->screen->width * v + u0;
  for (size_t idx = 0; idx < distance; idx++) {
    interface->memory[offset] = color;
    offset += increment;
  }
out:
  return;
}

void sicgl_direct_vline(
    interface_t* interface, color_t color, uext_t u, uext_t v0, uext_t v1) {
  if (NULL == interface->screen) {
    goto out;
  }
  int increment;
  size_t distance;
  if (v0 < v1) {
    increment = interface->screen->width;
    distance = v1 - v0 + 1;
  } else {
    increment = -interface->screen->width;
    distance = v0 - v1 + 1;
  }

  size_t offset = interface->screen->width * v0 + u;
  for (size_t idv = 0; idv < distance; idv++) {
    interface->memory[offset] = color;
    offset += increment;
  }
out:
  return;
}

void sicgl_direct_diagonal(
    interface_t* interface, color_t color, uext_t u0, uext_t v0, ext_t diru,
    ext_t dirv, uext_t count) {
  if (NULL == interface->screen) {
    goto out;
  }
  int du, dv;
  if (diru > 0) {
    du = 1;
  } else {
    du = -1;
  }
  if (dirv > 0) {
    dv = interface->screen->width;
  } else {
    dv = -interface->screen->width;
  }

  size_t offset = interface->screen->width * v0 + u0;
  for (uext_t idx = 0; idx < count; idx++) {
    interface->memory[offset] = color;
    offset += du;
    offset += dv;
  }
out:
  return;
}

void sicgl_direct_region(
    interface_t* interface, color_t color, uext_t u0, uext_t v0, uext_t u1,
    uext_t v1) {
  if (NULL == interface->screen) {
    goto out;
  }
  size_t du;
  size_t dv;
  size_t offset;
  uext_t width = interface->screen->width;

  // compute values
  if (u0 < u1) {
    offset = u0;
    du = u1 - u0 + 1;
  } else {
    offset = u1;
    du = u0 - u1 + 1;
  }
  if (v0 < v1) {
    offset += width * v0;
    dv = v1 - v0 + 1;
  } else {
    offset += width * v1;
    dv = v0 - v1 + 1;
  }

  // first: fill up one row
  for (size_t idu = 0; idu < du; idu++) {
    interface->memory[offset + idu] = color;
  }

  // then copy that memory region repeatedly for each subsequent row
  // copy scratch buffer into each
  size_t bpp = bytes_per_pixel();
  color_t* row = &interface->memory[offset];
  while (dv > 0) {
    memcpy(row, &interface->memory[offset], du * bpp);
    row += width;  // go to next row by advancing the fulll width
    dv--;
  }
out:
  return;
}
