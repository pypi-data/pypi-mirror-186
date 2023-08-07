from Akatosh import Mundus, Actor

class mom(Actor):

    def __init__(self, at, step, till, priority, name) -> None:
        super().__init__(at=at, step=step, till=till, priority=priority)
        self._name = name
        self._num_children = 0

    def action(self):
        c = child(at=self.timeline.now, step=1, till=8, priority=-self._num_children, name=f"Child-{self._num_children}")
        self._num_children += 1
        print(f"Time: {Mundus.now}\tEvent Priority: {self.priority}:\t{self._name} picks up a child {c._name}.")

class child(Actor):

    def __init__(self, at, step, till, priority, name) -> None:
        super().__init__(at=at, step=step, till=till, priority=priority)
        self._name = name

    def action(self):
        if self.timeline.now >= 7:
            uncle.deactivate()
        print(f"Time: {Mundus.now}\tEvent Priority: {self.priority}:\t{self._name}\tis playing at home.")

m = mom(at=0, step=1, till=5, priority=0, name="Mom")
father = Actor(after=m, priority=-1, action=lambda: print(f"Time: {Mundus.now}\tEvent Priority: {father.priority}:\tFather comes back home."))
uncle = Actor(after=father, step=1, till=10, priority=0, action=lambda: print(f"Time: {Mundus.now}\tEvent Priority: {uncle.priority}:\tUncle comes to vist."))

Mundus.simulate(10)
print(m.status)
print(father.status)
print(uncle.status)
