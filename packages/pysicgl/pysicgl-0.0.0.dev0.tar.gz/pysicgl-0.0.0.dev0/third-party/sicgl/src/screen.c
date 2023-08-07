#include "sicgl/screen.h"

#include <errno.h>
#include <stdbool.h>
#include <stddef.h>

#include "sicgl/debug.h"
#include "sicgl/private/minmax.h"

static int recompute_extent(screen_t* screen) {
  int ret = 0;
  if (NULL == screen) {
    ret = -ENOMEM;
    goto out;
  }

  // compute the extent (width and height) from corner coordinates
  screen->width = screen->u1 - screen->u0 + 1;
  screen->height = screen->v1 - screen->v0 + 1;

out:
  return ret;
}

/**
 * @brief Recompute the corners of a screen based on the extent.
 * (u0, v0) is used as the fixed point.
 * Screen is assumed to be normalized.
 *
 * @param screen
 * @return int
 */
static int recompute_corners(screen_t* screen) {
  int ret = 0;
  if (NULL == screen) {
    ret = -ENOMEM;
    goto out;
  }

  // compute the corners from the extent
  screen->u1 = screen->u0 + screen->width - 1;
  screen->v1 = screen->v0 + screen->height - 1;

out:
  return ret;
}

/**
 * @brief Set the corners of a screen all at once.
 * Note: this function does not normalize the screen.
 *
 * @param screen
 * @return int
 */
int screen_set_corners(
    screen_t* screen, ext_t u0, ext_t v0, ext_t u1, ext_t v1) {
  int ret = 0;
  if (NULL == screen) {
    ret = -ENOMEM;
    goto out;
  }

  // set the corners
  screen->u0 = u0;
  screen->v0 = v0;
  screen->u1 = u1;
  screen->v1 = v1;

  // recompute the width and height
  ret = recompute_extent(screen);
  if (0 != ret) {
    goto out;
  }

out:
  return ret;
}

/**
 * @brief DEPRECATED.
 * Set corners and global location of screen.
 *
 * @param screen
 * @param u0
 * @param v0
 * @param u1
 * @param v1
 * @param lu
 * @param lv
 * @return int
 */
int screen_set(
    screen_t* screen, ext_t u0, ext_t v0, ext_t u1, ext_t v1, ext_t lu,
    ext_t lv) {
  int ret = 0;
  if (NULL == screen) {
    ret = -ENOMEM;
    goto out;
  }

  // set the corners
  ret = screen_set_corners(screen, u0, v0, u1, v1);
  if (0 != ret) {
    goto out;
  }

  // set the location
  ret = screen_set_location(screen, lu, lv);
  if (0 != ret) {
    goto out;
  }

out:
  return ret;
}

/**
 * @brief Set the extent of a screen.
 * Corner locations are recomputed using (u0, v0) as the fixed point.
 *
 * @param screen
 * @param width
 * @param height
 * @return int
 */
int screen_set_extent(screen_t* screen, ext_t width, ext_t height) {
  int ret = 0;
  if (NULL == screen) {
    ret = -ENOMEM;
    goto out;
  }

  // set the extent
  screen->width = width;
  screen->height = height;

  // recompute corners
  ret = recompute_corners(screen);
  if (0 != ret) {
    goto out;
  }

out:
  return ret;
}

/**
 * @brief Set the location of a screen in global coordinates.
 *
 * @param screen
 * @param lu
 * @param lv
 * @return int
 */
int screen_set_location(screen_t* screen, ext_t lu, ext_t lv) {
  int ret = 0;
  if (NULL == screen) {
    ret = -ENOMEM;
    goto out;
  }

  // set the screen's location
  screen->lu = lu;
  screen->lv = lv;

out:
  return ret;
}

/**
 * @brief Normalize a screen for subsequent operations.
 * This function enforces assumptions about screen definition.
 *
 * @param screen
 * @return int
 */
