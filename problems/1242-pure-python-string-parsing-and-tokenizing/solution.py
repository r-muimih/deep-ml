def parse_inventory(s):
    totals = {}
    for record in s.split(';'):
        record = record.strip()
        if not record:
            continue                      # empty record
        name, sep, qty = record.partition(':')
        name = name.strip()
        if not name:
            continue                      # empty name: ignore the record
        qty = qty.strip()
        value = int(qty) if qty else 0    # no ':' or empty quantity -> 0
        totals[name] = totals.get(name, 0) + value
    return [f"{name}={totals[name]}" for name in sorted(totals)]