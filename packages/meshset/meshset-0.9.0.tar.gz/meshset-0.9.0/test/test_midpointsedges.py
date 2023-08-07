import numpy as np

import meshset


def test_midpoints_edges_tri():
    points, cells = meshset.rectangle_tri(
        np.linspace(0.0, 1.0, 2), np.linspace(0.0, 1.0, 2)
    )

    assert len(points) == 4
    assert cells.shape == (2, 3)

    points_new, cells_new = meshset.insert_midpoints_edges(
        points, cells, cell_type="triangle"
    )

    assert len(points_new) == 9
    assert cells_new.shape == (2, 6)


def test_midpoints_edges_tetra():
    ls = np.linspace(0.0, 1.0, 2)
    points, cells = meshset.cube_tetra(ls, ls, ls)

    assert len(points) == 8
    assert cells.shape == (5, 4)

    points_new, cells_new = meshset.insert_midpoints_edges(
        points, cells, cell_type="tetra"
    )

    assert len(points_new) == 26
    assert cells_new.shape == (5, 10)


def test_midpoints_edges_quad():
    ls = np.linspace(0.0, 1.0, 3)
    points, cells = meshset.rectangle_quad(ls, ls)

    assert len(points) == 9
    assert cells.shape == (4, 4)

    points_new, cells_new = meshset.insert_midpoints_edges(
        points, cells, cell_type="quad"
    )

    assert len(points_new) == 21
    assert cells_new.shape == (4, 8)


def test_midpoints_edges_hexa():
    ls = np.linspace(0.0, 1.0, 3)
    points, cells = meshset.cube_hexa(ls, ls, ls)

    assert len(points) == 27
    assert cells.shape == (8, 8)

    points_new, cells_new = meshset.insert_midpoints_edges(
        points, cells, cell_type="hexahedron"
    )

    assert len(points_new) == 81
    assert cells_new.shape == (8, 20)


if __name__ == "__main__":
    test_midpoints_edges_tri()
    test_midpoints_edges_tetra()
    test_midpoints_edges_quad()
    test_midpoints_edges_hexa()
