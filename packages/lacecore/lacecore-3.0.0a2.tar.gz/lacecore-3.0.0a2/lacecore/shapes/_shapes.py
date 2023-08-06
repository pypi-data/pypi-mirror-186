from polliwog import shapes
from .._mesh import Mesh


__all__ = [
    "rectangular_prism",
    "cube",
    "triangular_prism",
]


def _mesh_from_shape_fn(shape_factory_fn, *args, **kwargs):
    vertices, faces = shape_factory_fn(
        *args, ret_unique_vertices_and_faces=True, **kwargs
    )
    return Mesh(v=vertices, f=faces)


def rectangular_prism(origin, size):
    """
    Tesselate an axis-aligned rectangular prism. One vertex is `origin`. The
    diametrically opposite vertex is `origin + size`.

    Args:
        origin (np.ndarray): A 3D point vector containing the point on the
            prism with the minimum x, y, and z coords.
        size (np.ndarray): A 3D vector specifying the prism's length, width,
            and height, which should be positive.

    Returns:
        lacecore.Mesh: A `Mesh` instance containing the rectangular prism.
    """
    return _mesh_from_shape_fn(shapes.rectangular_prism, origin=origin, size=size)


def cube(origin, size):
    """
    Tesselate an axis-aligned cube. One vertex is `origin`. The diametrically
    opposite vertex is `size` units along `+x`, `+y`, and `+z`.

    Args:
        origin (np.ndarray): A 3D point vector containing the point on the
            prism with the minimum x, y, and z coords.
        size (float): The length, width, and height of the cube, which should
            be positive.

    Returns:
        lacecore.Mesh: A `Mesh` instance containing the cube.
    """
    return _mesh_from_shape_fn(shapes.cube, origin=origin, size=size)


def triangular_prism(p1, p2, p3, height):
    """
    Tesselate a triangular prism whose base is the triangle `p1`, `p2`, `p3`.
    If the vertices are oriented in a counterclockwise direction, the prism
    extends from behind them.

    Args:
        p1 (np.ndarray): A 3D point on the base of the prism.
        p2 (np.ndarray): A 3D point on the base of the prism.
        p3 (np.ndarray): A 3D point on the base of the prism.
        height (float): The height of the prism, which should be positive.

    Returns:
        lacecore.Mesh: A `Mesh` instance containing the triangular prism.
    """
    return _mesh_from_shape_fn(
        shapes.triangular_prism, p1=p1, p2=p2, p3=p3, height=height
    )
