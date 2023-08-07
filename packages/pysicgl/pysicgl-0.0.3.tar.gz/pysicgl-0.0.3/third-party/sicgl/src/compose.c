#include "sicgl/compose.h"

#include <errno.h>

#include "sicgl/debug.h"
#include "sicgl/screen.h"
#include "sicgl/translate.h"

/**
 * @brief Bit-blit a sprite into the region determined by screen upon the
 * interface.
 *
 * @param interface
 * @param screen
 * @param sprite
 * @return int
 */
int sicgl_compose(
    interface_t* interface, screen_t* screen, color_t* sprite,
    compositor_fn compositor) {
  int ret = 0;

  if (NULL == interface) {
    goto out;
  }
  if (NULL == screen) {
    ret = -ENOMEM;
    goto out;
  }
  if (NULL == sprite) {
    ret = -ENOMEM;
    goto out;
  }
  if (NULL == interface->screen) {
    ret = -ENOMEM;
    goto out;
  }
  if (NULL == compositor) {
    ret = -EINVAL;
    goto out;
  }

  // find screen overlap
  screen_t intersection;
  ret = screen_intersect(&intersection, screen, interface->screen);
  if (ret == SICGL_SCREEN_INTERSECTION_NONEXISTENT) {
    ret = 0;
    goto out;
  } else if (0 != ret) {
    goto out;
  }

  // assumptions:
  // - sprite buffer is large enough to fill the entire sprite screen
  // - intersection of the sprite screen with the interface screen will
  //   yeild a screen that is no larger than the sprite screen

  // determine starting location in both sprite and target screens
  // (intersection screen is computed in global coordinates)
  // sprite screen starting location:
  ext_t su0 = intersection.u0;
  ext_t sv0 = intersection.v0;
  ret = translate_screen_to_screen(&intersection, screen, &su0, &sv0);
  if (0 != ret) {
    goto out;
  }

  // target screen starting location:
  ext_t tu0 = interface->screen->u0;
  ext_t tv0 = interface->screen->v0;
  ret =
      translate_screen_to_screen(&intersection, interface->screen, &tu0, &tv0);
  if (0 != ret) {
    goto out;
  }

  // the starting positions give us the starting offsets into the appropriate
  // buffers
  size_t sprite_offset = screen->width * sv0 + su0;
  size_t interface_offset = interface->screen->width * tv0 + tu0;

  // then simply loop over the intersection screen height copying data from
  // the sprite buffer to the target buffer (using the full width of the
  // intersection)
  for (size_t idx = 0; idx < intersection.height; idx++) {
    compositor(
        &sprite[sprite_offset], &interface->memory[interface_offset],
        intersection.width);

    // add whole rows to sprite and interface offsets
    sprite_offset += screen->width;
    interface_offset += interface->screen->width;
  }

out:
  return ret;
}
