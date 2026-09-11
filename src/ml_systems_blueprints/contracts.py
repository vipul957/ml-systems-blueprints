def require_columns(record, required):
    """Validate the minimum fields at an inference boundary."""
    missing=sorted(set(required)-set(record))
    if missing: raise ValueError(f"missing required fields: {missing}")
    return True
