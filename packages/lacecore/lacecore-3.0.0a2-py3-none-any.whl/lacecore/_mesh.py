import numpy as np
from vg.compat import v2 as vg
from ._analysis.analysis_mixin import AnalysisMixin
from ._common.validation import check_arity, check_indices
from ._obj.writer import write as write_obj
from ._selection.selection_mixin import SelectionMixin
from ._transform.transform_mixin import TransformMixin


FACE_DTYPE = np.int64


class Mesh(AnalysisMixin, SelectionMixin, TransformMixin):
    """
    A triangular or quad mesh. Vertices and faces are represented using NumPy
    arrays. Instances are read-only, at least for now. This class is optimized
    for cloud computation.

    Args:
        v (np.ndarray): A `kx3` array of vertices. It will be marked read-only.
        f (np.ndarray): A `kx3` or `kx4` array of vertex indices which make
            up the faces. It will be marked read-only.
        copy_v (bool): When `True`, the input vertices will be copied before
            they are marked read-only.
        copy_f (bool): When `True`, the input faces will be copied before
            they are marked read-only.
    """

    def __init__(self, v, f, copy_v=False, copy_f=False, face_groups=None):
        num_vertices = vg.shape.check(locals(), "v", (-1, 3))
        vg.shape.check(locals(), "f", (-1, -1))
        assert f.dtype == FACE_DTYPE
        check_arity(f)
        check_indices(f, num_vertices, "f")

        # TODO: Needs coverage.
        # if copy_f:
        #     f = np.copy(f)
        # if copy_v:
        #     v = np.copy(v)
        f.setflags(write=False)
        v.setflags(write=False)
        self.f = f
        self.v = v
        self.face_groups = face_groups

    # TODO: Needs coverage.
    # @classmethod
    # def from_trimesh(cls, mesh):
    #     return cls(v=mesh.vertices, f=mesh.faces)

    def __repr__(self):
        return f"lacecore.Mesh(num_v={self.num_v}, num_f={self.num_f})"

    @property
    def num_v(self):
        """
        The number of vertices.

        Return:
            int: The number of vertices.
        """
        return len(self.v)

    @property
    def num_f(self):
        """
        The number of faces.

        Return:
            int: The number of faces.
        """
        return len(self.f)

    @property
    def is_tri(self):
        """
        `True` if a triangular mesh.

        Return:
            bool: `True` if a triangular mesh.
        """
        return self.f.shape[1] == 3

    @property
    def is_quad(self):
        """
        `True` if a triangular mesh.

        Return:
            bool: `True` if a triangular mesh.
        """
        return self.f.shape[1] == 4

    def write_obj(self, filename):
        """
        Save a mesh's faces, vertices, and face groups to a Wavefront OBJ file.

        Args:
            filename (str): The file to write. If it exists, it will be
                overwritten.
        """
        with open(filename, "w") as f:
            write_obj(f, self)
