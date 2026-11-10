from bisect import bisect_right


def resolve_version(versions, max_major, max_minor):
    if not versions:
        return None

    # Sort lexicographically: (major, minor) tuples follow natural version ordering.
    ordered = sorted((v[0], v[1]) for v in versions)

    # Index of the first version strictly greater than the ceiling.
    idx = bisect_right(ordered, (max_major, max_minor))

    if idx == 0:
        return None                 # every available version exceeds the ceiling

    major, minor = ordered[idx - 1]
    return [major, minor]