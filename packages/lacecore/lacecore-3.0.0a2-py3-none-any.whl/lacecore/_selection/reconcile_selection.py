import numpy as np
from vg.compat import v2 as vg
from .._common.validation import check_arity, check_indices


def reconcile_selection(faces, face_mask, vertex_mask, prune_orphan_vertices):
    """
    Reconcile the given vertex and face masks. When vertices are removed,
    their faces must also be removed. When faces are removed, the vertices
    can be removed or kept, depending on the `prune_orphan_vertices` option.

    Args:
        faces (np.ndarray): A `kx3` or `kx4` array of the vertices of each
            face.
        face_mask (np.ndarray): A boolean face mask.
        vertex_mask (np.ndarray): A boolean vertex mask.
        prune_orphan_vertices (bool): When `True`, remove vertices which
            their last referencing face is removed.

    Returns:
        tuple: The reconciled vertex and face masks.
    """
    num_faces, _ = vg.shape.check(locals(), "faces", (-1, -1))
    check_arity(faces)
    vg.shape.check(locals(), "face_mask", (num_faces,))
    num_vertices = vg.shape.check(locals(), "vertex_mask", (-1,))
    if face_mask.dtype != bool or vertex_mask.dtype != bool:
        raise ValueError("Expected face_mask and vertex_mask to be boolean arrays")
    check_indices(faces, num_vertices, "faces")

    # Invalidate faces containing any vertex which is being removed.
    reconciled_face_mask = np.zeros_like(face_mask, dtype=bool)
    reconciled_face_mask[face_mask] = np.all(vertex_mask[faces[face_mask]], axis=1)

    # Optionally, invalidate vertices for faces which are being removed.
    if prune_orphan_vertices:
        # Orphaned verts are those belonging to faces which are being
        # removed, and not faces which are being kept.
        orphaned_vertices = np.setdiff1d(
            faces[~reconciled_face_mask], faces[reconciled_face_mask]
        )
        reconciled_vertex_mask = np.copy(vertex_mask)
        reconciled_vertex_mask[orphaned_vertices] = False
    else:
        reconciled_vertex_mask = vertex_mask

    return reconciled_face_mask, reconciled_vertex_mask
