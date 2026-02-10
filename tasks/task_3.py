import re
from typing import Optional


def normalize_phone(phone_number: str, country_code: int = 38) -> Optional[str]:
    """Normalize a phone number to international format.

    Takes a phone number in various formats and normalizes it to
    international format: +[country_code][number] with only digits and
    leading plus sign.

    This function is designed primarily for Ukrainian phone numbers (country code 38).
    If the input number has a different country code, it will be replaced with
    the specified country_code parameter.

    Args:
        phone_number: The phone number to normalize.
        country_code: The country code to use (default: 38).
                      Should be a positive integer, without the '+' prefix.

    Returns:
        Normalized phone number in format +[country_code][digits], or None
        if validation fails.

    Validation:
        - phone_number must be a non-empty string
        - country_code must be a positive integer (not a boolean)
        - After cleaning, must have at least 10 digits (typical phone number length)

    Note:
        This function normalizes malformed phone numbers to a specific country format.
        It is NOT designed for converting between different countries' number systems.

        If the input has a different country code (e.g., +1), all digits are preserved
        and the specified country_code is prepended. For example:
        - normalize_phone("+15551234567", country_code=38) → "+3815551234567"

        This is intentional behavior for handling malformed inputs, not international conversion.

    """
    # Validate input types
    if not isinstance(phone_number, str):
        print(f"Error: phone_number must be a string, got {type(phone_number).__name__}.")
        return None

    if not isinstance(country_code, int) or isinstance(country_code, bool):
        print(f"Error: country_code must be an integer, got {type(country_code).__name__}.")
        return None

    # Validate country code value
    if country_code <= 0:
        print("Error: country_code must be a positive integer.")
        return None

    # Convert country_code to string for string operations
    country_code_str = str(country_code)

    # Strip whitespace
    phone = phone_number.strip()

    # Validate non-empty
    if not phone:
        print("Error: phone_number cannot be empty or whitespace-only.")
        return None

    # Add '+' prefix if not present
    if not phone.startswith("+"):
        phone = "+" + phone

    # Ensure country code is present
    # If phone doesn't start with the correct country code, replace/add it
    if not phone.startswith("+" + country_code_str):
        phone = "+" + country_code_str + phone[1:]

    # Remove ALL non-digit characters (including all '+' signs)
    digits_only = re.sub(r"\D", "", phone)

    # Validate minimum length (country code + typical phone number)
    # Typical phone number has at least 10 digits, plus country code
    if len(digits_only) < len(country_code_str) + 9:  # country code + at least 9 digits
        print(f"Error: Phone number too short. Expected at least {len(country_code_str) + 9} digits after '+', got {len(digits_only)}.")
        return None

    # Add single '+' prefix to the digits
    normalized = "+" + digits_only

    return normalized