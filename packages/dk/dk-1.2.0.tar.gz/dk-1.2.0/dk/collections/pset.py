"""
Mapping classes.
"""
from collections import namedtuple


keyval = namedtuple('keyval', 'key val')


def xmlrepr(v, toplevel=False):
    "Return ``v`` as xml tag-soup."
    if toplevel:
        return '<?xml version="1.0" standalone="yes"?>\n' + xmlrepr(v)

    if hasattr(v, '__xml__'):
        return v.__xml__()
    if isinstance(v, list):
        res = []
        for item in v:
            if hasattr(item, '__xml__'):
                res.append(xmlrepr(item))
            else:
                res.append(f'<item>{xmlrepr(item)}</item>')
        return f"<list>{''.join(res)}</list>"
    return str(v)


class pset(dict):
    """This code is placed in the Public Domain, or released under the
       wtfpl (http://sam.zoy.org/wtfpl/COPYING) wherever PD is problematic.

       Property Set class.
       A property set is an object where values are attached to attributes,
       but can still be iterated over as key/value pairs.
       The order of assignment is maintained during iteration.
       Only one value allowed per key.

         >>> x = pset()
         >>> x.a = 42
         >>> x.b = 'foo'
         >>> x.a = 314
         >>> x
         pset(a=314, b='foo')

    """
    def __init__(self, items=(), **attrs):
        object.__setattr__(self, '_order', [])
        super().__init__()
        for k, v in self._get_iterator(items):
            self._add(k, v)
        for k, v in attrs.items():
            self._add(k, v)

    def __json__(self):
        return dict(self.items())

    def _add(self, key, value):
        "Add key->value to client vars."
        if type(key) in (int,):
            key = self._order[key]
        elif key not in self._order:
            self._order.append(key)
        dict.__setitem__(self, key, value)

    def apply(self, fn):
        "Apply function ``fn`` to all values in self."
        object.__setattr__(self, '_order', [])
        for k, v in self:
            self[k] = fn(v)

    def remove(self, key):
        "Remove key from client vars."
        if type(key) in (int,):
            key = self._order[key]
            del self._order[key]
        elif key in self._order:
            self._order.remove(key)
        dict.__delitem__(self, key)

    def __eq__(self, other):
        """Equal iff they have the same set of keys, and the values for
           each key is equal. Key order is not considered for equality.
        """
        if other is None:
            return False
        if set(self._order) == set(other._order):  # pylint: disable=W0212
            return all(self[key] == other[key] for key in self._order)
        return False

    def _get_iterator(self, val):
        if not val:
            return []
        if isinstance(val, pset) or not isinstance(val, dict):
            return val
        else:
            return val.items()

    def __iadd__(self, other):
        for k, v in self._get_iterator(other):
            self._add(k, v)
        return self

    def __add__(self, other):
        "self + other"
        tmp = self.__class__()
        tmp += self
        tmp += other
        return tmp

    def __radd__(self, other):
        "other + self"
        tmp = self.__class__()
        for k, v in other.items():
            tmp[k] = v
        tmp += self
        return tmp

    def __neg__(self):
        "Reverse keys and values."
        return self.__class__((v, k) for (k, v) in self.items())

    def _name(self):
        return self.name if 'name' in self else self.__class__.__name__

    def __xml__(self):
        res = [f'<{self._name()}>']
        res.extend(f'<{k}>{xmlrepr(v)}</{k}>' for k, v in self if k != 'name')
        res.append(f'</{self._name()}>')
        return ''.join(res)

    def __str__(self):
        vals = []
        for k, v in self:
            if k != 'name':
                try:
                    vals.append(f'{k}={repr(v)}')
                except Exception:
                    vals.append(f'{k}=UNPRINTABLE')

        vals = ', '.join(vals)

        return f'{self._name()}({vals})'

    __repr__ = __str__

    def pprint(self, indent=0, tab='   ', seen=None):
        "Pretty print the pset, indented."
        if seen is None:
            seen = [self]

        if indent == 0:
            print('{|')

        indent += 1

        for key in self.keys():
            print(tab * indent, key, '=',)
            val = self[key]
            if isinstance(val, pset):
                print('{|')
                if val in seen:
                    print(tab * (1 + indent), '...')
                    print(tab * indent, '|}')
                else:
                    val.pprint(indent, tab, seen)
            elif isinstance(val, list):
                print('[')
                for item in val:
                    if isinstance(item, pset):
                        print(tab * (indent + 1), '{|')
                        if item in seen:
                            print('...')
                        else:
                            item.pprint(indent + 1, tab)
                    else:
                        print(tab * (indent + 1), item)
                print(tab * indent, ']')
            else:
                print(val)

        indent -= 1
        print(tab * indent, '|}')

    def __getattr__(self, key):
        if not super().__contains__(key):
            raise AttributeError(key)
        return dict.get(self, key)

    def __getitem__(self, key):
        if type(key) in (int,):
            key = self._order[key]
        return dict.get(self, key)

    def __delattr__(self, key):
        if key in self:
            self.remove(key)

    def __delitem__(self, key):
        if key in self:
            self.remove(key)

    def __iter__(self):
        return ((k, dict.get(self, k)) for k in self._order)

    def items(self):
        return iter(self)

    def values(self):
        return [dict.get(self, k) for k in self._order]

    def keys(self):
        return self._order

    def __setattr__(self, key, val):
        # assert key not in self._reserved, key
        if key.startswith('_'):
            object.__setattr__(self, key, val)
        else:
            self._add(key, val)

    def __setitem__(self, key, val):
        self._add(key, val)

    def update(self, dct):
        """Update self from dct.
        """
        for k, v in dct.items():
            self._add(k, v)
        return self


