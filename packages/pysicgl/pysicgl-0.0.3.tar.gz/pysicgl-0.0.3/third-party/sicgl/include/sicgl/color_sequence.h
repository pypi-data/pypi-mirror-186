#pragma once

#include <stddef.h>
#include <stdint.h>

#include "sicgl/color.h"

typedef struct _color_sequence_t {
  color_t* colors;
  size_t length;
} color_sequence_t;

static inline size_t color_sequence_length(color_sequence_t* sequence) {
  size_t len = 0;
  if (NULL == sequence) {
    goto out;
  }
  len = sequence->length;
out:
  return len;
}

typedef int (*sequence_map_fn)(
    color_sequence_t* sequence, double phase, color_t* color);

int color_sequence_initialize(
    color_sequence_t* sequence, color_t* buffer, size_t length);
int color_sequence_set_color(
    color_sequence_t* sequence, size_t idx, color_t color);
int color_sequence_get_color(
    color_sequence_t* sequence, size_t idx, color_t* color);

// color sequence map functions
// map a double to a color from a color sequence
int color_sequence_interpolate_color_continuous_linear(
    color_sequence_t* sequence, double phase, color_t* color);
int color_sequence_interpolate_color_continuous_circular(
    color_sequence_t* sequence, double phase, color_t* color);

int color_sequence_interpolate_color_discrete_linear(
    color_sequence_t* sequence, double phase, color_t* color);
int color_sequence_interpolate_color_discrete_circular(
    color_sequence_t* sequence, double phase, color_t* color);
