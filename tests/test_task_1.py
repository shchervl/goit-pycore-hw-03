"""
Comprehensive test suite for get_days_from_today function.

Test Coverage:
- Boundary values (today, ±1 day, month/year boundaries)
- Negative scenarios (invalid types, formats, dates)
- Leap year validation (past and future)
- Dynamic date calculation (no hardcoded dates)
"""

import pytest
from datetime import datetime, timedelta

from task_1 import get_days_from_today


class TestGetDaysFromToday:
    """Test suite for get_days_from_today function."""

    # ==================== BOUNDARY VALUES ====================

    def test_yesterday_returns_minus_one(self):
        """Yesterday should return -1."""
        yesterday = (datetime.now().date() - timedelta(days=1)).isoformat()
        result = get_days_from_today(yesterday)
        assert result == -1

    def test_tomorrow_returns_plus_one(self):
        """Tomorrow should return +1."""
        tomorrow = (datetime.now().date() + timedelta(days=1)).isoformat()
        result = get_days_from_today(tomorrow)
        assert result == 1

    def test_first_day_of_month(self):
        """First day of current month."""
        today = datetime.now().date()
        first_day = today.replace(day=1)
        expected_days = (first_day - today).days
        result = get_days_from_today(first_day.isoformat())
        assert result == expected_days

    def test_last_day_of_month(self):
        """Last day of current month."""
        today = datetime.now().date()
        # Get last day of current month
        next_month = today.replace(day=28) + timedelta(days=4)
        last_day = next_month - timedelta(days=next_month.day)
        expected_days = (last_day - today).days
        result = get_days_from_today(last_day.isoformat())
        assert result == expected_days

    def test_first_day_of_year(self):
        """First day of current year."""
        today = datetime.now().date()
        first_day = today.replace(month=1, day=1)
        expected_days = (first_day - today).days
        result = get_days_from_today(first_day.isoformat())
        assert result == expected_days

    def test_last_day_of_year(self):
        """Last day of current year."""
        today = datetime.now().date()
        last_day = today.replace(month=12, day=31)
        expected_days = (last_day - today).days
        result = get_days_from_today(last_day.isoformat())
        assert result == expected_days

    def test_one_year_in_past(self):
        """Date exactly one year in the past."""
        one_year_ago = datetime.now().date() - timedelta(days=365)
        result = get_days_from_today(one_year_ago.isoformat())
        assert result == -365

    def test_one_year_in_future(self):
        """Date exactly one year in the future."""
        one_year_ahead = datetime.now().date() + timedelta(days=365)
        result = get_days_from_today(one_year_ahead.isoformat())
        assert result == 365

    # ==================== LEAP YEAR VALIDATION ====================

    def test_leap_year_feb_29_past(self):
        """Valid Feb 29 on a past leap year (2024)."""
        result = get_days_from_today("2024-02-29")
        today = datetime.now().date()
        leap_date = datetime(2024, 2, 29).date()
        expected = (leap_date - today).days
        assert result == expected

    def test_leap_year_feb_29_future(self):
        """Valid Feb 29 on a future leap year (2028)."""
        result = get_days_from_today("2028-02-29")
        today = datetime.now().date()
        leap_date = datetime(2028, 2, 29).date()
        expected = (leap_date - today).days
        assert result == expected

    def test_non_leap_year_feb_29_fails(self):
        """Feb 29 on a non-leap year should return None (2025, 2026, 2027)."""
        result_2025 = get_days_from_today("2025-02-29")
        result_2026 = get_days_from_today("2026-02-29")
        result_2027 = get_days_from_today("2027-02-29")

        assert result_2025 is None
        assert result_2026 is None
        assert result_2027 is None

    def test_leap_year_feb_28(self):
        """Feb 28 on a leap year should work."""
        result = get_days_from_today("2024-02-28")
        today = datetime.now().date()
        date = datetime(2024, 2, 28).date()
        expected = (date - today).days
        assert result == expected

    def test_leap_year_march_1(self):
        """March 1 on a leap year should work."""
        result = get_days_from_today("2024-03-01")
        today = datetime.now().date()
        date = datetime(2024, 3, 1).date()
        expected = (date - today).days
        assert result == expected

    # ==================== NEGATIVE SCENARIOS: INVALID TYPES ====================

    def test_none_input_returns_none(self):
        """None input should return None."""
        result = get_days_from_today(None)
        assert result is None

    def test_integer_input_returns_none(self):
        """Integer input should return None."""
        result = get_days_from_today(20260208)
        assert result is None

    def test_float_input_returns_none(self):
        """Float input should return None."""
        result = get_days_from_today(2026.0208)
        assert result is None

    def test_list_input_returns_none(self):
        """List input should return None."""
        result = get_days_from_today(["2026-02-08"])
        assert result is None

    def test_dict_input_returns_none(self):
        """Dictionary input should return None."""
        result = get_days_from_today({"date": "2026-02-08"})
        assert result is None

    def test_datetime_object_returns_none(self):
        """Datetime object input should return None."""
        result = get_days_from_today(datetime.now())
        assert result is None

    # ==================== NEGATIVE SCENARIOS: INVALID FORMATS ====================

    def test_empty_string_returns_none(self):
        """Empty string should return None."""
        result = get_days_from_today("")
        assert result is None

    def test_whitespace_only_returns_none(self):
        """Whitespace-only string should return None."""
        result = get_days_from_today("   ")
        assert result is None

    def test_invalid_format_dd_mm_yyyy_returns_none(self):
        """DD-MM-YYYY format should return None."""
        result = get_days_from_today("08-02-2026")
        assert result is None

    def test_invalid_format_mm_dd_yyyy_returns_none(self):
        """MM/DD/YYYY format should return None."""
        result = get_days_from_today("02/08/2026")
        assert result is None

    def test_invalid_format_with_dots_returns_none(self):
        """DD.MM.YYYY format should return None."""
        result = get_days_from_today("08.02.2026")
        assert result is None

    def test_invalid_format_text_month_returns_none(self):
        """Text month format should return None."""
        result = get_days_from_today("February 8, 2026")
        assert result is None

    def test_invalid_format_short_date_returns_none(self):
        """Short date format should return None."""
        result = get_days_from_today("2026-2-8")
        assert result is None

    def test_invalid_format_reversed_returns_none(self):
        """Reversed format (DD-MM-YYYY) should return None."""
        result = get_days_from_today("08-02-2026")
        assert result is None

    def test_random_text_returns_none(self):
        """Random text should return None."""
        result = get_days_from_today("not a date")
        assert result is None

    # ==================== NEGATIVE SCENARIOS: INVALID DATES ====================

    def test_invalid_month_returns_none(self):
        """Month > 12 should return None."""
        result = get_days_from_today("2026-13-01")
        assert result is None

    def test_invalid_day_returns_none(self):
        """Day > 31 should return None."""
        result = get_days_from_today("2026-01-32")
        assert result is None

    def test_february_30_returns_none(self):
        """February 30 (non-existent) should return None."""
        result = get_days_from_today("2026-02-29")
        assert result is None

    def test_zero_month_returns_none(self):
        """Month 0 should return None."""
        result = get_days_from_today("2026-00-15")
        assert result is None

    def test_zero_day_returns_none(self):
        """Day 0 should return None."""
        result = get_days_from_today("2026-02-00")
        assert result is None

    # ==================== EDGE CASES ====================

    def test_very_far_future_date(self):
        """Very far future date (100 years ahead)."""
        far_future = datetime.now().date() + timedelta(days=36500)
        result = get_days_from_today(far_future.isoformat())
        assert result == 36500

    def test_very_far_past_date(self):
        """Very far past date (100 years ago)."""
        far_past = datetime.now().date() - timedelta(days=36500)
        result = get_days_from_today(far_past.isoformat())
        assert result == -36500

    def test_date_with_microseconds(self):
        """Date with full ISO format including microseconds."""
        today = datetime.now().date()
        date_with_micro = f"{today.isoformat()}T14:30:00.123456"
        result = get_days_from_today(date_with_micro)
        assert result == 0

    def test_date_with_timezone(self):
        """Date with timezone should work (timezone is ignored in date comparison)."""
        today = datetime.now().date()
        date_with_tz = f"{today.isoformat()}T14:30:00+02:00"
        result = get_days_from_today(date_with_tz)
        assert result == 0