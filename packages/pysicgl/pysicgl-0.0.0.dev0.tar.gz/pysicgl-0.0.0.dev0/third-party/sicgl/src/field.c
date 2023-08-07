#include "sicgl/field.h"

#include <errno.h>

#include "sicgl/debug.h"
#include "sicgl/translate.h"

/**
 * @brief Map a color sequence onto a scalar field.
 * Parameterizes mapping with the 'map' function.
 * Internal use.
 *
 * @param interface
 * @param field screen defining the region over which to apply the field.
 * coordinates must be in interface
 * @param scalars scalar values to map to colors for each pixel. assumed to have
 * sufficient length for the size of 'field' screen
 * @param sequence color sequence used
 * @param map function for mapping scalar value to color
 * @return int
 */
int sicgl_scalar_field(
    interface_t* interface, screen_t* field, double* scalars, double offset,
    color_sequence_t* sequence, sequence_map_fn map) {
  int ret = 0;

  if (NULL == interface) {
    goto out;
  }
  if (NULL == field) {
    ret = -ENOMEM;
    goto out;
  }
  if (NULL == scalars) {
    ret = -ENOMEM;
    goto out;
  }
  if (NULL == sequence) {
    ret = -ENOMEM;
    goto out;
  }
  if (NULL == map) {
    ret = -EINVAL;
    goto out;
  }
  if (NULL == interface->screen) {
    ret = -ENOMEM;
    goto out;
  }

  // find screen overlap
  screen_t intersection;
  ret = screen_intersect(&intersection, field, interface->screen);
  if (ret == SICGL_SCREEN_INTERSECTION_NONEXISTENT) {
    ret = 0;
    goto out;
  } else if (0 != ret) {
    goto out;
  }

  // assumptions:
  // - scalar buffer is large enough to fill the entire scalar screen
  // - intersection of the scalar screen with the interface screen will
  //   yeild a screen that is no larger than the sprite screen
  // - scalar field is in the same pixel arrangement as images (row contiguous)

  // determine starting location in both sprite and target screens
  // (intersection screen is computed in global coordinates)
  // scalar screen starting location:
  ext_t su0 = intersection.u0;
  ext_t sv0 = intersection.v0;
  ret = translate_screen_to_screen(&intersection, field, &su0, &sv0);
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
  size_t scalar_offset = field->width * sv0 + su0;
  size_t interface_offset = interface->screen->width * tv0 + tu0;

  // then simply loop over the intersection screen height copying data from
  // the scalar buffer to the target buffer (using the full width of the
  // intersection)
  for (size_t idv = 0; idv < intersection.height; idv++) {
    for (size_t idu = 0; idu < intersection.width; idu++) {
      color_t color;
      ret = map(sequence, scalars[scalar_offset] + offset, &color);
      if (0 != ret) {
        goto out;
      }
      interface->memory[interface_offset] = color;

      // advance the offsets along the row
      scalar_offset++;
      interface_offset++;
    }

    // new line, carriage return
    scalar_offset += field->width - intersection.width;
    interface_offset += interface->screen->width - intersection.width;
  }

out:
  return ret;
}
