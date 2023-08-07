import meshset

from .helpers import signed_simplex_volumes


def test_disk():
    points, cells = meshset.disk(9, 8)
    meshset.save2d("4gon_disk.svg", points, cells)
    assert len(points) == 325
    assert len(cells) == 576
    assert (signed_simplex_volumes(points, cells) > 0.0).all()


def test_disk_quad():
    points, cells = meshset.disk_quad(10)
    # meshset.save2d("disk-quad.svg", points, cells)
    assert len(points) == 121
    assert len(cells) == 100
