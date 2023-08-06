"""Inversable dictionary.
"""


class invdict(dict):
    """Inversable dict::

         >>> -invdict({'key': 'val'}) == {'val': 'key'}
    """
    def __neg__(self):
        return {v: k for k, v in self.items()}
