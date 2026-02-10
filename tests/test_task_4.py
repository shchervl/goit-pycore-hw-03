"""
Comprehensive test suite for get_upcoming_birthdays function.

Test Coverage:
- Boundary values (today, 6 days from now, 7 days from now)
- Negative scenarios (invalid types, formats, missing keys)
- Weekend handling (Saturday and Sunday birthdays)
- Year transitions (birthdays already passed this year)
- Edge cases (leap years, empty lists, multiple users)
"""

from datetime import datetime, timedelta

import pytest
from tasks.task_4 import get_upcoming_birthdays, _validate_value


class TestGetUpcomingBirthdays:
    """Test suite for get_upcoming_birthdays function."""

    # ==================== HELPER METHODS ====================

    def get_date_in_days(self, days: int) -> str:
        """Get date N days from today in YYYY.MM.DD format."""
        target_date = datetime.today().date() + timedelta(days=days)
        return target_date.strftime("%Y.%m.%d")

    def get_birthday_for_days_ahead(self, days: int, birth_year: int = 1990) -> str:
        """Get birthday string that will occur N days from today."""
        target_date = datetime.today().date() + timedelta(days=days)
        return f"{birth_year}.{target_date.month:02d}.{target_date.day:02d}"

    def get_next_monday_in_days(self, days: int) -> int:
        """Calculate days until next Monday from a date N days ahead."""
        target_date = datetime.today().date() + timedelta(days=days)
        weekday = target_date.weekday()

        if weekday == 5:  # Saturday
            return days + 2
        elif weekday == 6:  # Sunday
            return days + 1
        return days

    # ==================== BOUNDARY VALUES ====================

    def test_birthday_today(self):
        """Birthday today should be in the list."""
        today_birthday = self.get_birthday_for_days_ahead(0)
        users = [{"name": "John Doe", "birthday": today_birthday}]

        result = get_upcoming_birthdays(users)

        assert len(result) == 1
        assert result[0]['name'] == "John Doe"
        # Could be moved to Monday if today is weekend
        expected_days = self.get_next_monday_in_days(0)
        expected_date = self.get_date_in_days(expected_days)
        assert result[0]['congratulation_date'] == expected_date

    def test_birthday_tomorrow(self):
        """Birthday tomorrow should be in the list."""
        tomorrow_birthday = self.get_birthday_for_days_ahead(1)
        users = [{"name": "Jane Smith", "birthday": tomorrow_birthday}]

        result = get_upcoming_birthdays(users)

        assert len(result) == 1
        assert result[0]['name'] == "Jane Smith"
        expected_days = self.get_next_monday_in_days(1)
        expected_date = self.get_date_in_days(expected_days)
        assert result[0]['congratulation_date'] == expected_date

    def test_birthday_6_days_from_now(self):
        """Birthday 6 days from now (last valid day) should be in the list."""
        future_birthday = self.get_birthday_for_days_ahead(6)
        users = [{"name": "Bob Wilson", "birthday": future_birthday}]

        result = get_upcoming_birthdays(users)

        assert len(result) == 1
        expected_days = self.get_next_monday_in_days(6)
        expected_date = self.get_date_in_days(expected_days)
        assert result[0]['congratulation_date'] == expected_date

    def test_birthday_7_days_from_now(self):
        """Birthday 7 days from now (outside range) should NOT be in the list."""
        future_birthday = self.get_birthday_for_days_ahead(7)
        users = [{"name": "Alice Brown", "birthday": future_birthday}]

        result = get_upcoming_birthdays(users)

        assert len(result) == 0

    def test_birthday_8_days_from_now(self):
        """Birthday 8 days from now (outside range) should NOT be in the list."""
        future_birthday = self.get_birthday_for_days_ahead(8)
        users = [{"name": "Charlie Davis", "birthday": future_birthday}]

        result = get_upcoming_birthdays(users)

        assert len(result) == 0

    def test_birthday_yesterday(self):
        """Birthday yesterday should NOT be in the list (already passed)."""
        yesterday_birthday = self.get_birthday_for_days_ahead(-1)
        users = [{"name": "David Clark", "birthday": yesterday_birthday}]

        result = get_upcoming_birthdays(users)

        assert len(result) == 0

    # ==================== WEEKEND HANDLING ====================

    def test_saturday_birthday_moves_to_monday(self):
        """Saturday birthday should move to Monday."""
        today = datetime.today().date()

        # Find next Saturday
        days_until_saturday = (5 - today.weekday()) % 7
        if days_until_saturday == 0:  # Today is Saturday
            days_until_saturday = 0

        # Only test if Saturday is within next 6 days
        if 0 <= days_until_saturday <= 6:
            saturday_birthday = self.get_birthday_for_days_ahead(days_until_saturday)
            users = [{"name": "Saturday Person", "birthday": saturday_birthday}]

            result = get_upcoming_birthdays(users)

            assert len(result) == 1
            # Should be moved to Monday (+2 days)
            expected_date = self.get_date_in_days(days_until_saturday + 2)
            assert result[0]['congratulation_date'] == expected_date

    def test_sunday_birthday_moves_to_monday(self):
        """Sunday birthday should move to Monday."""
        today = datetime.today().date()

        # Find next Sunday
        days_until_sunday = (6 - today.weekday()) % 7
        if days_until_sunday == 0:  # Today is Sunday
            days_until_sunday = 0

        # Only test if Sunday is within next 6 days
        if 0 <= days_until_sunday <= 6:
            sunday_birthday = self.get_birthday_for_days_ahead(days_until_sunday)
            users = [{"name": "Sunday Person", "birthday": sunday_birthday}]

            result = get_upcoming_birthdays(users)

            assert len(result) == 1
            # Should be moved to Monday (+1 day)
            expected_date = self.get_date_in_days(days_until_sunday + 1)
            assert result[0]['congratulation_date'] == expected_date

    def test_weekday_birthday_not_moved(self):
        """Weekday birthday should not be moved."""
        today = datetime.today().date()

        # Find next weekday (Mon-Fri)
        for days_ahead in range(7):
            target_date = today + timedelta(days=days_ahead)
            if target_date.weekday() < 5:  # Monday to Friday
                weekday_birthday = self.get_birthday_for_days_ahead(days_ahead)
                users = [{"name": "Weekday Person", "birthday": weekday_birthday}]

                result = get_upcoming_birthdays(users)

                assert len(result) == 1
                # Should not be moved
                expected_date = self.get_date_in_days(days_ahead)
                assert result[0]['congratulation_date'] == expected_date
                break

    # ==================== MULTIPLE USERS ====================

    def test_multiple_users_all_in_range(self):
        """Multiple users with birthdays in range should all be returned."""
        users = [
            {"name": "User1", "birthday": self.get_birthday_for_days_ahead(0)},
            {"name": "User2", "birthday": self.get_birthday_for_days_ahead(3)},
            {"name": "User3", "birthday": self.get_birthday_for_days_ahead(6)},
        ]

        result = get_upcoming_birthdays(users)

        assert len(result) == 3
        names = [r['name'] for r in result]
        assert "User1" in names
        assert "User2" in names
        assert "User3" in names

    def test_multiple_users_mixed_range(self):
        """Only users with birthdays in range should be returned."""
        users = [
            {"name": "InRange1", "birthday": self.get_birthday_for_days_ahead(2)},
            {"name": "OutOfRange", "birthday": self.get_birthday_for_days_ahead(8)},
            {"name": "InRange2", "birthday": self.get_birthday_for_days_ahead(5)},
        ]

        result = get_upcoming_birthdays(users)

        assert len(result) == 2
        names = [r['name'] for r in result]
        assert "InRange1" in names
        assert "InRange2" in names
        assert "OutOfRange" not in names

    def test_no_users_in_range(self):
        """No users with birthdays in range should return empty list."""
        users = [
            {"name": "Future1", "birthday": self.get_birthday_for_days_ahead(10)},
            {"name": "Future2", "birthday": self.get_birthday_for_days_ahead(20)},
        ]

        result = get_upcoming_birthdays(users)

        assert len(result) == 0

    # ==================== EMPTY AND EDGE CASES ====================

    def test_empty_list(self):
        """Empty user list should return empty list."""
        result = get_upcoming_birthdays([])
        assert result == []

    def test_duplicate_names(self):
        """Users with duplicate names should all be returned."""
        birthday = self.get_birthday_for_days_ahead(3)
        users = [
            {"name": "John Doe", "birthday": birthday},
            {"name": "John Doe", "birthday": birthday},
        ]

        result = get_upcoming_birthdays(users)

        assert len(result) == 2
        assert all(r['name'] == "John Doe" for r in result)

    def test_same_birthday_different_users(self):
        """Multiple users with same birthday should all be returned."""
        birthday = self.get_birthday_for_days_ahead(4)
        users = [
            {"name": "Alice", "birthday": birthday},
            {"name": "Bob", "birthday": birthday},
            {"name": "Charlie", "birthday": birthday},
        ]

        result = get_upcoming_birthdays(users)

        assert len(result) == 3
        names = [r['name'] for r in result]
        assert set(names) == {"Alice", "Bob", "Charlie"}

    # ==================== NEGATIVE SCENARIOS: INVALID TYPES ====================

    def test_users_not_list(self):
        """Non-list input should return empty list."""
        result = get_upcoming_birthdays("not a list")
        assert result == []

    def test_users_none(self):
        """None input should return empty list."""
        result = get_upcoming_birthdays(None)
        assert result == []

    def test_users_dict(self):
        """Dictionary input should return empty list."""
        result = get_upcoming_birthdays({"name": "John", "birthday": "1990.01.01"})
        assert result == []

    def test_user_not_dict(self):
        """Non-dict user should be skipped."""
        birthday = self.get_birthday_for_days_ahead(2)
        users = [
            {"name": "Valid", "birthday": birthday},
            "invalid user",
            {"name": "Also Valid", "birthday": birthday},
        ]

        result = get_upcoming_birthdays(users)

        assert len(result) == 2
        names = [r['name'] for r in result]
        assert "Valid" in names
        assert "Also Valid" in names

    def test_name_not_string(self):
        """Non-string name should be skipped."""
        birthday = self.get_birthday_for_days_ahead(2)
        users = [
            {"name": 123, "birthday": birthday},
            {"name": "Valid", "birthday": birthday},
        ]

        result = get_upcoming_birthdays(users)

        assert len(result) == 1
        assert result[0]['name'] == "Valid"

    def test_birthday_not_string(self):
        """Non-string birthday should be skipped."""
        users = [
            {"name": "Invalid", "birthday": 20240101},
            {"name": "Valid", "birthday": self.get_birthday_for_days_ahead(2)},
        ]

        result = get_upcoming_birthdays(users)

        assert len(result) == 1
        assert result[0]['name'] == "Valid"

    def test_name_none(self):
        """User with None as name should be skipped."""
        birthday = self.get_birthday_for_days_ahead(2)
        users = [
            {"name": None, "birthday": birthday},
            {"name": "Valid", "birthday": birthday},
        ]

        result = get_upcoming_birthdays(users)

        assert len(result) == 1
        assert result[0]['name'] == "Valid"

    def test_birthday_none(self):
        """User with None as birthday should be skipped."""
        birthday = self.get_birthday_for_days_ahead(2)
        users = [
            {"name": "Invalid", "birthday": None},
            {"name": "Valid", "birthday": birthday},
        ]

        result = get_upcoming_birthdays(users)

        assert len(result) == 1
        assert result[0]['name'] == "Valid"

    # ==================== NEGATIVE SCENARIOS: MISSING KEYS ====================

    def test_missing_name_key(self):
        """User without 'name' key should be skipped."""
        birthday = self.get_birthday_for_days_ahead(2)
        users = [
            {"birthday": birthday},
            {"name": "Valid", "birthday": birthday},
        ]

        result = get_upcoming_birthdays(users)

        assert len(result) == 1
        assert result[0]['name'] == "Valid"

    def test_missing_birthday_key(self):
        """User without 'birthday' key should be skipped."""
        birthday = self.get_birthday_for_days_ahead(2)
        users = [
            {"name": "Invalid"},
            {"name": "Valid", "birthday": birthday},
        ]

        result = get_upcoming_birthdays(users)

        assert len(result) == 1
        assert result[0]['name'] == "Valid"

    def test_empty_name(self):
        """User with empty name should be skipped."""
        birthday = self.get_birthday_for_days_ahead(2)
        users = [
            {"name": "", "birthday": birthday},
            {"name": "Valid", "birthday": birthday},
        ]

        result = get_upcoming_birthdays(users)

        assert len(result) == 1
        assert result[0]['name'] == "Valid"

    def test_whitespace_only_name(self):
        """User with whitespace-only name should be skipped."""
        birthday = self.get_birthday_for_days_ahead(2)
        users = [
            {"name": "   ", "birthday": birthday},
            {"name": "Valid", "birthday": birthday},
        ]

        result = get_upcoming_birthdays(users)

        assert len(result) == 1
        assert result[0]['name'] == "Valid"

    # ==================== NEGATIVE SCENARIOS: INVALID FORMATS ====================

    def test_invalid_date_format_dashes(self):
        """Birthday with dashes (YYYY-MM-DD) should be skipped."""
        users = [
            {"name": "Invalid", "birthday": "1990-01-15"},
            {"name": "Valid", "birthday": self.get_birthday_for_days_ahead(2)},
        ]

        result = get_upcoming_birthdays(users)

        assert len(result) == 1
        assert result[0]['name'] == "Valid"

    def test_invalid_date_format_slashes(self):
        """Birthday with slashes (DD/MM/YYYY) should be skipped."""
        users = [
            {"name": "Invalid", "birthday": "15/01/1990"},
            {"name": "Valid", "birthday": self.get_birthday_for_days_ahead(2)},
        ]

        result = get_upcoming_birthdays(users)

        assert len(result) == 1
        assert result[0]['name'] == "Valid"

    def test_invalid_date_nonexistent(self):
        """Nonexistent date should be skipped."""
        users = [
            {"name": "Invalid", "birthday": "1990.02.30"},  # Feb 30 doesn't exist
            {"name": "Valid", "birthday": self.get_birthday_for_days_ahead(2)},
        ]

        result = get_upcoming_birthdays(users)

        assert len(result) == 1
        assert result[0]['name'] == "Valid"

    def test_invalid_date_format_short(self):
        """Short date format should be skipped."""
        users = [
            {"name": "Invalid", "birthday": "90.1.15"},
            {"name": "Valid", "birthday": self.get_birthday_for_days_ahead(2)},
        ]

        result = get_upcoming_birthdays(users)

        assert len(result) == 1
        assert result[0]['name'] == "Valid"

    # ==================== YEAR TRANSITIONS ====================

    def test_leap_year_feb_29_in_non_leap_year(self):
        """Feb 29 birthday in non-leap year should be skipped."""
        users = [
            {"name": "Leap Day", "birthday": "2000.02.29"},
            {"name": "Valid", "birthday": self.get_birthday_for_days_ahead(2)},
        ]

        # Will either skip Feb 29 or handle it depending on whether current year is leap
        result = get_upcoming_birthdays(users)

        # Valid user should always be in results
        names = [r['name'] for r in result]
        assert "Valid" in names


