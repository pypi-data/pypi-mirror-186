#pragma once

#include <stdint.h>

// colors are represented as a system int
// https://github.com/oclyke/sicgl/issues/24
// if necessary the user can change this definition
typedef int color_t;

// size of a color_t variable in bytes (must be positive... duh)
static inline int bytes_per_pixel(void) {
  return (sizeof(color_t) / sizeof(uint8_t));
}

// tools to get individual color channels
static inline color_t color_channel_alpha(color_t color) {
  return ((color >> 24U) & 0xff);
}
static inline color_t color_channel_red(color_t color) {
  return ((color >> 16U) & 0xff);
}
static inline color_t color_channel_green(color_t color) {
  return ((color >> 8U) & 0xff);
}
static inline color_t color_channel_blue(color_t color) {
  return ((color >> 0U) & 0xff);
}

// tools to assemble color channels
static inline color_t color_from_channels(
    color_t red, color_t green, color_t blue, color_t alpha) {
  return (
      (((alpha & 0xff) << 24U) | (red & 0xff) << 16U) | ((green & 0xff) << 8U) |
      ((blue & 0xff) << 0U));
}
