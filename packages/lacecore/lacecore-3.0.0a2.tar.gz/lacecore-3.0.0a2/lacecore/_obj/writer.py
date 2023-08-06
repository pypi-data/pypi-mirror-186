# Adapted from
# https://github.com/lace/lace/blob/d3c191dffaeedc14aafa4af031d74743de9e632d/lace/serialization/obj/__init__.py
import numpy as np
from .._group_map import GroupMap


def write(fp, mesh):
    """
    Save a mesh's faces, vertices, and face groups to a Wavefront OBJ file.

    Args:
        fp: An open file pointer.
        mesh (lacecore.Mesh): The mesh to write.
    """
    for vertex in mesh.v:
        fp.write("v {} {} {}\n".format(*vertex))

    face_groups = mesh.face_groups or GroupMap.from_dict({}, len(mesh.f))
    last_group_mask = np.zeros(len(face_groups.keys()), dtype=bool)
    for i, face in enumerate(mesh.f):
        this_group_mask = face_groups.mask_for_element(i)
        if np.any(last_group_mask != this_group_mask):
            fp.write(
                "g {}\n".format(
                    " ".join(face_groups.group_names_for_element_mask(this_group_mask))
                )
            )
            last_group_mask = this_group_mask

        # Add one, because OBJ indexing is one-based.
        if mesh.is_quad:
            fp.write("f {} {} {} {}\n".format(*face + 1))
        else:
            fp.write("f {} {} {}\n".format(*face + 1))
