import re
import socket
from typing import Any

def is_valid_email(email: str) -> bool:
    """Validates email string format using standard regex."""
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern, email))

def is_valid_ip(ip: str) -> bool:
    """Checks if a string is a valid IPv4 address."""
    try:
        socket.inet_aton(ip)
        return ip.count('.') == 3
    except (socket.error, AttributeError):
        return False

def is_not_empty(value: Any) -> bool:
    """Checks if a value is not None, empty string, list, or dict."""
    if value is None:
        return False
    if isinstance(value, (str, list, dict, set, tuple)):
        return len(value) > 0
    return True

def is_in_range(value: int, min_val: int, max_val: int) -> bool:
    """Checks if numeric value is within inclusive bounds."""
    return min_val <= value <= max_val

def is_alphanumeric(value: str) -> bool:
    """Validates that string contains only alphanumeric characters."""
    return value.isalnum()