# Akatosh
This is a light weighted disceret event simulation library. The name is from the Dragon God of Time in Elder Scroll. :)

# Install
    pip install --upgrade Akatosh
  
## Example
Import modules:

    from Akatosh import Mundus, Actor
    
create actors:

the mom actor will pick up a child every second, and the child will play at home for 8 second

    class mom(Actor):
        def __init__(self, at, step, till, priority, name) -> None:
            super().__init__(at=at, step=step, till=till, priority=priority)
            self._name = name
            self._num_children = 0

        def action(self):
            c = child(at=self.timeline.now, step=1, till=8, priority=-self._num_children, name=f"Child-{self._num_children}")
            self._num_children += 1
            print(f"Time: {Mundus.now}\tEvent Priority: {self.priority}:\t{self._name} picks up a child {c._name}.")
     m = mom(at=0, step=1, till=5, priority=0, name="Mom")
            
the child actor will prevent uncle to come to visit after 7 second

    class child(Actor):
        def __init__(self, at, step, till, priority, name) -> None:
            super().__init__(at=at, step=step, till=till, priority=priority)
            self._name = name

        def action(self):
            if self.timeline.now >= 7:
                uncle.deactivate()
            print(f"Time: {Mundus.now}\tEvent Priority: {self.priority}:\t{self._name}\tis playing at home.")
            
The father actor will come to home after mother pick up all child

    father = Actor(after=m, priority=-1, action=lambda: print(f"Time: {Mundus.now}\tEvent Priority: {father.priority}:\tFather comes back home."))
    
The uncle will come to visit once father has got home for some reason...

    uncle = Actor(after=father, step=1, till=10, priority=0, action=lambda: print(f"Time: {Mundus.now}\tEvent Priority: {uncle.priority}:\tUncle comes to vist."))
    
Start the simulation for 10 second:

    Mundus.simulate(10)
