from __future__ import annotations

from typing import TYPE_CHECKING, Generator, Union

if TYPE_CHECKING:
    from Akatosh import Actor


class Event:
    _at: Union[int, float]
    _priority: int
    _actor: Actor

    def __init__(self, at: Union[int, float], priority: int, actor: Actor) -> None:
        self._at = at
        self._priority = priority
        self._actor = actor

    @property
    def at(self):
        return self._at

    @property
    def priority(self):
        return self._priority

    @property
    def actor(self):
        return self._actor
