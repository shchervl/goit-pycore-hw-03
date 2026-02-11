from datetime import datetime, timedelta, date
from typing import List, Dict, Optional


def _validate_value(variable_name: str, value, expected_type=None) -> bool:
    """Validate a field's type and truthiness.

    Args:
        variable_name: Name of the field (for error messages)
        value: Value to validate
        expected_type: Expected type of the value (e.g., str, dict, list)

    Returns:
        True if valid (correct type and truthy), False otherwise
    """
    # Check type if specified
    if expected_type is not None:
        if not isinstance(value, expected_type):
            print(
                f"Error: {variable_name} must be a {expected_type.__name__}, "
                f"got {type(value).__name__}."
            )
            return False

    # Check if value is truthy (not None, not empty, not whitespace-only string)
    if not value:
        print(f"Error: {variable_name} cannot be empty or None.")
        return False

    # For strings, check if not just whitespace
    if isinstance(value, str) and not value.strip():
        print(f"Error: {variable_name} cannot be empty or whitespace.")
        return False

    return True


def _parse_birthday(birthday_str) -> Optional[date]:
    """Parse and validate birthday string.

    Args:
        birthday_str: Birthday string to parse

    Returns:
        date object if valid, None otherwise
    """
    if not _validate_value("birthday", birthday_str, str):
        print(f"Error: birthday must be a string, got {type(birthday_str).__name__}.")
        return None

    try:
        return datetime.strptime(birthday_str, "%Y.%m.%d").date()
    except ValueError:
        print(
            f"Error: Invalid birthday format '{birthday_str}'. Expected 'YYYY.MM.DD'."
        )
        return None


def get_upcoming_birthdays(users: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """Get list of users with upcoming birthdays in the next 7 days.

    This function identifies colleagues who have birthdays within the next 7 days
    (including today) and determines when to congratulate them. If a birthday
    falls on a weekend (Saturday or Sunday), the congratulation date is moved
    to the following Monday.

    Args:
        users: List of user dictionaries. Each dictionary must contain:
               - 'name': User's name (str)
               - 'birthday': Birth date in format 'YYYY.MM.DD' (str)

    Returns:
        List of dictionaries with congratulation information. Each contains:
        - 'name': User's name (str)
        - 'congratulation_date': Date to congratulate in format 'YYYY.MM.DD' (str)

        Returns empty list for invalid inputs or if no birthdays in range.

    Validations:
        - users must be a list
        - Each user must be a dict with 'name' and 'birthday' keys
        - Birthday must be in valid 'YYYY.MM.DD' format
        - Name must be a non-empty string

    Weekend Handling:
        - Weekday birthdays → congratulate on actual birthday
        - Saturday birthdays → congratulate on Monday
        - Sunday birthdays → congratulate on Monday

    Leap Year Handling:
        - Feb 29 birthdays in non-leap years → moved to March 1
        - This ensures people born on Feb 29 are still included

    """
    upcoming_birthdays = []

    # Validate input type
    if not _validate_value("users", users, list):
        return upcoming_birthdays

    # Empty list is valid
    if not users:
        return upcoming_birthdays

    today = datetime.today().date()

    for user in users:
        # Validate user is a dict
        if not _validate_value("user", user, dict):
            continue

        # Check required keys
        if "name" not in user or "birthday" not in user:
            print("Error: user dict must have 'name' and 'birthday' keys.")
            continue

        name = user["name"]
        birthday_str = user["birthday"]

        # Validate name is non-empty string
        if not _validate_value("name", name, str):
            continue

        # Parse and validate birthday
        birthday = _parse_birthday(birthday_str)
        if not birthday:
            continue

        # Calculate birthday for this year
        try:
            birthday_this_year = birthday.replace(year=today.year)
        except ValueError:
            # Handle Feb 29 in non-leap years - move to March 1
            birthday_this_year = date(today.year, 3, 1)

        # If birthday already passed this year, use next year
        if birthday_this_year < today:
            try:
                birthday_this_year = birthday.replace(year=today.year + 1)
            except ValueError:
                # Handle Feb 29 in non-leap years for next year - move to March 1
                birthday_this_year = date(today.year + 1, 3, 1)

        # Calculate days until birthday
        days_until_birthday = (birthday_this_year - today).days

        # Check if birthday is within next 7 days
        if 0 <= days_until_birthday <= 6:

            # Check if birthday falls on weekend
            weekday = birthday_this_year.weekday()
            if weekday == 5:  # Saturday
                birthday_this_year += timedelta(days=2)  # Move to Monday
            elif weekday == 6:  # Sunday
                birthday_this_year += timedelta(days=1)  # Move to Monday

            # Format date as string
            congratulation_date_str = birthday_this_year.strftime("%Y.%m.%d")

            upcoming_birthdays.append(
                {"name": name, "congratulation_date": congratulation_date_str}
            )

    return upcoming_birthdays
