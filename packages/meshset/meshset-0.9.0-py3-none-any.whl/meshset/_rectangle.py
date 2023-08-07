from __future__ import annotations

import numpy as np

# backwards compatibility
def rectangle(
    x0: float,
    x1: float,
    y0: float,
    y1: float,
    nx: int,
    ny: int,
):
    x_range = np.linspace(x0, x1, nx + 1)
    y_range = np.linspace(y0, y1, ny + 1)
    return rectangle_tri(x_range, y_range)


def rectangle_quad(x_range: np.typing.ArrayLike, y_range: np.typing.ArrayLike):
    x_range = np.asarray(x_range)
    y_range = np.asarray(y_range)

    nx = len(x_range)
    ny = len(y_range)

    points = np.array(np.meshgrid(x_range, y_range)).reshape(2, -1).T
    a = np.arange(nx * ny).reshape(ny, nx).T

    cells = np.array([a[:-1, :-1], a[1:, :-1], a[1:, 1:], a[:-1, 1:]]).reshape(4, -1).T
    return points, cells


def rectangle_tri(x_range: np.typing.ArrayLike, y_range: np.typing.ArrayLike, variant: str = "zigzag"):
    x_range = np.asarray(x_range)
    y_range = np.asarray(y_range)

    nx = len(x_range)
    ny = len(y_range)

    # Create the vertices.
    points = np.array(np.meshgrid(x_range, y_range)).reshape(2, -1).T

    a = np.arange(nx * ny).reshape(ny, nx).T

    # indices of corners
    #
    # c[3]   c[2]
    #    _____
    #    |   |
    #    |___|
    #
    # c[0]   c[1]
    #
    c = [
        a[:-1, :-1],
        a[1:, :-1],
        a[1:, 1:],
        a[:-1, 1:],
    ]

    if variant == "up":
        cells = [
            [c[0], c[1], c[2]],
            [c[0], c[2], c[3]],
        ]
    elif variant == "down":
        cells = [
            [c[0], c[1], c[3]],
            [c[1], c[2], c[3]],
        ]
    elif variant == "zigzag":
        # https://stackoverflow.com/a/68550456/353337
        idx = np.ones((nx - 1, ny - 1), dtype=bool)
        idx[1::2, ::2] = False
        idx[::2, 1::2] = False
        cells = [
            # up
            [c[0][idx], c[1][idx], c[2][idx]],
            [c[0][idx], c[2][idx], c[3][idx]],
            # down
            [c[0][~idx], c[1][~idx], c[3][~idx]],
            [c[1][~idx], c[2][~idx], c[3][~idx]],
        ]
    else:
        assert variant == "center"
        i = np.arange(nx - 1)
        j = np.arange(ny - 1)
        i, j = np.meshgrid(i, j, indexing="ij")

        idx = np.ones(((nx - 1), (ny - 1)), dtype=bool)
        idx[: (nx - 1) // 2, : (ny - 1) // 2] = False
        idx[(nx - 1) // 2 :, (ny - 1) // 2 :] = False

        cells = [
            # up
            [c[0][idx], c[1][idx], c[2][idx]],
            [c[0][idx], c[2][idx], c[3][idx]],
            # down
            [c[0][~idx], c[1][~idx], c[3][~idx]],
            [c[1][~idx], c[2][~idx], c[3][~idx]],
        ]

    cells = np.column_stack([np.array(c).reshape(3, -1) for c in cells]).T

    return points, cells
