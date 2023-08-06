from .nests import NestedDict, NestedList, NestedTuple

__all__ = ['NestedDict', 'NestedList', 'NestedTuple']

__locals = locals()
for __name in __all__:
    if not __name.startswith("__"):
        setattr(__locals[__name], "__module__", "nested_inside")  # noqa