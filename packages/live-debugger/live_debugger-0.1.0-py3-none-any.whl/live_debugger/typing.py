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
Types used in public interfaces to facilitate extending the library if necessary.
"""

__all__ = [
    "CodeData",
    "Value",
    "LocalsType",
    "FrameData",
    "CallbackType",
    "ConditionType",
    "CookieType",
    "LiveDebuggerProtocol",
]

import abc
import types
import typing
from dataclasses import dataclass


@dataclass(frozen=True)
class CodeData:
    """
    Data structure collected from :py:class:`types.CodeType` objects.
    """

    filename: str
    flags: int
    name: str
    first_line_no: int


@dataclass(frozen=True)
class Value:
    type: str
    value: typing.Any


LocalsType = typing.Tuple[typing.Tuple[str, Value], ...]


@dataclass(frozen=True)
class FrameData:
    """
    Data structure collected from :py:class:`types.FrameType` objects.
    """

    code: CodeData
    locals: LocalsType


CookieType = str
"""
Type associated with the identifier for point information when using :py:class:`LiveDebuggerProtocol`. It should be
a unique string.
"""

CallbackType = typing.Callable[[typing.List[FrameData]], None]
"""
Signature of the callback functions that can handle already processed information by :py:class:`LiveDebuggerProtocol`.
This type represents functions that actually do something about that data collected like storing int on a file or
sending it to a server.
"""

ConditionType = typing.Optional[types.CodeType]
"""
Type of the conditions that will evaluate whether the callback can be executed or not. Most of the cases, it will be the
result of using :py:func:`compile` function.
"""


class LiveDebuggerProtocol(typing.Protocol):
    """
    Protocol to facilitate the implementation of replacement classes that can be used in :py:mod:`live_debugger.api`.
    """

    @abc.abstractmethod
    def add_point(
        self,
        fn: str,
        line: int,
        callback: CallbackType,
        *,
        condition: ConditionType = None
    ) -> CookieType:
        """

        Args:
            fn: Filename of the function or code we want to patch. This path must be relative to some `PYTHONPATH` path.
            line: Line number in the file
            callback: Function that will receive data when the code gets executed
            condition: Optional condition for this callback to get activated

        Returns:
            CookieType: Unique cookie used to identify and remove a debugging code

        """
        raise NotImplementedError

    @abc.abstractmethod
    def clear_point(self, cookie: CookieType):
        """
        Remove all changes related to the cookie.

        Args:
            cookie: Unique cookie identifying a previously installed point.

        """

        raise NotImplementedError

    @abc.abstractmethod
    def is_active(self) -> bool:
        """
        Whether the debugger is actively collecting information from points or not

        Returns: Is the debugger active or not

        """
        raise NotImplementedError

    @abc.abstractmethod
    def activate(self):
        """
        Activates the debugger class to collect debugging information from the registered points. This method must
        be idempotent.

        """
        raise NotImplementedError

    @abc.abstractmethod
    def deactivate(self):
        """
        Prevent the debugger class from collect debugging information from the registered points. This method must
        be idempotent. It must guaranty all debugging point can not be activated after this.

        """
        raise NotImplementedError
