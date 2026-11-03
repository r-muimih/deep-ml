def calculate_data_quality_score(data: list, schema: dict) -> dict:
    """
    Calculate data quality metrics for ML pipeline monitoring.

    Args:
        data: list of dictionaries representing rows of data
        schema: dictionary defining expected columns and their types
                {'column_name': {'type': 'numeric'|'categorical'|'boolean', 'nullable': True|False}}

    Returns:
        dict with keys: 'completeness', 'type_validity', 'uniqueness_ratio', 'overall_score'
        All values as percentages (0-100), rounded to 2 decimal places.
    """
    if not data:
        return {}

    n_records = len(data)
    fields = list(schema.keys())
    n_expected = n_records * len(fields) if fields else 0

    # --- Completeness: % of non-null values across all expected fields ---
    non_null_count = 0
    for record in data:
        for field in fields:
            value = record.get(field)  # missing field treated as None
            if value is not None:
                non_null_count += 1

    completeness = (non_null_count / n_expected * 100) if n_expected else 0.0

    # --- Type Validity: % of values matching expected type (null-aware) ---
    def is_type_valid(value, field_type, nullable):
        if value is None:
            return nullable  # null counts valid only if field is nullable

        if field_type == "numeric":
            # bool is a subclass of int in Python, so exclude it explicitly
            return isinstance(value, (int, float)) and not isinstance(value, bool)
        elif field_type == "categorical":
            return isinstance(value, str)
        elif field_type == "boolean":
            return isinstance(value, bool)
        else:
            return False  # unknown type spec: treat as invalid

    valid_count = 0
    for record in data:
        for field in fields:
            spec = schema[field]
            value = record.get(field)
            if is_type_valid(value, spec.get("type"), spec.get("nullable", False)):
                valid_count += 1

    type_validity = (valid_count / n_expected * 100) if n_expected else 0.0

    # --- Uniqueness Ratio: % of unique records in the dataset ---
    def record_signature(record):
        # Hashable representation; only considers schema fields so extra
        # keys in a record don't affect uniqueness comparison.
        return tuple(sorted((field, record.get(field)) for field in fields))

    if fields:
        signatures = {record_signature(r) for r in data}
    else:
        # No schema fields: fall back to comparing whole records
        signatures = {tuple(sorted(r.items())) for r in data}

    uniqueness_ratio = (len(signatures) / n_records * 100) if n_records else 0.0

    # --- Overall Score: weighted combination ---
    overall_score = 0.4 * completeness + 0.4 * type_validity + 0.2 * uniqueness_ratio

    return {
        "completeness": round(completeness, 2),
        "type_validity": round(type_validity, 2),
        "uniqueness_ratio": round(uniqueness_ratio, 2),
        "overall_score": round(overall_score, 2),
    }