# ==================== PARAMETRIZED TESTS ====================

class TestParametrizedScenarios:
    """Parametrized tests for comprehensive coverage."""

    @pytest.mark.parametrize("invalid_input", [
        None,
        "string",
        123,
        12.34,
        {"key": "value"},
        True,
        False,
    ])
    def test_invalid_users_types(self, invalid_input):
        """Various invalid types for users parameter should return empty list."""
        result = get_upcoming_birthdays(invalid_input)
        assert result == []

    @pytest.mark.parametrize("invalid_format", [
        "1990-01-15",  # Dashes
        "15/01/1990",  # Slashes
        "01.15.1990",  # MM.DD.YYYY
        "15.01.90",    # Short year
        "1990.1.15",   # No leading zeros
        "invalid",     # Text
        "2024.13.01",  # Invalid month
        "2024.00.15",  # Invalid month
        "2024.01.32",  # Invalid day
        "2024.02.30",  # Nonexistent date
    ])
    def test_invalid_birthday_formats(self, invalid_format):
        """Various invalid birthday formats should be skipped."""
        # Get a valid birthday for comparison
        today = datetime.today().date()
        valid_date = today + timedelta(days=2)
        valid_birthday = valid_date.strftime("%Y.%m.%d")
        valid_birthday_parts = valid_birthday.split(".")
        valid_birthday_this_year = f"1990.{valid_birthday_parts[1]}.{valid_birthday_parts[2]}"

        users = [
            {"name": "Invalid", "birthday": invalid_format},
            {"name": "Valid", "birthday": valid_birthday_this_year},
        ]

        result = get_upcoming_birthdays(users)

        # Only valid user should be in results
        names = [r['name'] for r in result]
        assert "Invalid" not in names
        assert "Valid" in names

