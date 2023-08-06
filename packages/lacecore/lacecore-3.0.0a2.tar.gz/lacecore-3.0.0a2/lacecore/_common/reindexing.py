import numpy as np
from vg.compat import v2 as vg


def indices_of_original_elements_after_applying_mask(mask):
    """
    Given a mask that represents which of the original elements should be kept,
    produce an array containing the new indices of the original elements. Returns
    -1 as the index of the removed elements.
    """
    result = np.repeat(-1, len(mask))
    result[mask] = np.arange(np.count_nonzero(mask))
    return result


def create_submesh(
    mesh, vertex_mask, face_mask, ret_indices_of_original_faces_and_vertices=False
):
    """
    Apply the requested mask to the vertices and faces to create a submesh,
    discarding the face groups.
    """
    from .._mesh import Mesh

    new_v = mesh.v[vertex_mask]
    indices_of_original_vertices = indices_of_original_elements_after_applying_mask(
        vertex_mask
    )
    new_f = indices_of_original_vertices[mesh.f[face_mask]]
    submesh = Mesh(v=new_v, f=new_f)

    if ret_indices_of_original_faces_and_vertices:
        indices_of_original_faces = indices_of_original_elements_after_applying_mask(
            face_mask
        )
        return submesh, indices_of_original_faces, indices_of_original_vertices
    else:
        return submesh


def reindex_vertices(mesh, ordering):
    """
    Reorder the vertices of the given mesh, returning a new mesh.

    Args:
        mesh (lacecore.Mesh): The mesh on which to operate.
        ordering (np.arraylike): An array specifying the order in which
            the original vertices should be arranged.

    Returns:
        lacecore.Mesh: The reindexed mesh.
    """
    from .._mesh import Mesh

    vg.shape.check(locals(), "ordering", (mesh.num_v,))
    unique_values, inverse = np.unique(ordering, return_index=True)
    if not np.array_equal(unique_values, np.arange(mesh.num_v)):
        raise ValueError(
            "Expected new vertex indices to be unique, and range from 0 to {}".format(
                mesh.num_v - 1
            )
        )

    return Mesh(v=mesh.v[ordering], f=inverse[mesh.f], face_groups=mesh.face_groups)


def reindex_faces(mesh, ordering):
    """
    Reorder the faces of the given mesh, returning a new mesh.

    Args:
        mesh (lacecore.Mesh): The mesh on which to operate.
        ordering (np.arraylike): An array specifying the order in which
            the original faces should be arranged.

    Returns:
        lacecore.Mesh: The reindexed mesh.
    """
    from .._mesh import Mesh

    vg.shape.check(locals(), "ordering", (mesh.num_f,))
    unique_values = np.unique(ordering)
    if not np.array_equal(unique_values, np.arange(mesh.num_f)):
        raise ValueError(
            "Expected new face indices to be unique, and range from 0 to {}".format(
                mesh.num_f - 1
            )
        )

    return Mesh(
        v=mesh.v,
        f=mesh.f[ordering],
        face_groups=None
        if mesh.face_groups is None
        else mesh.face_groups.reindexed(ordering),
    )
