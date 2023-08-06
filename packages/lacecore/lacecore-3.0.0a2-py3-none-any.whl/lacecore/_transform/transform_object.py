import numpy as np
from polliwog import CompositeTransform
from .._common.tri import flip_faces


class Transform:
    """
    Encapsulate a composite transform operation.

    Invoke `.end()` to apply the transform operation and create a mesh with
    transformed vertices and faces.

    Args:
        target (lacecore.Mesh): The mesh on which to operate.

    See also:
        https://polliwog.readthedocs.io/en/latest/#polliwog.CompositeTransform
    """

    def __init__(self, target):
        self.target = target
        self._transform = CompositeTransform()
        self._flip_faces = False

    def append_transform(self, forward, reverse=None):
        """
        Append an arbitrary transformation, defined by 4x4 forward and reverse
        matrices.

        Returns:
            self
        """
        self._transform.append_transform(forward=forward, reverse=reverse)
        return self

    def uniform_scale(self, factor):
        """
        Scale by the given factor.

        Args:
            factor (float): The scale factor.

        Returns:
            self
        """
        self._transform.uniform_scale(factor=factor)
        return self

    def non_uniform_scale(self, x_factor, y_factor, z_factor):
        """
        Scale along each axis by the given factors.

        Args:
            x_factor (flot): The scale factor along the `x` axis.
            y_factor (flot): The scale factor along the `y` axis.
            z_factor (flot): The scale factor along the `z` axis.

        Returns:
            self
        """
        self._transform.non_uniform_scale(x_factor, y_factor, z_factor)
        return self

    def convert_units(self, from_units, to_units):
        """
        Convert the mesh from one set of units to another.

        Supports the length units from Ounce:
        https://github.com/lace/ounce/blob/master/ounce/core.py#L26

        Returns:
            self
        """
        self._transform.convert_units(from_units=from_units, to_units=to_units)
        return self

    def translate(self, translation):
        """
        Translate by the vector provided.

        Args:
            vector (np.arraylike): A 3x1 vector.

        Returns:
            self
        """
        self._transform.translate(translation=translation)
        return self

    def reorient(self, up, look):
        """
        Reorient using up and look.

        Returns:
            self
        """
        self._transform.reorient(up=up, look=look)
        return self

    def rotate(self, rotation):
        """
        Rotate by the given 3x3 rotation matrix or a Rodrigues vector.

        Returns:
            self
        """
        self._transform.rotate(rotation=rotation)
        return self

    def flip_faces(self):
        """
        Flip the orientation of the faces.

        Returns:
            self
        """
        self._flip_faces = not self._flip_faces
        return self

    def flip(self, dim, preserve_vertex_centroid=False):
        """
        Flip about the given axis.

        Args:
            dim (int): The axis to flip around: 0 for `x`, 1 for `y`, 2 for `z`.
            preserve_vertex_centroid (bool): When `True`, translate after
                flipping to preserve the original vertex centroid.

        Returns:
            self
        """
        if dim not in (0, 1, 2):
            raise ValueError("Expected dim to be 0, 1, or 2")

        self._transform.flip(dim=dim)
        self.flip_faces()

        if preserve_vertex_centroid:
            translation = np.zeros(3)
            # `2 * vertex_centroid[dim]` takes it all the way back to the other
            # side of the axis.
            translation[dim] = 2 * self.target.vertex_centroid[dim]
            self._transform.translate(translation=translation)

        return self

    def end(self, reverse=False):
        """
        Apply the requested transformation and return a new mesh.

        Args:
            reverse (bool): When `True` applies the selected transformations
                in reverse.

        Returns:
            lacecore.Mesh: The transformed mesh.
        """
        from .._mesh import Mesh  # Avoid circular import.

        return Mesh(
            v=self._transform(self.target.v),
            f=flip_faces(self.target.f) if self._flip_faces else self.target.f,
            face_groups=self.target.face_groups,
        )
