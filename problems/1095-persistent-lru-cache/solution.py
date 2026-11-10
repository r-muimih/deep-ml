# Cell 1
from collections import OrderedDict


def lru_cache_operations(capacity, ops):
    class PersistentLRU:
        def __init__(self, capacity):
            self.capacity = capacity
            self.cache = OrderedDict()   # volatile: lost on crash
            self.journal = []            # durable: survives crash
            self.compact_at = 4 * capacity + 16

        # The only place state changes; used by live ops and by replay.
        @staticmethod
        def _apply(cache, capacity, entry):
            kind, key, value = entry
            if kind == "put":
                if key in cache:
                    cache[key] = value
                cache[key] = value
                cache.move_to_end(key)
                if len(cache) > capacity:
                    cache.popitem(last=False)
            else:  # "touch": a get hit refreshes recency
                cache.move_to_end(key)

        def put(self, key, value):
            entry = ("put", key, value)
            self.journal.append(entry)           # log first (write-ahead)
            self._apply(self.cache, self.capacity, entry)
            self._maybe_compact()

        def get(self, key):
            if key not in self.cache:
                return -1                        # a miss changes nothing
            self.journal.append(("touch", key, None))
            self.cache.move_to_end(key)
            self._maybe_compact()
            return self.cache[key]

        def _maybe_compact(self):
            if len(self.journal) > self.compact_at:
                # Snapshot: puts in LRU -> MRU order reproduce the same state
                self.journal = [("put", k, v) for k, v in self.cache.items()]

        def crash(self):
            self.cache = OrderedDict()           # memory is gone
            for entry in self.journal:           # recover from durable log
                self._apply(self.cache, self.capacity, entry)

    lru = PersistentLRU(capacity)
    results = []
    for op in ops:
        cmd = op[0]
        if cmd == "put":
            lru.put(op[1], op[2])
        elif cmd == "get":
            results.append(lru.get(op[1]))
        elif cmd == "crash":
            lru.crash()
    return results