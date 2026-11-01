import numpy as np

def column_transformer(X, transformers):
    """
    Apply per-column-group transformations and horizontally concatenate the results.

    Args:
        X: 2D array-like of shape (n_samples, n_features)
        transformers: list of (name, kind, columns) tuples

    Returns:
        2D list of floats with transformed and concatenated columns.
    """
    X = np.asarray(X, dtype=float)
    if X.ndim == 1:
        X = X.reshape(-1, 1)

    blocks = []
    for name, kind, columns in transformers:
        if isinstance(columns, (int, np.integer)):          # allow a single index
            columns = [columns]
        cols = list(columns)
        kind_key = str(kind).lower().replace("-", "_").replace(" ", "_")

        if kind_key == "drop":                               # contributes no columns
            continue

        block = X[:, cols]
        if kind_key in ("standard", "standard_scaler", "standardize", "zscore", "z_score"):
            mean = block.mean(axis=0)
            std = block.std(axis=0)                          # population std (ddof=0)
            safe = np.where(std == 0, 1.0, std)
            block = np.where(std == 0, 0.0, (block - mean) / safe)
        elif kind_key in ("minmax", "min_max", "minmax_scaler", "min_max_scaler"):
            mn = block.min(axis=0)
            rng = block.max(axis=0) - mn
            safe = np.where(rng == 0, 1.0, rng)
            block = np.where(rng == 0, 0.0, (block - mn) / safe)
        elif kind_key in ("passthrough", "pass", "identity"):
            pass                                             # keep the block untouched
        else:
            raise ValueError(f"unknown transformer kind: {kind!r}")

        blocks.append(block)

    if not blocks:                                           # everything was dropped
        return [[] for _ in range(X.shape[0])]
    return np.hstack(blocks).tolist()
