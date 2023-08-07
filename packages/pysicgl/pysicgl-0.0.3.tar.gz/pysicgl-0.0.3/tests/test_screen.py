import pytest
import pysicgl


def test_init_extent():
    extent = (20, 42)
    s = pysicgl.Screen(extent)

    assert s.width == 20
    assert s.height == 42
    assert s.extent == extent


def test_init_normalization():
    from testutils import vec_add

    extent = (20, 20)
    location = (1, 1)

    expected_corners = ((0, 0), (extent[0] - 1, extent[1] - 1))
    expected_global_corners = tuple(
        vec_add(corner, location) for corner in expected_corners
    )

    s = pysicgl.Screen(extent, location)

    for (expected, corner) in zip(expected_corners, s.corners):
        assert corner == expected

    for (expected, corner) in zip(expected_global_corners, s.global_corners):
        assert corner == expected