int screen_normalize(screen_t* screen) {
  int ret = 0;
  ext_t tmp;
  if (NULL == screen) {
    ret = -ENOMEM;
    goto out;
  }

  // enforce u0 <= u1
  // it is valid to swap only the u coordinates borders share corners
  if (screen->u1 < screen->u0) {
    tmp = screen->u0;
    screen->u0 = screen->u1;
    screen->u1 = tmp;
  }

  // enforce v0 <= v1
  // it is valid to swap only the v coordinates borders share corners
  if (screen->v1 < screen->v0) {
    tmp = screen->v0;
    screen->v0 = screen->v1;
    screen->v1 = tmp;
  }

  // compute global location
  screen->_gu0 = screen->lu + screen->u0;
  screen->_gv0 = screen->lv + screen->v0;
  screen->_gu1 = screen->lu + screen->u1;
  screen->_gv1 = screen->lv + screen->v1;

  screen->width = screen->u1 - screen->u0 + 1;
  screen->height = screen->v1 - screen->v0 + 1;

out:
  return ret;
}

/**
 * @brief Intersect screens so that target defines
 * the common area between them. This intersection
 * is computed in global coordinates.
 *
 * Input screens must be normalized prior.
 *
 * Returns:
 *   SICGL_SCREEN_INTERSECTION_EXISTS: success, intersection exists
 *   SICGL_SCREEN_INTERSECTION_NONEXISTENT: success, intersection does not exist
 *   negative error code: failure
 *
 * @param target
 * @param s0
 * @param s1
 * @return int
 */
int screen_intersect(screen_t* target, screen_t* s0, screen_t* s1) {
  int ret = 0;
  if ((NULL == s0) || (NULL == s1)) {
    ret = -ENOMEM;
    goto out;
  }

  // check for complete disagreement
  if ((s0->_gu1 < s1->_gu0) || (s0->_gv1 < s1->_gv0) || (s1->_gu1 < s0->_gu0) ||
      (s1->_gv1 < s0->_gv0)) {
    ret = SICGL_SCREEN_INTERSECTION_NONEXISTENT;
    goto out;
  }

  // optionally fill the target with the intersection
  if (NULL != target) {
    // determine global coordinates of intersection
    target->_gu0 = max(s0->_gu0, s1->_gu0);
    target->_gv0 = max(s0->_gv0, s1->_gv0);
    target->_gu1 = min(s0->_gu1, s1->_gu1);
    target->_gv1 = min(s0->_gv1, s1->_gv1);

    // arbitrarily set the origin to upper-left
    target->lu = target->_gu0;
    target->lv = target->_gv0;

    // set the new screen coordinates in local frame
    target->u0 = 0;
    target->v0 = 0;
    target->u1 = target->_gu1 - target->_gu0;
    target->v1 = target->_gv1 - target->_gv0;

    // compute the target extent
    ret = recompute_extent(target);
    if (0 != ret) {
      goto out;
    }
  }

out:
  return ret;
}

/**
 * @brief Clip a horizontal line to the given dislay.
 * Coordinates are given in screen frame.
 * Preserves original order of u0 and u1.
 * Screen must be mnormalized.
 *
 * @param screen
 * @param u0
 * @param v0
 * @param u1
 * @param v1
 * @return int 	0 for success with pixels to draw, positive for success with
 *							no pixels to draw,
 *negative errno on failure.
 */
int screen_clip_pixel(screen_t* screen, ext_t u0, ext_t v0) {
  int ret = 0;
  if (NULL == screen) {
    ret = -EINVAL;
    goto out;
  }
  if ((u0 < screen->u0) || (u0 > screen->u1) || (v0 < screen->v0) ||
      (v0 > screen->v1)) {
    ret = 1;
    goto out;
  }
out:
  return ret;
}

/**
 * @brief Clip a horizontal line to the given dislay.
 * Coordinates are given in screen frame.
 * Preserves original order of u0 and u1.
 * Screen must be mnormalized.
 *
 * @param screen
 * @param u0
 * @param v0
 * @param u1
 * @param v1
 * @return int 	0 for success with pixels to draw, positive for success with
 *							no pixels to draw,
 *negative errno on failure.
 */
