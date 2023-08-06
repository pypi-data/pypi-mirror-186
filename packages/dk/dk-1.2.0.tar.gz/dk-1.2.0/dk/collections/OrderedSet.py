"""Ordered Set.
   Items can only be added once, further additions have no effect.
   The iterator iterates over the items in insertion order.
"""


class oset(set):
    """Ordered Set.
       Items can only be added once, further additions have no effect.
       The iterator iterates over the items in insertion order.
    """
    def __init__(self, iterable=()):
        super().__init__()
        self._order = []
        for item in iterable:
            self.add(item)

    def add(self, item):
        if item not in self:
            self._order.append(item)
            super().add(item)

    def __iter__(self):
        return iter(self._order)

    def __repr__(self):
        return f'oset({repr(self._order)})'
