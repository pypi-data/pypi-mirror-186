from ctypes import Union
from math import inf
from typing import List, Union
from uuid import uuid4

from .timeline import Timeline


class Universe:
    _id: int
    _timeline: Timeline
    _till: Union[int, float]

    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(Universe, cls).__new__(cls)
        return cls.instance

    def __init__(self) -> None:
        self._id = uuid4().int
        self._timeline = Timeline()
        self._till = int()

    def simulate(self, till: Union[int, float] = inf) -> None:
        self._till = till
        while self.timeline.now <= self.till:
            self.timeline.forward(self.till)
            if len(self.timeline.events) == 0:
                break

    @property
    def timeline(self) -> Timeline:
        return self._timeline

    @property
    def till(self) -> Union[int, float]:
        return self._till

    @property
    def now(self) -> Union[int, float]:
        return self.timeline.now


Mundus = Universe()