int screen_clip_hline(screen_t* screen, ext_t* _u0, ext_t* _v0, ext_t* _u1) {
  int ret = 0;
  if ((NULL == screen) || (NULL == _u0) || (NULL == _v0) || (NULL == _u1)) {
    ret = -EINVAL;
    goto out;
  }
  int reversed = (*_u0 <= *_u1) ? false : true;
  ext_t u0 = min(*_u0, *_u1);
  ext_t v0 = *_v0;
  ext_t u1 = max(*_u0, *_u1);

  // check whether hline is off-screen entirely
  if ((v0 < screen->v0) || (v0 > screen->v1)) {
    ret = 1;
    goto out;
  }
  // limit endpoints for screen
  if (reversed) {
    // original direction was negative
    if (u0 < screen->u0) {
      *_u1 = screen->u0;
    }
    if (u1 > screen->u1) {
      *_u0 = screen->u1;
    }
  } else {
    // original direction was positive
    if (u0 < screen->u0) {
      *_u0 = screen->u0;
    }
    if (u1 > screen->u1) {
      *_u1 = screen->u1;
    }
  }
out:
  return ret;
}

/**
 * @brief Clip a vertical line to the given screen.
 * Coordinates are given in screen frame.
 * Preserves original order of v0 and v1.
 * Screen must be normalized.
 *
 * @param screen
 * @param u0
 * @param v0
 * @param u1
 * @param v1
 * @return int 	0 for success with pixels to draw, positive for success with
 *              no pixels to draw, negative errno on failure.
 */
int screen_clip_vline(screen_t* screen, ext_t* _u0, ext_t* _v0, ext_t* _v1) {
  int ret = 0;
  if ((NULL == screen) || (NULL == _u0) || (NULL == _v0) || (NULL == _v1)) {
    ret = -EINVAL;
    goto out;
  }
  int reversed = (*_v0 <= *_v1) ? false : true;
  ext_t u0 = *_u0;
  ext_t v0 = min(*_v0, *_v1);
  ext_t v1 = max(*_v0, *_v1);

  // check whether hline is off-screen entirely
  if ((u0 < screen->u0) || (u0 > screen->u1)) {
    ret = 1;
    goto out;
  }
  // limit endpoints for screen
  if (reversed) {
    // original direction was negative
    if (v0 < screen->v0) {
      *_v1 = screen->v0;
    }
    if (v1 > screen->v1) {
      *_v0 = screen->v1;
    }
  } else {
    // original direction was positive
    if (v0 < screen->v0) {
      *_v0 = screen->v0;
    }
    if (v1 > screen->v1) {
      *_v1 = screen->v1;
    }
  }
out:
  return ret;
}

/**
 * @brief Clips screen diagonal from interior of screen.
 * Does not change initial point, as it is assumed to be interior to the screen.
 * May reduce the pixel count if an overrun would occur.
 * Screen must be normalized.
 *
 * @param screen
 * @param u
 * @param v
 * @param diru
 * @param dirv
 * @param _count
 * @return int
 */
static int screen_clip_diagonal_from_interior(
    screen_t* screen, ext_t u, ext_t v, ext_t diru, ext_t dirv, uext_t* count) {
  int ret = 0;
  uext_t du, dv, max_pixels;

  if ((NULL == screen) || (NULL == count)) {
    ret = -ENOMEM;
    goto out;
  }

  // the line is starting inside the screen draw until either u or v goes
  // off-screen
  if (diru < 0) {
    du = u - screen->u0;
  } else {
    du = screen->u1 - u;
  }
  if (dirv < 0) {
    dv = v - screen->v0;
  } else {
    dv = screen->v1 - v;
  }
  // coordinates are already on-screen, no need to modify them.
  // just set the count as needed then exit.
  max_pixels = min(du, dv) + 1;
  if (*count > max_pixels) {
    *count = max_pixels;
  }

out:
  return ret;
}

/**
 * @brief Clip a diagonal line to the given dislay.
 * Coordinates are given in screen frame.
 * Screen must be normalized.
 *
 * @param screen
 * @param u0
 * @param v0
 * @param u1
 * @param v1
 * @return int 	0 for success with pixels to draw, positive for success with
 *              no pixels to draw, negative errno on failure.
 */
