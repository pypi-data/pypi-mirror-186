#include "sicgl/private/interpolation.h"

#include <errno.h>
#include <math.h>

#include "sicgl/debug.h"

static inline int interpolate_color_between(
    color_t lower, color_t upper, double phase, color_t* color) {
  int ret = 0;
  if (NULL == color) {
    ret = -ENOMEM;
    goto out;
  }

  // interpolate channels individually
  color_t red = (phase * ((int)color_channel_red(upper) -
                          (int)color_channel_red(lower))) +
                color_channel_red(lower);
  color_t green = (phase * ((int)color_channel_green(upper) -
                            (int)color_channel_green(lower))) +
                  color_channel_green(lower);
  color_t blue = (phase * ((int)color_channel_blue(upper) -
                           (int)color_channel_blue(lower))) +
                 color_channel_blue(lower);
  color_t alpha = (phase * ((int)color_channel_alpha(upper) -
                            (int)color_channel_alpha(lower))) +
                  color_channel_alpha(lower);

  // assemble the resulting color
  *color = color_from_channels(red, green, blue, alpha);

out:
  return ret;
}

int interpolate_color_linear(
    color_t* colors, size_t length, double phase, color_t* color) {
  int ret = 0;

  // user does not need result
  if (NULL == color) {
    goto out;
  }

  // cannot interpolate nonexistent list
  if (NULL == colors) {
    ret = -ENOMEM;
    goto out;
  }
  if (0 == length) {
    ret = -EINVAL;
    goto out;
  }

  // nothing to interpolate when input has single element
  if (1 == length) {
    *color = colors[0];
    goto out;
  }

  // linear interpolation gets clamped at the array bounds
  if (phase <= 0.0f) {
    *color = colors[0];
    goto out;
  } else if (phase >= 1.0f) {
    *color = colors[length - 1];
    goto out;
  }

  // get bounding values
  size_t max_idx = length - 1;
  double center = phase * max_idx;   // center E [0, max_idx]
  size_t lower_idx = floor(center);  // lower E [0, max_idx], integer
  size_t upper_idx = ceil(center);   // upper E [0, max_idx], integer

  // handle balance case
  if (lower_idx == upper_idx) {
    *color = colors[lower_idx];
    goto out;
  }

  // get delta from the lower index
  double spacing = 1.0f / max_idx;
  double delta = (phase / spacing) - lower_idx;

  // interpolate between these two colors
  ret = interpolate_color_between(
      colors[lower_idx], colors[upper_idx], delta, color);
  if (0 != ret) {
    goto out;
  }

out:
  return ret;
}

int interpolate_color_circular(
    color_t* colors, size_t length, double phase, color_t* color) {
  int ret = 0;

  // user does not need result
  if (NULL == color) {
    goto out;
  }

  // cannot interpolate nonexistent list
  if (NULL == colors) {
    ret = -ENOMEM;
    goto out;
  }
  if (0 == length) {
    ret = -EINVAL;
    goto out;
  }

  // nothing to interpolate when input has single element
  if (1 == length) {
    *color = colors[0];
    goto out;
  }

  // circular interpolation restricts the phase to the range [0.0, 1.0]
  phase = fmod(phase, 1.0f);
  if (phase < 0.0f) {
    phase += 1.0f;
  }

  // get bounding values
  double center = phase * length;    // center E [0, length]
  size_t lower_idx = floor(center);  // lower E [0, length], integer
  size_t upper_idx = ceil(center);   // upper E [0, length], integer

  // handle balance case
  if (lower_idx == upper_idx) {
    *color = (lower_idx == length) ? colors[0] : colors[lower_idx];
    goto out;
  }

  // handle wraparound
  if (upper_idx == length) {
    upper_idx = 0;
  }

  // get delta from the lower
  double spacing = 1.0f / length;
  double delta = (phase / spacing) - lower_idx;

  // interpolate between these two colors
  ret = interpolate_color_between(
      colors[lower_idx], colors[upper_idx], delta, color);
  if (0 != ret) {
    goto out;
  }

out:
  return ret;
}
