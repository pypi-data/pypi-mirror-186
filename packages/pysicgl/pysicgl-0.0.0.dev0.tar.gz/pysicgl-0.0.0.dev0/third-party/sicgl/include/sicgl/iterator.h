#pragma once

#include <stdbool.h>

// a generic iterator which carries user defined data
typedef struct _iter_t {
  // iterator function pointers
  void* (*first)(void* args);
  void* (*next)(void* args);
  bool (*done)(void* args);

  // user data
  void* args;
} iter_t;

void iter_foreach(iter_t iter, void (*callback)(void*), void* arg);
