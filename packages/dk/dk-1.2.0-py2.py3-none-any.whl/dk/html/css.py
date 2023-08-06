from dk.collections import pset


class css(pset):
    def __init__(self, **attrs):
        super().__init__()
        for key, val in sorted(attrs.items()):
            if isinstance(val, bytes):
                val = val.decode('u8')
            if isinstance(key, bytes):
                key = key.decode('u8')
            self[key.replace('_', '-')] = val

    def __setattr__(self, key, val):
        super().__setattr__(key.replace('_', '-'), val)

    def attrs(self):
        yield from sorted(list(self.items()))

    def __str__(self):
        return ';'.join(f'{k}:{v}' for (k, v) in self.attrs())

    __repr__ = __str__
