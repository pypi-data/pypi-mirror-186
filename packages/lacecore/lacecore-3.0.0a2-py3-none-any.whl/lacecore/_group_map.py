import numpy as np
from vg.compat import v2 as vg


class GroupMap:
    """
    An immutable map of groups of elements, which are allowed to overlap.
    These can be used for face or vertex groups, as in the Wavefront OBJ
    standard.

    Args:
        num_elements (int): The total number of elements. This determines
            the length of the masks.
        group_names (list): The names of the groups.
        masks (np.array): A boolean array with a row containing a boolean
            mask for each group.

    See also:
        http://paulbourke.net/dataformats/obj/
    """

    def __init__(self, num_elements, group_names, masks, copy_masks=False):
        if not isinstance(num_elements, int) or num_elements < 0:
            raise ValueError("num_elements should be a non-negative integer")
        if not all(isinstance(group_name, str) for group_name in group_names):
            raise ValueError("group_names should be a list of strings")
        vg.shape.check(locals(), "masks", (len(group_names), num_elements))
        if masks.dtype != bool:
            raise ValueError("Expected masks to be a bool array")

        if copy_masks:
            masks = masks.copy()
        masks.setflags(write=False)
        self._num_elements = num_elements
        self._masks = masks
        self._group_names = {k: i for i, k in enumerate(group_names)}

    @classmethod
    def from_dict(cls, group_data, num_elements):
        """
        Create a group map from a dictionary of elements. The keys are the
        group names and the values are lists of element indices.

        Args:
            group_data (dict): The group data.
            num_elements (int): The total number of elements.
        """
        masks = np.zeros((len(group_data), num_elements), dtype=bool)
        for i, element_indices in enumerate(group_data.values()):
            try:
                masks[i][element_indices] = True
            except IndexError:
                raise ValueError(
                    "Element indices should be less than {}".format(num_elements)
                )
        return cls(
            num_elements=num_elements,
            group_names=group_data.keys(),
            masks=masks,
            copy_masks=False,
        )

    def __len__(self):
        """
        Get the number of groups.

        Returns:
            int: The number of groups.
        """
        return len(self._group_names)

    def __iter__(self):
        """
        Iterate over the groups.

        Returns:
            list_iterator: An iterator over the groups.
        """
        return iter(self._group_names)

    def __getitem__(self, group_name):
        """
        Get the read-only mask for the requested group.

        Args:
            group_name (string): The desired group.

        Returns:
            np.array: A read-only boolean array with length equal to
            `self.num_elements`.
        """
        try:
            index = self._group_names[group_name]
        except KeyError:
            raise KeyError("Unknown group: {}".format(group_name))
        return self._masks[index]

    def keys(self):
        """
        Get the names of all the groups.

        Returns:
            list: A list of the group names.
        """
        return list(self._group_names)

    @property
    def num_elements(self):
        return self._num_elements

    def to_dict(self):
        return {
            group_name: list(self[group_name].nonzero()[0])
            for group_name in self.keys()
        }

    def mask_for_element(self, element):
        """
        Get the read-only group mask for the requested element.

        Args:
            element (int): The desired element.

        Returns:
            np.array: A read-only boolean array corresponding to the
                group names in `self.keys()`.
        """
        return self._masks[:, element]

    def group_names_for_element_mask(self, element_mask):
        """
        Translate an element mask to a list of group names.

        Args:
            element_mask (np.array): An element mask (e.g. a return value from
                `mask_for_element()`).

        Returns:
            list: The group membership represented by the element mask.
        """
        vg.shape.check(locals(), "element_mask", (len(self._group_names),))
        group_names = self.keys()
        return [group_names[index] for index in element_mask.nonzero()[0]]

    def union(self, *group_names):
        """
        Construct the union of the requested groups and return it as a
        writable mask.

        Args:
            group_names (list): The requested groups.

        Returns:
            np.array: A boolean mask with length equal to `self.num_elements`.
        """
        if not all(isinstance(group_name, str) for group_name in group_names):
            raise ValueError("Group names must be strings")
        indices = []
        invalid_group_names = []
        for group_name in group_names:
            try:
                indices.append(self._group_names[group_name])
            except KeyError:
                invalid_group_names.append(group_name)
        if len(invalid_group_names):
            raise KeyError("Unknown groups: {}".format(", ".join(invalid_group_names)))
        return np.any(self._masks[indices], axis=0)

    def reindexed(self, f_new_to_old):
        """
        Given a mapping from new face indices to old face indices, construct
        a group map which preserves the original groups but references the
        new set of indices. When reindexing a mesh, invoke this function on
        the old group map to construct a new group map which preserves the
        original segments wherever possible.

        Args:
            f_new_to_old (np.ndarray): The old face index
                corresponding to each of the new faces.

        Returns:
            GroupMap: A new group map suitable for use with the new faces.
        """
        return GroupMap(
            num_elements=len(f_new_to_old),
            group_names=self._group_names,
            masks=np.asarray(self._masks[:, f_new_to_old]),
            copy_masks=False,
        )

    def defragment(self, group_order=None):
        """
        Reorder the faces to keep groups together.

        Overlapping groups are not supported.

        Args:
            group_order (list): The desired order of the groups. The default is
                to order by the first face in which the group appears.

        Returns:
            np.ndarray: The new order of the faces, suitable for passing to
            `lacecore.reindex_faces()`.
        """
        from collections import Counter
        from ._mesh import FACE_DTYPE

        if group_order is None:
            # Inspired by https://stackoverflow.com/a/22150003/893113
            group_order = [item[0] for item in Counter(self._group_names).most_common()]
            group_order.reverse()
        else:
            nonempty_groups = [
                group_name for group_name in self if np.any(self[group_name])
            ]
            missing_groups = set(nonempty_groups) - set(group_order)
            if len(missing_groups) > 0:
                raise ValueError(
                    f"group_order is missing groups: {', '.join(sorted(list(missing_groups)))}"
                )
            unknown_groups = set(group_order) - set(self.keys())
            if len(unknown_groups) > 0:
                raise ValueError(
                    f"group_order contains unknown groups: {', '.join(sorted(list(unknown_groups)))}"
                )

        ordering = np.zeros(0, dtype=FACE_DTYPE)
        for group_name in group_order:
            this_mask = self[group_name]
            these_elements = this_mask.nonzero()[0]
            if len(np.intersect1d(ordering, these_elements)) > 0:
                raise ValueError(f'Group "{group_name}" overlaps with previous groups')
            ordering = np.append(ordering, these_elements)
        return ordering
