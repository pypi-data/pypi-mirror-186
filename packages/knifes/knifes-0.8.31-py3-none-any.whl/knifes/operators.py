def safe_list_get(l_, *, idx=0, default=None):
    try:
        if not isinstance(l_, list):
            raise TypeError
        return l_[idx]
    except (IndexError, TypeError):
        return default