class defset(pset):
    "pset with default value."
    def __init__(self, defval):
        object.__setattr__(self, '_defval', defval)
        super().__init__()

    def __getattr__(self, key):
        if key not in self:
            self[key] = self._defval()
        return dict.get(self, key)

    def __getitem__(self, key):
        if key not in self:
            self[key] = self._defval()
        return dict.get(self, key)

    def _add(self, key, value):
        if key not in self._order:
            self._order.append(key)
        dict.__setitem__(self, key, value)


class record(pset):  # pylint:disable=R0904
    """A property set with commit, rollback, and encoding translation.
    """
    @property
    def fields(self):
        "Verbose name of all fields."
        return [k.title() for k in self._order]

    def strvals(self, empty='', none='NULL', encoding='u8'):
        "Return a list of all values, formatted for human consumption."

        def cnvt(v):
            "Convert ``v`` to a human readable format."
            if v is None:
                res = none  # from outer scope parameters
            elif isinstance(v, str):
                res = v
            elif isinstance(v, bytes):
                res = v.decode(encoding)
            elif hasattr(v, 'strfmt'):
                if hasattr(v, 'minute'):
                    res = v.strfmt('%d.%m.%Y %H:%M')
                else:
                    res = v.strfmt('%d.%m.%Y')
            elif v == '':
                res = empty
            else:
                res = str(v)
            return res

        return [cnvt(self[f]) for f in self._order]

    def commit(self):
        "Copy current state to ``self._history``"

        self._history = pset()  # pylint:disable=W0201
        for f in self._order:
            self._history[f] = self[f]
        return self

    def rollback(self):
        "Copy snapshot from ``self._history`` into self."
        if not hasattr(self, '_history'):
            raise ValueError('Record has no history.')

        self.clear()  # dict.clear()
        del self._order[:]
        for k, v in self._history:
            self[k] = v

        return self

    def changed(self):
        "Return list of fields that have changed since last commit."
        if not hasattr(self, '_history'):
            raise ValueError('Record has no history.')

        return [k for k in self._order if self[k] != self._history[k]]

    def trans(self, source='iso-8859-1', dest='utf-8'):
        "Translate encoding."
        self.decode(source)
        self.encode(dest)
        return self

    def decode(self, encoding):
        "Decode using ``encoding``."
        def decodeval(v):
            "Helper function to decode value ``v``."
            return v.decode(encoding) if type(v) is bytes else v

        neworder = []
        for k in self._order:
            newval = decodeval(self.get(k))
            newkey = decodeval(k)
            neworder.append(newkey)
            dict.__delitem__(self, k)
            dict.__setitem__(self, newkey, newval)
        self._order = neworder
        return self

    def encode(self, encoding):
        "Encode using ``encoding``."
        def encodeval(v):
            "Helper function to encode value ``v``."
            return v.encode(encoding) if isinstance(v, str) else v

        neworder = []
        for k in self._order:
            newval = encodeval(self.get(k))
            newkey = encodeval(k)
            neworder.append(newkey)
            dict.__delitem__(self, k)
            dict.__setitem__(self, newkey, newval)
        self._order = neworder  # pylint:disable=W0201
        return self


def test_pset():
    """
       Unit tests...

       >>> request = pset(REQUEST={}, META={}, path='/', user=None, session={}, method='GET',
       ...                COOKIES={}, LANGUAGE_CODE='no')
       >>> p = page(request)
       >>> p.forms = 'fruit'
       >>> p.forms.foo = 'bar'
       >>> print p.forms.foo
       bar
       >>> p.forms.fob = 'baz'
       >>> print p.forms.fob
       baz
       >>> x = pset()
       >>> x.a
       Traceback (most recent call last):
         ...
       AttributeError: a
       >>> y = pset(a=1, b=2, c=3)
       >>> y.a
       1
       >>> y.b
       2
       >>> y.c
       3
       >>> z = pset()
       >>> z.a = 1
       >>> z.b = 2
       >>> z.c = 3
       >>> z[1]
       2
       >>> z
       pset(a=1, b=2, c=3)
       >>> class Point(pset): pass
       >>> p = Point(x=11, y=22)
       >>> p
       Point(y=22, x=11)

    """
    import doctest  # pylint:disable=W0404
    doctest.testmod()
