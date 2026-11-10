class _TrieNode:
    __slots__ = ("children", "is_end")

    def __init__(self):
        self.children = {}
        self.is_end = False


def trie_operations(words, queries):
    root = _TrieNode()

    for w in words:
        node = root
        for ch in w:
            nxt = node.children.get(ch)
            if nxt is None:
                nxt = node.children[ch] = _TrieNode()
            node = nxt
        node.is_end = True

    def walk(s):
        node = root
        for ch in s:
            node = node.children.get(ch)
            if node is None:
                return None
        return node

    results = []
    for op, value in queries:
        node = walk(value)
        if op == "search":
            results.append(node is not None and node.is_end)
        elif op == "startsWith":
            # The empty prefix always matches; any other prefix matches
            # iff its full path exists in the trie.
            results.append(node is not None)
        else:
            raise ValueError("op must be 'search' or 'startsWith'")

    return results