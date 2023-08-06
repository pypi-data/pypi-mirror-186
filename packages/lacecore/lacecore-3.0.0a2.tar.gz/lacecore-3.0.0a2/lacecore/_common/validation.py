import numpy as np


def check_arity(faces):
    if faces.shape[1] not in [3, 4]:
        raise ValueError("Expected 3 or 4 vertices per face")


def check_indices(indices, num_elements, name):
    if np.any(indices >= num_elements):
        raise ValueError(
            "Expected indices in {} to be less than {}".format(name, num_elements)
        )
