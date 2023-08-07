#include "sicgl/debug.h"
#include "sicgl/iterator.h"

void iter_foreach(iter_t iter, void (*callback)(void*), void* arg) {
  for (iter.first(iter.args); !iter.done(iter.args); iter.next(iter.args)) {
    callback(arg);
  }
}
