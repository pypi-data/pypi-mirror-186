from .selection_object import Selection


class SelectionMixin:
    def select(self):
        """
        Begin a chained selection operation. After invoking `.select()`,
        apply selection criteria, then invoke `.end()` to create a submesh.

        Include `.union()` in the chain to combine multiple sets of
        selection criteria into a single submesh.

        Does not mutate the callee.

        Returns:
            lacecore.Selection: The selection operation.

        Example:
            >>> centroid = np.average(mesh.v, axis=0)
            >>> upper_right_quadrant = (
                mesh.select()
                .vertices_above(centroid, dim=0)
                .vertices_above(centroid, dim=1)
                .end()
            )
            >>> upper_half_plus_right_half = (
                mesh.select()
                .vertices_above(centroid, dim=0)
                .union()
                .vertices_above(centroid, dim=1)
                .end()
            )
        """
        return Selection(target=self)

    def keeping_vertices_at_or_above(self, dim, point):
        """
        Select vertices which, when projected to the given axis, are either
        coincident with the projection of the given point, or lie further
        along the axis.

        Return a new mesh, without mutating the callee.

        Args:
            dim (int): The axis of interest: 0 for `x`, 1 for `y`, 2 for `z`.
            point (np.arraylike): The point of interest.

        Returns:
            lacecore.Mesh: A submesh containing the selection.
        """
        return self.select().vertices_at_or_above(dim=dim, point=point).end()

    def keeping_vertices_above(self, dim, point):
        """
        Select vertices which, when projected to the given axis, lie further
        along that axis than the projection of the given point.

        Return a new mesh, without mutating the callee.

        Args:
            dim (int): The axis of interest: 0 for `x`, 1 for `y`, 2 for `z`.
            point (np.arraylike): The point of interest.

        Returns:
            lacecore.Mesh: A submesh containing the selection.
        """
        return self.select().vertices_above(dim=dim, point=point).end()

    def keeping_vertices_at_or_below(self, dim, point):
        """
        Select vertices which, when projected to the given axis, are either
        coincident with the projection of the given point, or lie before it.

        Return a new mesh, without mutating the callee.

        Args:
            dim (int): The axis of interest: 0 for `x`, 1 for `y`, 2 for `z`.
            point (np.arraylike): The point of interest.

        Returns:
            lacecore.Mesh: A submesh containing the selection.
        """
        return self.select().vertices_at_or_below(dim=dim, point=point).end()

    def keeping_vertices_below(self, dim, point):
        """
        Select vertices which, when projected to the given axis, lie before
        the projection of the given point.

        Return a new mesh, without mutating the callee.

        Args:
            dim (int): The axis of interest: 0 for `x`, 1 for `y`, 2 for `z`.
            point (np.arraylike): The point of interest.

        Returns:
            lacecore.Mesh: A submesh containing the selection.
        """
        return self.select().vertices_below(dim=dim, point=point).end()

    def keeping_vertices_on_or_in_front_of_plane(self, plane):
        """
        Select the vertices which are either on or in front of the given
        plane.

        Return a new mesh, without mutating the callee.

        Args:
            plane (polliwog.Plane): The plane of interest.

        Returns:
            lacecore.Mesh: A submesh containing the selection.

        See also:
            https://polliwog.readthedocs.io/en/latest/#polliwog.Plane
        """
        return self.select().vertices_on_or_in_front_of_plane(plane=plane).end()

    def keeping_vertices_in_front_of_plane(self, plane):
        """
        Select the vertices which are in front of the given plane.

        Return a new mesh, without mutating the callee.

        Args:
            plane (polliwog.Plane): The plane of interest.

        Returns:
            lacecore.Mesh: A submesh containing the selection.

        See also:
            https://polliwog.readthedocs.io/en/latest/#polliwog.Plane
        """
        return self.select().vertices_in_front_of_plane(plane=plane).end()

    def keeping_vertices_on_or_behind_plane(self, plane):
        """
        Select the vertices which are either on or behind the given plane.

        Return a new mesh, without mutating the callee.

        Args:
            plane (polliwog.Plane): The plane of interest.

        Returns:
            lacecore.Mesh: A submesh containing the selection.

        See also:
            https://polliwog.readthedocs.io/en/latest/#polliwog.Plane
        """
        return self.select().vertices_on_or_behind_plane(plane=plane).end()

    def keeping_vertices_behind_plane(self, plane):
        """
        Select the vertices which are behind the given plane.

        Return a new mesh, without mutating the callee.

        Args:
            plane (polliwog.Plane): The plane of interest.

        Returns:
            lacecore.Mesh: A submesh containing the selection.

        See also:
            https://polliwog.readthedocs.io/en/latest/#polliwog.Plane
        """
        return self.select().vertices_behind_plane(plane=plane).end()

    def picking_vertices(self, indices_or_boolean_mask):
        """
        Select only the given vertices.

        Return a new mesh, without mutating the callee.

        Args:
            indices_or_boolean_mask (np.arraylike): Either a list of vertex
                indices, or a boolean mask the same length as the vertex array.

        Returns:
            lacecore.Mesh: A submesh containing the selection.
        """
        return (
            self.select()
            .pick_vertices(indices_or_boolean_mask=indices_or_boolean_mask)
            .end()
        )

    def picking_faces(self, indices_or_boolean_mask):
        """
        Select only the given faces.

        Return a new mesh, without mutating the callee.

        Args:
            indices_or_boolean_mask (np.arraylike): Either a list of vertex
                indices, or a boolean mask the same length as the vertex array.

        Returns:
            lacecore.Mesh: A submesh containing the selection.
        """
        return (
            self.select()
            .pick_faces(indices_or_boolean_mask=indices_or_boolean_mask)
            .end()
        )

    def picking_face_groups(self, *group_names):
        """
        Select faces which belong to the given face groups.

        Args:
            group_names (list): The face groups to keep.

        Returns:
            lacecore.Mesh: A submesh containing the selection.
        """
        return self.select().pick_face_groups(*group_names).end()

    def sliced_by_plane(self, *planes, only_for_selection=None):
        """
        Slice the triangles, keeping the portion in front of the given plane.

        - Faces partially in front of the plane are sliced.
        - Faces fully in front of the plane are kept as is.
        - Faces fully behind the plane are culled.

        Return a new mesh, without mutating the callee.

        Args:
            plane (polliwog.Plane): The plane of interest.
            only_for_selection (function): A function which receives a
                `lacecore.Selection` and should invoke selection methods on it.

        Returns:
            lacecore.Mesh: The sliced mesh.

        See also:
            https://polliwog.readthedocs.io/en/latest/#polliwog.Plane
        """
        from polliwog import Plane
        from polliwog.plane import slice_triangles_by_plane
        from .._mesh import Mesh

        for plane in planes:
            assert isinstance(plane, Plane)

        working = self
        for plane in planes:
            # Since slicing renumbers the faces, recompute `faces_to_slice`
            # after each slice.
            if only_for_selection is None:
                faces_to_slice = None
            else:
                selection = working.select()
                only_for_selection(selection)
                faces_to_slice, _ = selection.generate_masks()

            vertices, faces, face_mapping = slice_triangles_by_plane(
                vertices=working.v,
                faces=working.f,
                plane_reference_point=plane.reference_point,
                plane_normal=plane.normal,
                faces_to_slice=faces_to_slice,
                ret_face_mapping=True,
            )
            face_groups = (
                None
                if working.face_groups is None
                else working.face_groups.reindexed(face_mapping)
            )
            working = Mesh(v=vertices, f=faces, face_groups=face_groups)
        return working
