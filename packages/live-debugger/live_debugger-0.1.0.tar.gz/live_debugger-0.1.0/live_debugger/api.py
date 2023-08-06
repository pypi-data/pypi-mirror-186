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
Simple and clean `Façade pattern <https://en.wikipedia.org/wiki/Facade_pattern>`_ for managing debuggers.

>>> from live_debugger import api
>>> cookie = api.add_point("flask_example/app.py", 33, print)
>>> api.clear_point(cookie)



Module
******
"""

__all__ = ["use", "add_point", "clear_point"]

from live_debugger import debugger
from live_debugger import typing as ld_typing

_registry: ld_typing.LiveDebuggerProtocol = debugger.LiveDebugger()
"Registry of points."


def use(registry: ld_typing.LiveDebuggerProtocol):
    """
    Sets a Registry object to use in the API. By defaults, the library uses the one implemented in
    :class:`live_debugger.debuggers.tracing.points.PointRegistry`. Any object passed to this function should implement
    :class:`live_debugger.typing.LiveDebuggerProtocol`. When called, old registry object is deactivated and parameter
    ``registry`` is activated after.

    Args:
        registry (live_debugger.typing.LiveDebuggerProtocol): Registry object to use when calling this API.


    """
    global _registry
    _registry.deactivate()
    _registry = registry


def add_point(
    fn: str,
    line: int,
    callback: ld_typing.CallbackType,
    *,
    condition: ld_typing.ConditionType = None
) -> ld_typing.CookieType:
    """
    Adds an inspection point for the debugger. It triggers
    :py:meth:`live_debugger.typing.LiveDebuggerProtocol.add_point` of the debugger currently active in the module.

    Args:
        fn: Filename of the function or code we want to patch. This path must be relative to some `PYTHONPATH` path.
        line: Line number in the file
        callback: Function that will receive data when the code gets executed
        condition: Optional condition for this callback to get activated

    Returns:
        live_debugger.typing.CookieType: Unique cookie used to identify and remove a debugging code

    """
    global _registry
    return _registry.add_point(fn, line, callback, condition=condition)


def clear_point(cookie: ld_typing.CookieType):
    """
    Remove all changes related to the cookie. It triggers
    :py:meth:`live_debugger.typing.LiveDebuggerProtocol.clear_point` of the debugger currently active in the module.

    Args:
        cookie: Unique cookie identifying a previously installed point.

    """
    global _registry
    return _registry.clear_point(cookie)


def is_activate() -> bool:
    """
    Activates current debugger to collect debugging information from the registered points. Can be called multiple
    times, always with the same result. It triggers :py:meth:`live_debugger.typing.LiveDebuggerProtocol.is_active`
    of the debugger currently active in the module.

    """
    global _registry
    return _registry.is_active()


def activate():
    """
    Activates current debugger to collect debugging information from the registered points. Can be called multiple
    times, always with the same result. It triggers :py:meth:`live_debugger.typing.LiveDebuggerProtocol.activate`
    of the debugger currently active in the module.

    """
    global _registry
    return _registry.activate()


def deactivate():
    """
    Prevent current debugger class from collect debugging information from the registered points. It triggers
    :py:meth:`live_debugger.typing.LiveDebuggerProtocol.deactivate` of the debugger currently active in the module.
    """
    global _registry
    return _registry.deactivate()
