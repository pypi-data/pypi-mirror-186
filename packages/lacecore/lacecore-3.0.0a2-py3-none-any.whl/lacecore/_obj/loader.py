from collections import OrderedDict
import numpy as np
from .._group_map import GroupMap
from .._mesh import FACE_DTYPE, Mesh

try:
    from tinyobjloader import ObjReader, ObjReaderConfig
except Exception:  # pragma: no cover
    ObjReader = None
    ObjReaderConfig = None


class LoadException(Exception):
    pass


class ArityException(Exception):
    pass


def unstack(stacked_result, slice_lengths, safe=True):
    """
    Iterate over slices within a stacked result.
    """
    if safe:
        k = np.sum(slice_lengths)
        if stacked_result.shape[0] != k:  # pragma: no cover
            raise ValueError("Expected stacked_result to have lenth {}".format(k))

    # This code is equivalent to this NumPy call. Strangely enough, our
    # generator-based implementation seems to be faster.
    # return np.array_split(stacked_result, np.cumsum(slice_lengths)[:-1], axis=0)

    last_index = -1
    for slice_length in slice_lengths:
        new_last_index = last_index + int(slice_length)
        yield stacked_result[last_index + 1 : new_last_index + 1]
        last_index = new_last_index


def create_reader_and_config():
    if ObjReader is None:  # pragma: no cover
        raise ImportError(
            """
            tinyobjloader library has not been installed.
            You will not be able to load OBJ files.
            To fix, run `pip install lacecore[obj]`.
            """
        )
    reader = ObjReader()
    config = ObjReaderConfig()
    # There is some complex code in tinyobjloader which occasionally switches
    # the axes of triangulation based on the vertex positions. This is
    # undesirable in lacecore as it scrambles correspondence.
    config.triangulate = False
    return reader, config


def _get_arity(shapes):
    if len(shapes) == 0:
        return 3

    all_vertices_per_face = np.concatenate(
        [shape.mesh.numpy_num_face_vertices() for shape in shapes]
    )
    first_arity = all_vertices_per_face[0]
    if np.any(all_vertices_per_face < 3) or np.any(all_vertices_per_face > 4):
        raise ArityException(
            "OBJ Loader does not support arities greater than 4 or less than 3"
        )
    is_mixed_arity = ~np.all(all_vertices_per_face == first_arity)
    return tuple(all_vertices_per_face) if is_mixed_arity else all_vertices_per_face[0]


def _finalize(reader, triangulate):
    shapes = reader.GetShapes()

    arity = _get_arity(shapes)
    is_mixed_arity = isinstance(arity, tuple)
    first_arity = arity[0] if is_mixed_arity else arity

    all_faces = np.zeros((0, 3 if triangulate else first_arity), dtype=FACE_DTYPE)
    segm = OrderedDict()

    for shape in shapes:
        these_face_indices = shape.mesh.numpy_indices().reshape(-1, 3)[:, 0]
        if is_mixed_arity and not triangulate:
            raise ArityException(
                "OBJ Loader does not support mixed arities with triangulate=False"
            )
        elif is_mixed_arity:
            these_vertices_per_face = shape.mesh.numpy_num_face_vertices()
            these_faces = np.zeros((0, 3), dtype=FACE_DTYPE)
            for this_face in unstack(these_face_indices, these_vertices_per_face):
                if len(this_face) == 3:
                    these_faces = np.concatenate([these_faces, this_face.reshape(1, 3)])
                else:
                    these_faces = np.concatenate(
                        [
                            these_faces,
                            this_face[[0, 1, 2]].reshape(1, 3),
                            this_face[[0, 2, 3]].reshape(1, 3),
                        ]
                    )
        else:
            these_faces = these_face_indices.reshape(-1, first_arity)
            if triangulate and first_arity == 4:
                # Triangulate ABCD as ABC + ACD.
                these_faces = these_faces[:, [[0, 1, 2], [0, 2, 3]]].reshape(-1, 3)

        start = len(all_faces)
        end = start + len(these_faces)
        these_face_indices = list(range(start, end))

        all_faces = np.concatenate([all_faces, these_faces])

        for name in shape.name.split():
            if name not in segm:
                segm[name] = []
            segm[name] = segm[name] + these_face_indices

    group_map = GroupMap.from_dict(segm, len(all_faces))

    return Mesh(
        v=reader.GetAttrib().numpy_vertices().reshape(-1, 3),
        f=all_faces,
        face_groups=group_map,
    )


def load(mesh_path, triangulate=False):
    """
    Load a `Mesh` from a path to an OBJ file.

    Args:
        mesh_path (str): A path to an OBJ file
        triangulate (bool): A flag that indicates whether to triangulate the mesh on load.

    Returns:
        lacecore.Mesh: A `Mesh` instance
    """
    reader, config = create_reader_and_config()
    success = reader.ParseFromFile(mesh_path, config)
    if not success:
        raise LoadException(reader.Warning() or reader.Error())
    return _finalize(reader=reader, triangulate=triangulate)


def loads(mesh_string, triangulate=False):
    """
    Load `Mesh` contents from a string.

    Args:
        mesh_string (str): The contents of an OBJ file.
        triangulate (bool): A flag that indicates whether to triangulate the mesh on load.

    Returns:
        lacecore.Mesh: A `Mesh` instance
    """
    reader, config = create_reader_and_config()
    success = reader.ParseFromString(mesh_string, "", config)
    if not success:
        raise LoadException(reader.Warning() or reader.Error())
    return _finalize(reader=reader, triangulate=triangulate)