# ==================== UNIT TESTS FOR HELPER FUNCTIONS ====================

class TestValidateFieldHelper:
    """Unit tests for _validate_field helper function."""

    def test_validate_field_type_checking(self):
        """Test type validation."""
        # Valid type and truthy
        result = _validate_value('field', "test", str)
        assert result is True

        # Invalid type
        result = _validate_value('field', 123, str)
        assert result is False

    def test_validate_field_string_empty_check(self):
        """Test string emptiness validation (automatic)."""
        # Empty string - fails truthiness check
        result = _validate_value('name', "", str)
        assert result is False

        # Whitespace only - fails whitespace check
        result = _validate_value('name', "   ", str)
        assert result is False

        # Valid non-empty string
        result = _validate_value('name', "John", str)
        assert result is True

    def test_validate_field_none_value(self):
        """Test validation with None value."""
        # None with type check
        result = _validate_value('field', None, str)
        assert result is False

        # None without type check - fails truthiness
        result = _validate_value('field', None)
        assert result is False

    def test_validate_field_empty_collections(self):
        """Test validation with empty collections."""
        # Empty list - fails truthiness
        result = _validate_value('field', [], list)
        assert result is False

        # Empty dict - fails truthiness
        result = _validate_value('field', {}, dict)
        assert result is False

        # Non-empty list - passes
        result = _validate_value('field', [1, 2, 3], list)
        assert result is True

        # Non-empty dict - passes
        result = _validate_value('field', {'key': 'value'}, dict)
        assert result is True

    def test_validate_field_no_type_check(self):
        """Test validation without type checking (only truthiness)."""
        # Truthy value without type check
        result = _validate_value('field', "anything")
        assert result is True

        result = _validate_value('field', 123)
        assert result is True

        # Falsy values without type check
        result = _validate_value('field', None)
        assert result is False

        result = _validate_value('field', "")
        assert result is False

        result = _validate_value('field', 0)
        assert result is False


