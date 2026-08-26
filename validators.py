import re
from typing import Any, Dict, List

# Reorganized validators for better maintainability and readability

def validate_email(email: str) -> bool:
    """Validate basic email address format."""
    if not isinstance(email, str) or not email.strip():
        return False
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))

def validate_url(url: str) -> bool:
    """Validate simple URL starting with http or https."""
    if not isinstance(url, str) or not url.strip():
        return False
    pattern = r"^https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(/[^\s]*)?$"
    return bool(re.match(pattern, url))

def validate_phone(phone: str) -> bool:
    """Validate phone number by digit count after cleaning."""
    if not isinstance(phone, str):
        return False
    cleaned = re.sub(r"\D", "", phone)
    return 10 <= len(cleaned) <= 15

def validate_positive_int(value: Any) -> bool:
    """Check for positive integer value."""
    return isinstance(value, int) and value > 0

def validate_required_dict(data: Dict[str, Any], keys: List[str]) -> bool:
    """Ensure dictionary has all specified keys."""
    if not isinstance(data, dict):
        return False
    return all(k in data for k in keys)

class Validators:
    """Class wrapper for organized access to validators."""
    
    def __init__(self) -> None:
        pass

    @staticmethod
    def email(email: str) -> bool:
        return validate_email(email)

    @staticmethod
    def url(url: str) -> bool:
        return validate_url(url)

    @staticmethod
    def phone(phone: str) -> bool:
        return validate_phone(phone)

    @staticmethod
    def positive_int(value: Any) -> bool:
        return validate_positive_int(value)

    @staticmethod
    def required_dict(data: Dict[str, Any], keys: List[str]) -> bool:
        return validate_required_dict(data, keys)
