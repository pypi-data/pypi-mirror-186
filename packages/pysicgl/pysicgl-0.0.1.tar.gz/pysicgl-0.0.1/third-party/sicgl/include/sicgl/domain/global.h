#pragma once

#include "sicgl/interface.h"
#include "sicgl/screen.h"

// draw in global coordinates
int sicgl_global_pixel(
    interface_t* interface, color_t color, ext_t u0, ext_t v0);
int sicgl_global_line(
    interface_t* interface, color_t color, ext_t u0, ext_t v0, ext_t u1,
    ext_t v1);
int sicgl_global_rectangle(
    interface_t* interface, color_t color, ext_t u0, ext_t v0, ext_t u1,
    ext_t v1);
int sicgl_global_rectangle_filled(
    interface_t* interface, color_t color, ext_t u0, ext_t v0, ext_t u1,
    ext_t v1);
int sicgl_global_circle_bresenham(
    interface_t* interface, color_t color, ext_t u0, ext_t v0, ext_t diameter);
int sicgl_global_circle_ellipse(
    interface_t* interface, color_t color, ext_t u0, ext_t v0, ext_t diameter);
int sicgl_global_ellipse(
    interface_t* interface, color_t color, ext_t u0, ext_t v0, ext_t semiu,
    ext_t semiv);
