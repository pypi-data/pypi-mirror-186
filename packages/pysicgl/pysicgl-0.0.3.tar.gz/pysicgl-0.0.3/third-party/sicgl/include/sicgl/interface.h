#pragma once

#include <string.h>

#include "sicgl/color.h"
#include "sicgl/color_sequence.h"
#include "sicgl/extent.h"
#include "sicgl/screen.h"

typedef struct _interface_t {
  screen_t* screen;  // geometrical display info
  color_t* memory;   // pointer to start of specific memory
  size_t length;     // memory length in pixels
} interface_t;