int screen_clip_diagonal(
    screen_t* screen, ext_t* _u0, ext_t* _v0, ext_t _diru, ext_t _dirv,
    uext_t* _count) {
  int ret = 0;
  if ((NULL == screen) || (NULL == _u0) || (NULL == _v0) || (NULL == _count)) {
    ret = -EINVAL;
    goto out;
  }
  ext_t u = *_u0;
  ext_t v = *_v0;
  ext_t diru = _diru;
  ext_t dirv = _dirv;
  ext_t su0 = screen->u0;
  ext_t su1 = screen->u1;
  ext_t sv0 = screen->v0;
  ext_t sv1 = screen->v1;
  uext_t count = *_count;

  // check for the case that the line is already starting within the screen
  // boundaries: if this is the case then it is simple to compute the remaining
  // length allowed.
  if (((su0 <= u) && (u <= su1)) && ((sv0 <= v) && (v <= sv1))) {
    ret = screen_clip_diagonal_from_interior(screen, u, v, diru, dirv, _count);
    goto out;
  }

  // check for cases where line will stay off-screen
  // this eliminates some possible lines right up to the edges of
  // the screen and works in conjunction with the test below.
  if (((u < su0) && (diru < 0)) || ((u > su1) && (diru > 0)) ||
      ((v < sv0) && (dirv < 0)) || ((v > sv1) && (dirv > 0))) {
    ret = 1;
    goto out;
  }

  // imagine a square rotated 45 degrees so that the diagonal axes are aligned
  // with u and v this square circumscribes the screen when its sides are given
  // by the equation: abs(v) + abs(u) = (width + height) / 2 since we know the
  // screen is normalized the positive values of width and height are:
  uext_t width = su1 - su0 + 1;
  uext_t height = sv1 - sv0 + 1;

  // since pixels and integers do that annoying discrete thing the right side of
  // the above equation actually becomes:
  uext_t distance = (width + height) / 2;

  // when both width and height are even add one - in other cases (where at
  // least one is odd) there is some overlap which takes up this extra distance.
  // (draw it out and you'll see)
  if (((width & 0x01) == 0) && ((height & 0x01) == 0)) {
    distance += 1;
  }

  // the next computations are peformed relative to the center of the screen,
  // (cu, cv) when either the width or height (or both) are odd the center is
  // chosen to include some overlap - this prevents any starting locations from
  // being missed. (this is done by relying on integer division to truncate the
  // remainder toward zero)
  ext_t cu = (su0 + su1) / 2;
  ext_t cv = (sv0 + sv1) / 2;

  // transform drawing coordinates to be relative to the center of the screen.
  ext_t ru = u - cu;
  ext_t rv = v - cv;

  // now change the signs so that this all happens in the first quadrant
  bool u_flipped = false;
  bool v_flipped = false;
  if (ru < 0) {
    u_flipped = true;
    ru = -ru;
    diru = -diru;
  }
  if (rv < 0) {
    v_flipped = true;
    rv = -rv;
    dirv = -dirv;
  }

  // now: check for lines which are never going to intersect...
  // if the starting coordinate is on or outside the circumscribing rectangle
  // and either of the directions is positive then there will never be an
  // intersection.
  if ((ru + rv) > (distance - 1)) {
    if ((diru > 0) || (dirv > 0)) {
      ret = 1;
      goto out;
    }
  }

  // any remaining lines are off-screen and pointing toward the valid area.
  // all that is left is to determine:
  // - whether they make it to the valid area
  // - how far through the valid area they make it
  // (and then transform back to original coordinates)

  // the distance to the screen can be computed for the u and v axes
  // independently and the larger of the two will be the valid distance.
  ext_t du = ru - (width / 2);
  ext_t dv = rv - (height / 2);
  uext_t bump = max(du, dv);

  // adjust the relative coordinates toward the screen
  if (count <= bump) {
    // if the original count is smaller than bump the line does not reach the
    // screen
    ret = 1;
    goto out;
  }
  ru -= bump;
  rv -= bump;
  count -= bump;

  // transform the coordinates back into real space
  if (u_flipped) {
    ru = -ru;
    diru = -diru;
  }
  if (v_flipped) {
    rv = -rv;
    dirv = -dirv;
  }
  u = ru + cu;
  v = rv + cv;

  // finally the first algorithm - for determining the length to the end
  // of the screen from within, may be reapplied.
  // checking boundaries again should not be necessary, but itwill help
  // catch errors early in testing.
  if (((su0 <= u) && (u <= su1)) && ((sv0 <= v) && (v <= sv1))) {
    *_u0 = u;
    *_v0 = v;
    *_count = count;
    ret = screen_clip_diagonal_from_interior(screen, u, v, diru, dirv, _count);
    goto out;
  } else {
    ret = -EINVAL;
    goto out;
  }

out:
  return ret;
}

