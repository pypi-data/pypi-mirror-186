import numpy as np
from polliwog import Plane
from vg.compat import v2 as vg
from .reconcile_selection import reconcile_selection
from .._common.reindexing import create_submesh
from .._common.validation import check_indices


class Selection:
    """
    Encapsulate a chained submesh selection operation.

    Invoke `.end()` to apply the selection operation and create a submesh. By
    default, orphaned vertices are pruned. However you can keep them by
    invoking `.end(prune_orphan_vertices=True)`.

    Include `.union()` in the chain to combine more than one set of selection
    criteria into a single submesh.

    Args:
        target (lacecore.Mesh): The mesh on which to operate.
        union_with (lacecore.Selection): The operation with which the new
            instance should combine itself. Normally this is reserved for
            internal use.
    """

    def __init__(
        self,
        target,
        union_with=[],
    ):
        self._target = target
        self._union_with = union_with
        self._vertex_mask = np.ones(target.num_v, dtype=bool)
        self._face_mask = np.ones(target.num_f, dtype=bool)

    def _keep_faces(self, mask):
        self._face_mask = np.logical_and(self._face_mask, mask)

    def _keep_vertices(self, mask):
        self._vertex_mask = np.logical_and(self._vertex_mask, mask)

    def vertices_at_or_above(self, dim, point):
        """
        Select vertices which, when projected to the given axis, are either
        coincident with the projection of the given point, or lie further
        along the axis.

        Args:
            dim (int): The axis of interest: 0 for `x`, 1 for `y`, 2 for `z`.
            point (np.arraylike): The point of interest.

        Returns:
            self
        """
        if dim not in [0, 1, 2]:
            raise ValueError("Expected dim to be 0, 1, or 2")
        vg.shape.check(locals(), "point", (3,))
        self._keep_vertices(self._target.v[:, dim] >= point[dim])
        return self

    def vertices_above(self, dim, point):
        """
        Select vertices which, when projected to the given axis, lie further
        along that axis than the projection of the given point.

        Args:
            dim (int): The axis of interest: 0 for `x`, 1 for `y`, 2 for `z`.
            point (np.arraylike): The point of interest.

        Returns:
            self
        """
        if dim not in [0, 1, 2]:
            raise ValueError("Expected dim to be 0, 1, or 2")
        vg.shape.check(locals(), "point", (3,))
        self._keep_vertices(self._target.v[:, dim] > point[dim])
        return self

    def vertices_at_or_below(self, dim, point):
        """
        Select vertices which, when projected to the given axis, are either
        coincident with the projection of the given point, or lie before it.

        Args:
            dim (int): The axis of interest: 0 for `x`, 1 for `y`, 2 for `z`.
            point (np.arraylike): The point of interest.

        Returns:
            self
        """
        if dim not in [0, 1, 2]:
            raise ValueError("Expected dim to be 0, 1, or 2")
        vg.shape.check(locals(), "point", (3,))
        self._keep_vertices(self._target.v[:, dim] <= point[dim])
        return self

    def vertices_below(self, dim, point):
        """
        Select vertices which, when projected to the given axis, lie before
        the projection of the given point.

        Args:
            dim (int): The axis of interest: 0 for `x`, 1 for `y`, 2 for `z`.
            point (np.arraylike): The point of interest.

        Returns:
            self
        """
        if dim not in [0, 1, 2]:
            raise ValueError("Expected dim to be 0, 1, or 2")
        vg.shape.check(locals(), "point", (3,))
        self._keep_vertices(self._target.v[:, dim] < point[dim])
        return self

    def vertices_on_or_in_front_of_plane(self, plane):
        """
        Select the vertices which are either on or in front of the given
        plane.

        Args:
            plane (polliwog.Plane): The plane of interest.

        Returns:
            self

        See also:
            https://polliwog.readthedocs.io/en/latest/#polliwog.Plane
        """
        if not isinstance(plane, Plane):
            raise ValueError("Expected an instance of polliwog.Plane")
        self._keep_vertices(plane.sign(self._target.v) != -1)
        return self

    def vertices_in_front_of_plane(self, plane):
        """
        Select the vertices which are in front of the given plane.

        Args:
            plane (polliwog.Plane): The plane of interest.

        Returns:
            self

        See also:
            https://polliwog.readthedocs.io/en/latest/#polliwog.Plane
        """
        if not isinstance(plane, Plane):
            raise ValueError("Expected an instance of polliwog.Plane")
        self._keep_vertices(plane.sign(self._target.v) == 1)
        return self

    def vertices_on_or_behind_plane(self, plane):
        """
        Select the vertices which are either on or behind the given plane.

        Args:
            plane (polliwog.Plane): The plane of interest.

        Returns:
            self

        See also:
            https://polliwog.readthedocs.io/en/latest/#polliwog.Plane
        """
        if not isinstance(plane, Plane):
            raise ValueError("Expected an instance of polliwog.Plane")
        self._keep_vertices(plane.sign(self._target.v) != 1)
        return self

    def vertices_behind_plane(self, plane):
        """
        Select the vertices which are behind the given plane.

        Args:
            plane (polliwog.Plane): The plane of interest.

        Returns:
            self

        See also:
            https://polliwog.readthedocs.io/en/latest/#polliwog.Plane
        """
        if not isinstance(plane, Plane):
            raise ValueError("Expected an instance of polliwog.Plane")
        self._keep_vertices(plane.sign(self._target.v) == -1)
        return self

    @staticmethod
    def _mask_like(value, num_elements):
        value = np.asarray(value)
        if value.dtype == bool:
            vg.shape.check(locals(), "value", (num_elements,))
            return value
        else:
            check_indices(value, num_elements, "mask")
            mask = np.zeros(num_elements, dtype=bool)
            mask[value] = True
            return mask

    def pick_vertices(self, indices_or_boolean_mask):
        """
        Select only the given vertices.

        Args:
            indices_or_boolean_mask (np.arraylike): Either a list of vertex
                indices, or a boolean mask the same length as the vertex array.

        Returns:
            self
        """
        self._keep_vertices(
            self._mask_like(indices_or_boolean_mask, len(self._vertex_mask))
        )
        return self

    def pick_faces(self, indices_or_boolean_mask):
        """
        Select only the given faces.

        Args:
            indices_or_boolean_mask (np.arraylike): Either a list of face
                indices, or a boolean mask the same length as the face array.

        Returns:
            self
        """
        self._keep_faces(self._mask_like(indices_or_boolean_mask, len(self._face_mask)))
        return self

    def pick_face_groups(self, *group_names):
        """
        Select faces which belong to the given face groups.

        Args:
            group_names (list): The face groups to keep.

        Returns:
            self
        """
        if self._target.face_groups is None:
            raise ValueError("Mesh has no face groups")
        self._keep_faces(self._target.face_groups.union(*group_names))
        return self

    def pick_vertices_of_face_groups(self, *group_names):
        """
        Select vertices which belong to any of the given face groups.

        Args:
            group_names (list): The face groups to keep.

        Returns:
            self
        """
        if self._target.face_groups is None:
            raise ValueError("Mesh has no face groups")
        face_indices = self._target.face_groups.union(*group_names)
        vertex_indices = self._target.f[face_indices].flatten()
        self._keep_vertices(self._mask_like(vertex_indices, len(self._vertex_mask)))
        return self

    def union(self):
        """
        Chain on a new selection object. This works like a boolean "or" to
        combine two sets of submesh operations.

        Args:
            indices_or_boolean_mask (np.arraylike): Either a list of face
                indices, or a boolean mask the same length as the face array.

        Returns:
            lacecore.Selection: The new selection operation, which will
                combine itself with `self`.

        Example:
            >>> upper_half_plus_right_half = (
                mesh.select()
                .vertices_above(centroid, dim=0)
                .union()
                .vertices_above(centroid, dim=1)
                .end()
            )

        """
        return self.__class__(target=self._target, union_with=self._union_with + [self])

    def _reconciled_selection(self, prune_orphan_vertices):
        return reconcile_selection(
            faces=self._target.f,
            face_mask=self._face_mask,
            vertex_mask=self._vertex_mask,
            prune_orphan_vertices=prune_orphan_vertices,
        )

    def generate_masks(self, prune_orphan_vertices=True):
        """
        Apply the selection to generate vertex and face masks.

        Args:
            prune_orphan_vertices (bool): When `True`, remove vertices which
                are referenced only by faces which are being removed.

        Returns:
            tuple: `(face_mask, vertex_mask)`. The index arrays contain the new
                indices of the original vertices, and `-1` for each removed face
                and vertex.
        """
        # The approach here is designed to keep faces which have verts in two
        # halves of a union, and to avoid keeping the entire mesh when faces
        # are selected in one half of a union and verts are selected in the
        # other.

        # First, form the union of reconciled vertices.
        _, initial_vertex_mask_of_union = self._reconciled_selection(
            prune_orphan_vertices=prune_orphan_vertices
        )
        for other in self._union_with:
            _, this_vertex_mask = other._reconciled_selection(
                prune_orphan_vertices=prune_orphan_vertices
            )
            initial_vertex_mask_of_union = np.logical_or(
                initial_vertex_mask_of_union, this_vertex_mask
            )

        # Second, union the faces.
        initial_face_mask_of_union = self._face_mask
        for other in self._union_with:
            initial_face_mask_of_union = np.logical_or(
                initial_face_mask_of_union, other._face_mask
            )

        # Finally, reconcile the union of reconciled vertices with the union of
        # faces.
        return reconcile_selection(
            faces=self._target.f,
            face_mask=initial_face_mask_of_union,
            vertex_mask=initial_vertex_mask_of_union,
            prune_orphan_vertices=prune_orphan_vertices,
        )

    def end(
        self,
        prune_orphan_vertices=True,
        ret_indices_of_original_faces_and_vertices=False,
    ):
        """
        Apply the selection to construct a submesh.

        Args:
            prune_orphan_vertices (bool): When `True`, remove vertices which
                are referenced only by faces which are being removed.
            ret_indices_of_original_faces_and_vertices: When `True`, also
                return the indices of the original faces and vertices.

        Returns:
            object: Either the submesh as an instance of `lacecore.Mesh`, or a tuple
                `(submesh, indices_of_original_faces, indices_of_original_vertices)`.
                The index arrays contain the new indices of the original vertices,
                and `-1` for each removed face and vertex.
        """

        face_mask, vertex_mask = self.generate_masks(
            prune_orphan_vertices=prune_orphan_vertices
        )
        return create_submesh(
            mesh=self._target,
            vertex_mask=vertex_mask,
            face_mask=face_mask,
            ret_indices_of_original_faces_and_vertices=ret_indices_of_original_faces_and_vertices,
        )
