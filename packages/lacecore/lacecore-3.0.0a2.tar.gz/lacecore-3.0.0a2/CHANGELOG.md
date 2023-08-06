# Changelog

## 3.0.0a2

- Support NumPy 1.24+


## 3.0.0a1

- Allow any version of numpy
- Test in Python 3.9


## 3.0.0a0

- Support polliwog 3.0.0 prereleases.


## 2.4.3

- Revert previous change. This version does not support polliwog 3.0.0
  prereleases.


## 2.4.2

- Support polliwog 3.0.0 prereleases.


## 2.4.1

- GroupMap: Fix `defragment()`.


## 2.4.0

- GroupMap: Add `defragment()` and `to_dict()` methods.


## 2.3.0

- `check_arity()` and `check_indices()`: Add to public interface.


## 2.2.0

- Improve `.sliced_by_plane()`:
  - Slice a submesh by passing `only_for_selection`
  - Slice by several planes at once
  - Preserve `face_groups` when slicing
- Selection: Add `generate_masks()`method
- Selection: Improve error message for `.pick_face_groups()` on meshes without
  face groups.
- Upgrade to polliwog >= 2.1.0.

## 2.1.0

- Add `.face_normals()` method.

## 2.0.0

- Mesh constructor requires face indices to have dtype `np.int64`.
- Add `lacecore.FACE_DTYPE` property.
- Upgrade to pollliwog >= 2.0.0.

While this restriction may be a little inconvenient for the caller, it improves
interoperability and performance, simplifies the implementation, and produces
more predictable return values. It's recommended that applications using lacecore
store all face indices using this dtype.

## 1.1.0

- Add `sliced_by_plane()` method.
- Upgrade to polliwog >= 1.1.0.

## 1.0.0

- Upgrade to polliwog >= 1.0.0 and vg >= 2.0.0.

## 0.11.0

- Upgrade to polliwog 1.0.0b14 and vg >= 1.11.1.

## 0.10.0

- Bump tinyobjloader to work around an issue in Poetry. Poetry will not
  install dependency versions like 2.0.0rc9.dev0.

## 0.9.0

- Upgrade to polliwog 1.0.0b13.

## 0.8.0

- Selection: add `pick_vertices_of_face_groups()` method.

## 0.7.0

- Temporarily use the [Curvewise fork of tinyobjloader][fork].

[fork]: https://github.com/curvewise-forks/tinyobjloader

## 0.6.0

- Add `faces_triangulated()` method.
- Correctly preserve groups when reindexing faces.
- Upgrade to tinyobjloader 2.0.0rc8.

## 0.5.0

- Add `load_obj_string()` function.
- Upgrade to tinyobjloader 2.0.0rc7.

## 0.4.1

- Ensure faces have integral dtype.

## 0.4.0

- obj: Add support for triangulating mixed arities.
- Upgrade to tinyobjloader 2.0.0rc6.
- Upgrade to polliwog 1.0.0b10.

## 0.3.0

- Upgrade to polliwog 1.0.0b8.
- Remove `lacecore.shapes.rectangle()`.

## 0.2.0

### New features

- Optional OBJ loading with `pip install lacecore[obj]`.
- Add transform methods.
- Add group selection.
- Add `apex()` method.
- Add `vertex_centroid` and `bounding_box` properties.

### Bug fixes

- Pass through `face_groups` when returning a new mesh.
- Reject invalid `point` from selection methods.
- Avoid scrambling correspondence with inconsistent triangulation.


## 0.1.0

Initial release.
