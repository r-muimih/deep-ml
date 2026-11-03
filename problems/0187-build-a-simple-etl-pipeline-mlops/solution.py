def run_etl(csv_text: str) -> list[tuple[str, float]]:
    """Run a simple ETL pipeline over CSV text with header user_id,event_type,value.

    Returns a sorted list of (user_id, total_value) for event_type == "purchase".
    """
    # --- Extract ---
    lines = [line.strip() for line in csv_text.splitlines()]
    lines = [line for line in lines if line]  # drop blank lines

    if not lines:
        return []

    header = [col.strip() for col in lines[0].split(",")]
    expected = ["user_id", "event_type", "value"]
    if header != expected:
        raise ValueError(f"Unexpected header {header}, expected {expected}")

    rows = []
    for line in lines[1:]:
        fields = line.split(",")
        if len(fields) != 3:
            continue  # malformed row, skip
        user_id, event_type, value = (f.strip() for f in fields)
        rows.append((user_id, event_type, value))

    # --- Transform ---
    totals: dict[str, float] = {}
    for user_id, event_type, raw_value in rows:
        if event_type != "purchase":
            continue
        if not user_id:
            continue
        try:
            value = float(raw_value)
        except ValueError:
            continue  # invalid value, drop row

        totals[user_id] = totals.get(user_id, 0.0) + value

    # --- Load ---
    return sorted(totals.items(), key=lambda pair: pair[0])