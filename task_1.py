from datetime import datetime
from typing import Optional


def get_days_from_today(date: str) -> Optional[int]:
    """Calculate the difference in days between a given date and today.

    Compares only the date portion (ignoring time) of the input against
    today's date.

    Args:
        date: A date string in ISO 8601 format (``YYYY-MM-DD``).
              Time components (e.g. ``2025-01-15T14:30:00``) are accepted
              but ignored for the calculation.

    Returns:
        The number of days from today to *date*.
        Positive when *date* is in the future, negative when in the past,
        zero when *date* is today.
        Returns ``None`` if *date* cannot be parsed.

    """
    if not isinstance(date, str):
        print(f"Expected a string, got {type(date).__name__}.")
        return None

    if not date.strip():
        print("Date string is empty.")
        return None

    try:
        input_date = datetime.fromisoformat(date).date()
    except (ValueError, TypeError):
        print(
            "Cannot parse the date. "
            "Please use a valid ISO 8601 format: YYYY-MM-DD"
        )
        return None

    return (input_date - datetime.now().date()).days

