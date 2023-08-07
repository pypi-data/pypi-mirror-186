import numpy as np

import meshset

from .helpers import is_near_equal


def test_tube():
    points, cells = meshset.tube(n=10)
    assert len(points) == 20
    assert is_near_equal(np.sum(points, axis=0), [0.0, 0.0, 0.0])
    assert len(cells) == 20