/**
 * @brief Clip a line along the first axis so that it fits within [umin, umax].
 *
 * @param screen
 * @param _u0
 * @param _v0
 * @param _u1
 * @param _v1
 * @return int 	0 for success with pixels to draw, positive for success with
 *							no pixels to draw,
 *negative errno on failure.
 */
static int screen_clip_line_partial(
    ext_t* u0, ext_t* v0, ext_t* u1, ext_t* v1, ext_t umin, ext_t umax) {
  int ret = 0;
  if ((NULL == u0) || (NULL == v0) || (NULL == u1) || (NULL == v1)) {
    ret = -ENOMEM;
    goto out;
  }
  double slope;

  // check whether the line begins outside the window
  if (*u0 < umin) {
    if (*u1 < umin) {
      // both start and end dimensions are off-screen - no pixels to draw
      ret = 1;
      goto out;
    }
    slope = (*v1 - *v0) / (double)(*u1 - *u0);
    *v0 -= (ext_t)(slope * (*u0 - umin));
    *u0 = umin;

    // we already know the slope, it is easy to check the other point as well
    // now
    if (*u1 > umax) {
      *v1 += slope * (umax - *u1);
      *u1 = umax;
    }
    goto out;
  }
  if (*u0 > umax) {
    if (*u1 > umax) {
      // both start and end dimensions are off-screen - no pixels to draw
      ret = 1;
      goto out;
    }
    slope = (*v1 - *v0) / (double)(*u1 - *u0);
    *v0 += (ext_t)(slope * (umax - *u0));
    *u0 = umax;

    // we already know the slope, it is easy to check the other point as well
    // now
    if (*u1 < umin) {
      *v1 -= (ext_t)(slope * (*u1 - umin));
      *u1 = umin;
    }
    goto out;
  }
  // if this point is reached the starting point is known to be on-screen
  if (*u1 > umax) {
    // ending point is beyond umax
    slope = (*v1 - *v0) / (double)(*u1 - *u0);
    *v1 += (ext_t)(slope * (umax - *u1));
    *u1 = umax;
    goto out;
  }
  if (*u1 < umin) {
    // ending point is below umin
    slope = (*v1 - *v0) / (double)(*u1 - *u0);
    *v1 -= (ext_t)(slope * (*u1 - umin));
    *u1 = umin;
    goto out;
  }
  // both starting and ending points were within the window in the primary axis

out:
  return ret;
}

/**
 * @brief Clip a line to the given dislay.
 * Coordinates are given in screen frame.
 * Screen must be normalized.
 *
 * @param screen
 * @param u0
 * @param v0
 * @param u1
 * @param v1
 * @return int 	0 for success with pixels to draw, positive for success with
 *							no pixels to draw,
 *negative errno on failure.
 */
int screen_clip_line(
    screen_t* screen, ext_t* u0, ext_t* v0, ext_t* u1, ext_t* v1) {
  int ret = 0;
  if (NULL == screen) {
    ret = -ENOMEM;
    goto out;
  }
  ret = screen_clip_line_partial(
      u0, v0, u1, v1, screen->u0, screen->u1);  // clip u axis
  if (0 != ret) {
    goto out;
  }
  ret = screen_clip_line_partial(
      v0, u0, v1, u1, screen->v0, screen->v1);  // clip v axis
  if (0 != ret) {
    goto out;
  }

out:
  return ret;
}
