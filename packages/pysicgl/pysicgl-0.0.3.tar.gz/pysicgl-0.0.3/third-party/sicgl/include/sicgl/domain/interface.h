#pragma once

#include "sicgl/interface.h"

// write direct-to-display
int sicgl_interface_fill(interface_t* interface, color_t color);
int sicgl_interface_pixel(
    interface_t* interface, color_t color, ext_t u0, ext_t v0);
int sicgl_interface_line(
    interface_t* interface, color_t color, ext_t u0, ext_t v0, ext_t u1,
    ext_t v1);
int sicgl_interface_rectangle(
    interface_t* interface, color_t color, ext_t u0, ext_t v0, ext_t u1,
    ext_t v1);
int sicgl_interface_rectangle_filled(
    interface_t* interface, color_t color, ext_t u0, ext_t v0, ext_t u1,
    ext_t v1);
int sicgl_interface_circle_bresenham(
    interface_t* interface, color_t color, ext_t u0, ext_t v0, ext_t diameter);
int sicgl_interface_circle_ellipse(
    interface_t* interface, color_t color, ext_t u0, ext_t v0, ext_t diameter);
int sicgl_interface_ellipse(
    interface_t* interface, color_t color, ext_t u0, ext_t v0, ext_t semiu,
    ext_t semiv);
