#pragma once

#include <stddef.h>

#include "sicgl/color.h"

int interpolate_color_linear(
    color_t* colors, size_t length, double phase, color_t* color);
int interpolate_color_circular(
    color_t* colors, size_t length, double phase, color_t* color);
