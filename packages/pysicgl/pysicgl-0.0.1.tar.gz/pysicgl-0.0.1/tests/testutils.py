# vector utilities
# vectors are fixed-length iterables with scalar numeric elements

import math


def vec_add(*vectors):
    return tuple(sum(elements) for elements in zip(*vectors))


def vec_magnitude(vector):
    return math.sqrt(sum(math.pow(element, 2) for element in vector))


def vec_normalize(vector):
    magnitude = vec_magnitude(vector)
    return tuple(element / magnitude for element in vector)
