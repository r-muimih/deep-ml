import hashlib

def feature_hash(features, n_features):
    """
    Apply the (signed) feature hashing trick.

    Args:
        features: dict mapping feature name (str) -> value (float).
        n_features: int, size of the output vector.

    Returns:
        list of length n_features.
    """
    vec = [0.0] * n_features
    for name, value in features.items():
        digest = hashlib.md5(name.encode("utf-8")).digest()          # 16 bytes
        idx = int.from_bytes(digest[:4], "big") % n_features          # bucket  h(f)
        sign = 1 if int.from_bytes(digest[4:8], "big") % 2 == 0 else -1   # sign xi(f)
        vec[idx] += sign * value                                      # sum collisions
    return vec