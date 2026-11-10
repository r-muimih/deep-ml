def hash_table_operations(operations):
    class HashTable:
        def __init__(self, capacity=8, max_load=0.75):
            self.capacity = capacity
            self.max_load = max_load
            self.size = 0
            self.buckets = [[] for _ in range(capacity)]

        @staticmethod
        def _hash(key):
            # Polynomial rolling hash (djb2-style), computed manually
            h = 5381
            for ch in key:
                h = (h * 33 + ord(ch)) & 0xFFFFFFFFFFFFFFFF
            return h

        def _index(self, key):
            return self._hash(key) % self.capacity

        def _resize(self):
            old = self.buckets
            self.capacity *= 2
            self.buckets = [[] for _ in range(self.capacity)]
            for bucket in old:
                for k, v in bucket:
                    self.buckets[self._index(k)].append([k, v])

        def put(self, key, value):
            bucket = self.buckets[self._index(key)]
            for pair in bucket:
                if pair[0] == key:
                    pair[1] = value
                    return
            bucket.append([key, value])
            self.size += 1
            if self.size / self.capacity > self.max_load:
                self._resize()

        def get(self, key):
            for k, v in self.buckets[self._index(key)]:
                if k == key:
                    return v
            return None

        def delete(self, key):
            bucket = self.buckets[self._index(key)]
            for i, (k, _) in enumerate(bucket):
                if k == key:
                    bucket.pop(i)
                    self.size -= 1
                    return True
            return False

    table = HashTable()
    results = []
    for op in operations:
        cmd = op[0]
        if cmd == "put":
            table.put(op[1], op[2])
        elif cmd == "get":
            results.append(table.get(op[1]))
        elif cmd == "delete":
            results.append(table.delete(op[1]))
    return results