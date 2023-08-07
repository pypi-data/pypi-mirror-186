#include "sicgl/translate.h"

#include <errno.h>
#include <stddef.h>

#include "sicgl/debug.h"

int translate_screen_to_screen(
    screen_t* from, screen_t* to, ext_t* u, ext_t* v) {
  int ret = 0;
  if ((NULL == from) || (NULL == to)) {
    ret = -ENOMEM;
    goto out;
  }

  // perform translation
  if (NULL != u) {
    *u = *u + from->lu - to->lu;
  }
  if (NULL != v) {
    *v = *v + from->lv - to->lv;
  }

out:
  return ret;
}

int translate_screen_to_global(screen_t* screen, ext_t* u, ext_t* v) {
  int ret = 0;
  if (NULL == screen) {
    ret = -ENOMEM;
    goto out;
  }

  // perform translation
  if (NULL != u) {
    *u = *u + screen->lu;
  }
  if (NULL != v) {
    *v = *v + screen->lv;
  }

out:
  return ret;
}

int translate_global_to_screen(screen_t* screen, ext_t* u, ext_t* v) {
  int ret = 0;
  if (NULL == screen) {
    ret = -ENOMEM;
    goto out;
  }

  // perform translation
  if (NULL != u) {
    *u = *u - screen->lu;
  }
  if (NULL != v) {
    *v = *v - screen->lv;
  }

out:
  return ret;
}
