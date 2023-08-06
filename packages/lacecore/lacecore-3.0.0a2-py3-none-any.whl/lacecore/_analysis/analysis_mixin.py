from vg.compat import v2 as vg


class AnalysisMixin:
    @property
    def vertex_centroid(self):
        """
        The centroid or geometric average of the vertices.
        """
        return vg.average(self.v)

    @property
    def bounding_box(self):
        """
        A bounding box around the vertices.

        Returns:
            polliwog.Box: The bounding box.

        See also:
            https://polliwog.readthedocs.io/en/latest/#polliwog.Box
        """
        from polliwog import Box

        return Box.from_points(self.v)

    def apex(self, along):
        """
        Find the most extreme vertex in the direction provided.

        Args:
            along (np.arraylike): A `(3,)` direction of interest.

        Returns:
            np.ndarray: A copy of the point in `self.v` which lies furthest
                in the direction of interest.
        """
        return vg.apex(self.v, along=along)

    def face_normals(self, normalize=True):
        """
        Compute surface normals of each face. The direction of the normal
        follows conventional counter-clockwise winding and the right-hand rule.

        Args:
            normalize (bool): When True, return unit-length normals.

        Returns:
            np.ndarray: Face normals as `(k, 3)`.
        """
        from polliwog.tri import surface_normals

        return surface_normals(self.v[self.f], normalize=normalize)