class TestLeapYearEdgeCases:
    """Test edge cases for Feb 29 birthdays in leap years."""

    def test_feb_29_birthday_within_7_days_leap_year(self):
        """Feb 29 birthday within 7 days in a leap year should be included."""
        from unittest.mock import patch
        from datetime import date

        with patch('tasks.task_4.datetime') as mock_datetime:
            # Mock current date to Feb 24, 2024 (leap year, Feb 29 is 5 days away)
            mock_datetime.today.return_value.date.return_value = date(2024, 2, 24)
            mock_datetime.strptime = datetime.strptime

            users = [
                {"name": "Leap Day Baby", "birthday": "2000.02.29"},
            ]

            result = get_upcoming_birthdays(users)

            # Feb 29 is within 7 days, should be included
            assert len(result) == 1
            assert result[0]['name'] == "Leap Day Baby"
            assert result[0]['congratulation_date'] == "2024.02.29"

    def test_feb_29_birthday_on_saturday(self):
        """Feb 29 birthday on Saturday should move to Monday."""
        from unittest.mock import patch
        from datetime import date

        with patch('tasks.task_4.datetime') as mock_datetime:
            # Feb 29, 2020 was a Saturday
            # Mock current date to Feb 24, 2020 (5 days before)
            mock_datetime.today.return_value.date.return_value = date(2020, 2, 24)
            mock_datetime.strptime = datetime.strptime

            users = [
                {"name": "Leap Day Baby", "birthday": "2000.02.29"},
            ]

            result = get_upcoming_birthdays(users)

            # Feb 29, 2020 is Saturday, should move to Monday March 2
            assert len(result) == 1
            assert result[0]['name'] == "Leap Day Baby"
            assert result[0]['congratulation_date'] == "2020.03.02"

    def test_feb_29_moved_to_march_1_within_range(self):
        """Feb 29 birthday in non-leap year should be moved to March 1 (or Monday if weekend)."""
        from unittest.mock import patch
        from datetime import date

        with patch('tasks.task_4.datetime') as mock_datetime:
            # Mock current date to Feb 25, 2025 (non-leap year)
            # March 1, 2025 is 4 days away, but it's a Saturday
            mock_datetime.today.return_value.date.return_value = date(2025, 2, 25)
            mock_datetime.strptime = datetime.strptime

            users = [
                {"name": "Leap Day Baby", "birthday": "2000.02.29"},
            ]

            result = get_upcoming_birthdays(users)

            # Feb 29 → March 1, 2025 (Saturday) → moved to Monday, March 3
            assert len(result) == 1
            assert result[0]['name'] == "Leap Day Baby"
            assert result[0]['congratulation_date'] == "2025.03.03"
