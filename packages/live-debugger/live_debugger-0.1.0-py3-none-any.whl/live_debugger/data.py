# python-live-debugger
# Copyright (C) 2022 Yunier Rojas García
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
Responsable for transforming a stack frame into an immutable dataclass. Each time a patched code executes,
:py:func:`transform_frame` receives the current stack frame and transform it into a list of
:py:class:`live_debugger.ld.FrameData`.
"""

__all__ = ["transform_frame"]

import functools
import inspect
import types
import typing

from live_debugger import typing as ld


def _qname(obj: typing.Any) -> str:
    """
    Get fully qualified class name of an object.

    Args:
        obj: Object being transformed

    Returns: The fully qualified class name of the object

    """
    klass = obj.__class__
    module = klass.__module__
    mod = f"{module}." if module != "builtins" else ""
    return f"{mod}{klass.__qualname__}"


def _next(obj: typing.Any, depth: int) -> ld.Value:
    """
    Small logic for decide whether it will use recursion or finalise the inspection using :py:func:`repr`.

    Args:
        obj: Object being transformed
        depth: Remaining depth

    Returns: An immutable representation of the object

    """
    return (
        _transform_object(obj, depth - 1)
        if depth
        else ld.Value(
            type=_qname(obj),
            value=repr(obj),
        )
    )


@functools.singledispatch
def _transform_object(obj: typing.Any, _) -> ld.Value:
    """
    Transform objects into immutable types that can be passed to callback function for processing. Given that some
    objects can be recursive or contain long concatenation of other objects, the function only reach certain depth.

    Args:
        obj: Object being transformed

    Returns: A more safe representation of the object useful enough for debugging purpose.

    """

    return _next(obj, 0)


@_transform_object.register(list)
@_transform_object.register(set)
@_transform_object.register(tuple)
def _(obj: typing.Any, depth) -> ld.Value:
    return ld.Value(
        type=_qname(obj),
        value=tuple(_next(value, depth) for value in obj),
    )


@_transform_object.register(dict)
def _(obj: typing.Any, depth) -> ld.Value:
    return ld.Value(
        type=_qname(obj),
        value=tuple((key, _next(obj[key], depth)) for key in obj),
    )


def _transform_locals(local_vars: typing.Dict[str, typing.Any], depth) -> ld.LocalsType:
    """
    Transforms the function locals into immutable structure.

    Args:
        local_vars: Local variable dictionary
        depth: Allowed depth

    Returns: Immutable tuple of local variables

    """
    return tuple(
        (str(key), _transform_object(value, depth)) for key, value in local_vars.items()
    )


def transform_frame(frame: types.FrameType, depth=2) -> typing.List[ld.FrameData]:
    """
    Transform a stack frame into a more safe data type that can be passed to callback function for processing.
    Given that some objects can be recursive or contain long concatenation of other objects, the function only
    reach certain depth.

    Args:
        frame: Stack frame being transformed
        depth: Remaining depth the function can reach

    Returns: A safe data type representation of the stack frame useful enough for debugging purpose.

    """
    return [
        ld.FrameData(
            code=_transform_code(frame.f_code),
            locals=_transform_locals(frame.f_locals, depth),
        )
    ] + [
        ld.FrameData(
            code=_transform_code(info.frame.f_code),
            locals=_transform_locals(info.frame.f_locals, depth),
        )
        for info in inspect.getouterframes(frame)
    ]


def _transform_code(obj: types.CodeType) -> ld.CodeData:
    """
    Transform a code object into a more safe data type that can be passed to callback function for processing.

    Args:
        obj: Stack frame being transformed

    Returns: A safe data type representation of the code object useful enough for debugging purpose.

    """
    return ld.CodeData(
        filename=obj.co_filename,
        flags=obj.co_flags,
        name=obj.co_name,
        first_line_no=obj.co_firstlineno,
    )
