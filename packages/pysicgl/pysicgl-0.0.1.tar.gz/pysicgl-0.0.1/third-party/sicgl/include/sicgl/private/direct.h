#pragma once

#include "sicgl/interface.h"

static inline void sicgl_direct_pixel(
    interface_t* interface, color_t color, ext_t u, ext_t v) {
  if (NULL == interface->screen) {
    goto out;
  }
  size_t offset = interface->screen->width * v + u;
  interface->memory[offset] = color;
out:
  return;
}

void sicgl_direct_hrun(
    interface_t* interface, color_t color, uext_t u, uext_t v, ext_t du);
void sicgl_direct_vrun(
    interface_t* interface, color_t color, uext_t u, uext_t v, ext_t dv);
void sicgl_direct_hline(
    interface_t* interface, color_t color, uext_t u0, uext_t v, uext_t u1);
void sicgl_direct_vline(
    interface_t* interface, color_t color, uext_t u, uext_t v0, uext_t v1);
void sicgl_direct_diagonal(
    interface_t* interface, color_t color, uext_t u0, uext_t v0, ext_t diru,
    ext_t dirv, uext_t count);
void sicgl_direct_region(
    interface_t* interface, color_t color, uext_t u0, uext_t v0, uext_t u1,
    uext_t v1);
