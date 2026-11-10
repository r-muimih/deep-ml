def find_duplicates(records):
    # records: list of hashable items (ints or strings)
    # return a list of values that appear more than once,
    # each listed once, ordered by the position of its second occurrence
    seen = set()
    duplicates = []
    added = set()

    for item in records:
        if item in seen:
            if item not in added:
                duplicates.append(item)
                added.add(item)
        else:
            seen.add(item)

    return duplicates