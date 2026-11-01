import numpy as np
from collections import Counter

def dummy_classifier(y_train, n_test, strategy, constant=None):
    """
    Produce baseline predictions of length n_test using the given strategy.
    Returns a Python list of predicted labels.
    """
    labels = y_train.tolist() if hasattr(y_train, "tolist") else list(y_train)

    if strategy == "constant":
        if constant is None:
            raise ValueError("strategy='constant' requires a constant label")
        return [constant] * n_test
    if not labels:
        raise ValueError("y_train must not be empty")

    counts = Counter(labels)
    classes = sorted(counts)                      # sorted unique labels
    n = len(labels)

    if strategy == "most_frequent":
        top = max(counts.values())
        mode = min(c for c in classes if counts[c] == top)       # ties -> smallest label
        return [mode] * n_test

    if strategy == "uniform":
        k = len(classes)
        return [classes[i % k] for i in range(n_test)]           # cycle through sorted classes

    if strategy == "stratified":
        base = {c: (n_test * counts[c]) // n for c in classes}        # floor(m * f_c)
        remainder = {c: (n_test * counts[c]) % n for c in classes}    # fractional part * n
        leftover = n_test - sum(base.values())
        order = sorted(classes, key=lambda c: (-remainder[c], classes.index(c)))
        for c in order[:leftover]:                                    # largest remainders first
            base[c] += 1
        preds = []
        for c in classes:
            preds.extend([c] * base[c])
        return preds

    raise ValueError(f"unknown strategy: {strategy!r}")