from __future__ import annotations
from typing import Generator, List, Optional, Union, Callable
from uuid import uuid4
from math import inf

from Akatosh import Event, Timeline, Mundus


class Actor:

    _id: int
    _action: Optional[Generator | Callable]
    _timeline: Timeline
    _priority: int
    _at: Union[int, float]
    _step: Union[int, float, Callable]
    _till: Union[int, float]
    _active: bool
    _after: Actor

    _time: Union[int, float]
    _status: List[str]
    _followers: List[Actor]

    def __init__(
        self,
        action: Optional[Generator | Callable] = None,
        timeline: Optional[Timeline] = None,
        priority: int = 0,
        at: Union[int, float, Callable] = 0,
        step: Optional[int | float | Callable] = None,
        till: Optional[int | float | Callable] = None,
        active: bool = True,
        after: Optional[Actor] = None,
    ) -> None:

        # generate a unique id for this actor
        self._id = uuid4().int

        # assign the action to this actor
        self._action = action

        # assign the timeline to this actor
        if timeline is None:
            self._timeline = Mundus.timeline
        else:
            self._timeline = timeline
        self.timeline.actors.append(self)

        # assign the priority to this actor
        self._priority = priority

        # initialize the follower list
        self._followers = list()

        # assign the waiting target to this actor
        if after is not None:
            self._after = after
            after.followers.append(self)

        # initialize the time
        self._time = at
        self._step = step
        self._till = till

        # initialize the status
        self._status = list()
        if active:
            self.status.append("active")
        else:
            self.status.append("inactive")
        if after is not None:
            self.status.append("onhold")

        # schedule the actor onto timeline
        if self.onhold is False:
            self.timeline.schedule(self)

    def perform(self):
        if self.step is None and self.till is None:
            if self.active:
                self.action()
        elif self.step is None and self.till is not None:
            raise AttributeError(f"Actor {self.id} has no step size defined.")
        elif self.step is not None and self.till is None:
            self._till = inf
            while self.time < self.till:
                if self.active:
                    self.action()
                if callable(self.step):
                    self._time += self.step()
                else:
                    self._time += self.step
                yield self.timeline.schedule(self)
            if self.active:
                self.action()
        elif self.step is not None and self.till is not None:
            if callable(self.till):
                self._till = self.till()
            while self.time < self.till:
                if self.active:
                    self.action()
                if callable(self.step):
                    self._time += self.step()
                else:
                    self._time += self.step
                yield self.timeline.schedule(self)
            if self.active:
                self.action()

    def deactivate(self):
        if "active" in self.status:
            self.status.remove("active")
        if "inactive" not in self.status:
            self.status.append("inactive")

    @property
    def id(self):
        return self._id

    @property
    def priority(self):
        return self._priority

    @property
    def action(self):
        return self._action

    @property
    def timeline(self):
        return self._timeline

    @property
    def time(self):
        return self._time

    @property
    def till(self):
        return self._till

    @property
    def step(self):
        return self._step

    @property
    def status(self):
        return self._status

    @property
    def after(self):
        return self._after

    @property
    def active(self):
        return "active" in self.status

    @property
    def inactive(self):
        return "inactive" in self.status

    @property
    def onhold(self):
        return "onhold" in self.status

    @property
    def completed(self):
        return "completed" in self.status

    @property
    def followers(self):
        return self._followers
