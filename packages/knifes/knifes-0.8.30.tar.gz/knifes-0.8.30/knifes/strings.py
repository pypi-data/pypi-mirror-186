def desensitizePhone(phone):
    """
    废弃
    """
    return '****'.join([phone[:3], phone[7:]])


# 手机号脱敏
def blur_phone(phone):
    if not phone or len(phone) < 11:
        return phone
    return phone[:3] + '****' + phone[7:]


def abbreviate(text, max_len=2, marker='...'):
    return text[0:max_len] + marker if len(text) > max_len else text


def ensure_str(bytes_or_str):
    """convert a byte or string object to unicode string.

    Useful when dealing with redis return values.

    """
    x = bytes_or_str
    return x if isinstance(x, str) else x.decode("utf-8")


def ensure_bytes(bytes_or_str):
    """convert a byte or string object to byte.

    """
    x = bytes_or_str
    return x.encode('utf-8') if isinstance(x, str) else x


class String(str):
    """str object to which attributes can be added

    """
    pass


def int_or_none(v, default=None):
    try:
        return int(v)
    except (ValueError, TypeError, OverflowError):
        return default
