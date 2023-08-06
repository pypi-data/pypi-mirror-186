import numpy as np
from vg.compat import v2 as vg
from .validation import check_arity


def flip_faces(faces, face_indices_to_flip=()):
    vg.shape.check(locals(), "faces", (-1, -1))
    check_arity(faces)

    flipped = np.copy(faces)
    flipped[face_indices_to_flip] = np.fliplr(faces[face_indices_to_flip])
    return flipped
