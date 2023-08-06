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
Basic implementation of :class:`live_debugger.typing.LiveDebuggerProtocol` using a Singleton pattern based on
class attributes.
"""

__all__ = ["LiveDebugger"]

import collections
import sys
import types
import typing
import uuid
from os import path

from live_debugger import data
from live_debugger import typing as ld_typing

_KeyType = typing.Tuple[str, int]
_PointDataType = typing.DefaultDict[
    _KeyType,
    typing.Dict[str, typing.Tuple[ld_typing.CallbackType, ld_typing.ConditionType]],
]
_FrameHandlerType = typing.Callable[[types.FrameType], None]


class LiveDebugger(ld_typing.LiveDebuggerProtocol):
    """
    Registry to keep record of installed points in each code object.

    This class keeps a record of all patches lines of a code object with all callbacks and conditions. Each time a
    point is added using :py:meth:`PointRegistry.add_point` stores all necessary information to trigger the callback
    when the code is executed or to clear the point using :py:meth:`PointRegistry.clear_point`.

    The class stores all information in class attributes so the class itself acts as a Singleton. It implements
    :py:class:`live_debugger.typing.LiveDebuggerProtocol` as `classmethod` using those class attributes.

    The module is compiled to C using `Cython <https://cython.org/>`_ to provide fast code execution when needed the
    most: when the patched code kicks in, the frame stack needs to be "exported" to a more friendly format and be
    passed to all callbacks matching the condition.

    """

    __slots__ = [
        "_callbacks",
        "_lines",
        "_handlers",
        "_cookies",
        "_old_tracer",
        "_trace_allowed_events",
        "_active",
    ]

    def __init__(self):
        self._callbacks: _PointDataType = collections.defaultdict(dict)
        self._lines: typing.Dict[str, typing.Set[int]] = collections.defaultdict(set)
        self._handlers: typing.Dict[_KeyType, _FrameHandlerType] = {}
        self._cookies: typing.Dict[ld_typing.CookieType, _KeyType] = {}
        self._old_tracer = None
        self._trace_allowed_events = {"call", "line"}
        self._active = False

    def _make_safe_handler(
        self, key: _KeyType
    ) -> typing.Callable[[types.FrameType], None]:
        """
        Function factory that takes a tuple if (code id, line number) and returns a function capable of handling
        the frame object from the code point. The built function transform :py:class:`types.FrameType` into a
        :py:class:`live_debugger.models.FrameData` object and passed into all callbacks of the key which the condition
        activates.

        Args:
            key: Tuple of filename and line number

        Returns: Function to handle a stack frame

        """

        def handler(frame: types.FrameType):
            info = data.transform_frame(frame)

            for cb, cond in self._callbacks.get(key, {}).values():
                if cond is None or eval(  # nosec B307
                    cond, frame.f_globals, frame.f_locals
                ):
                    cb(info)

        return handler

    def add_point(
        self,
        fn: str,
        line: int,
        callback: ld_typing.CallbackType,
        *,
        condition: ld_typing.ConditionType = None
    ) -> ld_typing.CookieType:
        """
        Stores a callback and a condition for activate it when the code runs. If the specified code does not have a
        bytecode patch already installed, this method will install it but only once.

        Args:
            fn: Filename hosting the source code
            line: Line number
            callback: Function handling the data processed from the stack frame
            condition: Condition to decide whether to call the callback or not

        Returns: Unique cookie that identifies all changes made to the code with the data stored

        """

        # let's find the importable path of the given file
        for p in sys.path:
            if path.exists(path.join(p, fn)):
                fn = path.join(p, fn)

        key = (fn, line)
        # if the file and lineno are first time seen, set up a handler for it
        if key not in self._handlers:
            handler = self._make_safe_handler(key)
            self._lines[fn].add(line)
            self._handlers[key] = handler

        # store callback information associated with a cookie
        cookie = str(uuid.uuid4())
        self._cookies[cookie] = key
        self._callbacks[key][cookie] = (callback, condition)

        if not self._is_tracing() and self.is_active():
            self._start_tracing()

        return cookie

    def clear_point(self, cookie: str):
        """
        Clear all data associated with a cookie.

        Args:
            cookie: Unique cookie identifying the previous installed callback.

        """

        fn, line = key = self._cookies[cookie]
        del self._callbacks[key][cookie]

        if not self._callbacks[key]:
            del self._handlers[key]
            del self._callbacks[key]
            del self._lines[fn]

        if not self._callbacks:
            self._stop_tracing()

        del self._cookies[cookie]

    def _trace_dispatch(self, frame, event, arg):
        if event not in self._trace_allowed_events:
            return

        fn = frame.f_code.co_filename
        if fn in self._lines:
            return self._trace_lines

    def _trace_lines(self, frame, event, arg):
        if event not in self._trace_allowed_events:
            return

        fn = frame.f_code.co_filename
        line = frame.f_lineno
        key = (fn, line)
        if key in self._handlers:
            self._handlers[key](frame)

    def _is_tracing(self):
        tracer = sys.gettrace()
        return tracer == self._trace_dispatch

    def _stop_tracing(self):
        sys.settrace(self._old_tracer)

    def _start_tracing(self):
        tracer = sys.gettrace()
        self._old_tracer = tracer
        sys.settrace(self._trace_dispatch)

    def is_active(self):
        return self._active

    def activate(self):
        if self.is_active():
            return

        self._active = True
        self._start_tracing()

    def deactivate(self):
        if not self.is_active():
            return
        self._active = False
        self._stop_tracing()
