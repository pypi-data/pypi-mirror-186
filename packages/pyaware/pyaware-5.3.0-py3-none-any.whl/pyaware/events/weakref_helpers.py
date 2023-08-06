import typing
from weakref import ref, WeakMethod


class _IterationGuard:
    # This context manager registers itself in the current iterators of the
    # weak container, such as to delay all removals until the context manager
    # exits.
    # This technique should be relatively thread-safe (since sets are).

    def __init__(self, weakcontainer):
        # Don't create cycles
        self.weakcontainer = ref(weakcontainer)

    def __enter__(self):
        w = self.weakcontainer()
        if w is not None:
            w._iterating.add(self)
        return self

    def __exit__(self, e, t, b):
        w = self.weakcontainer()
        if w is not None:
            s = w._iterating
            s.remove(self)
            if not s:
                w._commit_removals()


class WeakHandleDictionary:
    def __init__(self):
        self.data = {}
        self._pending_removals: set = set()
        self._iterating: set = set()

    def __setitem__(self, key: int, value: typing.Tuple[typing.Callable, bool]):
        handle, parse_topic = value
        try:
            self.data[key] = WeakMethod(handle), parse_topic
        except TypeError:
            self.data[key] = ref(handle), parse_topic

    def __getitem__(self, key):
        handle, parse_topic = self.data[key]
        if handle() is None:
            del self[key]
            raise KeyError(key)
        else:
            return handle(), parse_topic

    def __delitem__(self, key):
        if self._iterating:
            self._pending_removals.add(key)
        else:
            try:
                del self.data[key]
            except KeyError:
                pass

    def items(self):
        if self._pending_removals:
            self._commit_removals()
        with _IterationGuard(self):
            for k, v in self.data.items():
                try:
                    yield k, self[k]
                except KeyError:
                    continue

    def keys(self):
        if self._pending_removals:
            self._commit_removals()
        with _IterationGuard(self):
            for k in self.data.keys():
                try:
                    self[k]
                except KeyError:
                    continue
                yield k

    __iter__ = keys

    def values(self):
        if self._pending_removals:
            self._commit_removals()
        with _IterationGuard(self):
            for k, v in self.data.items():
                try:
                    v = self[k]
                except KeyError:
                    continue
                yield v

    def _commit_removals(self):
        for itm in self._pending_removals:
            del self[itm]

    def clear(self):
        self.data.clear()

    def __len__(self):
        return len(self.data)

    def __contains__(self, item):
        return item in self.data


def weak_ref(value: typing.Any):
    try:
        return WeakMethod(value)
    except TypeError:
        return ref(value)
