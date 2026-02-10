"""
Comprehensive test suite for normalize_phone function.

Test Coverage:
- Boundary values (minimum length, edge cases)
- Negative scenarios (invalid types, empty strings, too short numbers)
- Various phone number formats (local, international, with formatting)
- Country code handling
"""

import pytest
from tasks.task_3 import normalize_phone


class TestNormalizePhone:
    """Test suite for normalize_phone function."""

    # ==================== BOUNDARY VALUES ====================

    def test_minimum_length_phone(self):
        """Minimum valid length: country code + 9 digits."""
        result = normalize_phone("050123456")  # 9 digits
        assert result == "+38050123456"

    def test_long_phone_number(self):
        """Longer phone number (11 digits)."""
        result = normalize_phone("05012345678")
        assert result == "+3805012345678"

    def test_very_long_phone_number(self):
        """Very long phone number (15 digits, max international)."""
        result = normalize_phone("050123456789012")
        assert result == "+38050123456789012"

    def test_single_digit_country_code(self):
        """Single digit country code."""
        result = normalize_phone("5012345678", country_code=1)
        assert result == "+15012345678"

    def test_three_digit_country_code(self):
        """Three digit country code."""
        result = normalize_phone("5012345678", country_code=123)
        assert result == "+1235012345678"

    # ==================== COUNTRY CODE VARIATIONS ====================

    def test_different_country_code_us(self):
        """US country code (1)."""
        result = normalize_phone("5551234567", country_code=1)
        assert result == "+15551234567"

    def test_different_country_code_uk(self):
        """UK country code (44)."""
        result = normalize_phone("7911123456", country_code=44)
        assert result == "+447911123456"

    def test_different_country_code_keeps_all_digits(self):
        """When input has different country code, all digits are kept."""
        # Input has +1 (US), normalize to +38 (Ukraine)
        # Note: This doesn't "convert" between countries, it normalizes
        # malformed numbers. All digits are preserved.
        result = normalize_phone("+15551234567", country_code=38)
        assert result == "+3815551234567"  # Keeps all digits including the '1'

    def test_country_code_already_present(self):
        """Country code already present in number."""
        result = normalize_phone("+380501234567", country_code=38)
        assert result == "+380501234567"

    def test_country_code_without_plus(self):
        """Number with country code but without plus."""
        result = normalize_phone("380501234567", country_code=38)
        assert result == "+380501234567"

    # ==================== NEGATIVE SCENARIOS: INVALID TYPES ====================

    def test_none_phone_number_returns_none(self):
        """None as phone_number should return None."""
        result = normalize_phone(None)
        assert result is None

    def test_integer_phone_number_returns_none(self):
        """Integer as phone_number should return None."""
        result = normalize_phone(380501234567)
        assert result is None

    def test_float_phone_number_returns_none(self):
        """Float as phone_number should return None."""
        result = normalize_phone(380501234567.0)
        assert result is None

    def test_list_phone_number_returns_none(self):
        """List as phone_number should return None."""
        result = normalize_phone(["380501234567"])
        assert result is None

    def test_dict_phone_number_returns_none(self):
        """Dict as phone_number should return None."""
        result = normalize_phone({"phone": "380501234567"})
        assert result is None

    def test_boolean_phone_number_returns_none(self):
        """Boolean as phone_number should return None."""
        result = normalize_phone(True)
        assert result is None

    def test_none_country_code_returns_none(self):
        """None as country_code should return None."""
        result = normalize_phone("0501234567", country_code=None)
        assert result is None

    def test_string_country_code_returns_none(self):
        """String as country_code should return None."""
        result = normalize_phone("0501234567", country_code="38")
        assert result is None

    def test_float_country_code_returns_none(self):
        """Float as country_code should return None."""
        result = normalize_phone("0501234567", country_code=38.0)
        assert result is None

    def test_list_country_code_returns_none(self):
        """List as country_code should return None."""
        result = normalize_phone("0501234567", country_code=[38])
        assert result is None

    def test_boolean_country_code_returns_none(self):
        """Boolean as country_code should return None."""
        result = normalize_phone("0501234567", country_code=True)
        assert result is None

    # ==================== NEGATIVE SCENARIOS: INVALID VALUES ====================

    def test_empty_string_returns_none(self):
        """Empty string should return None."""
        result = normalize_phone("")
        assert result is None

    def test_whitespace_only_returns_none(self):
        """Whitespace-only string should return None."""
        result = normalize_phone("   ")
        assert result is None

    def test_too_short_phone_returns_none(self):
        """Phone number too short (less than 9 digits after country code)."""
        result = normalize_phone("12345")
        assert result is None

    def test_very_short_phone_returns_none(self):
        """Very short phone number (3 digits)."""
        result = normalize_phone("123")
        assert result is None

    def test_single_digit_returns_none(self):
        """Single digit returns None."""
        result = normalize_phone("5")
        assert result is None

    def test_only_special_characters_returns_none(self):
        """Only special characters returns None."""
        result = normalize_phone("()---...")
        assert result is None

    def test_zero_country_code_returns_none(self):
        """Country code of 0 should return None."""
        result = normalize_phone("0501234567", country_code=0)
        assert result is None

    def test_negative_country_code_returns_none(self):
        """Negative country code should return None."""
        result = normalize_phone("0501234567", country_code=-38)
        assert result is None

    def test_very_negative_country_code_returns_none(self):
        """Very negative country code should return None."""
        result = normalize_phone("0501234567", country_code=-999)
        assert result is None

    # ==================== EDGE CASES ====================

    def test_phone_with_letters_returns_none(self):
        """Phone with letters should return None (too short after cleaning)."""
        result = normalize_phone("abc123def")
        assert result is None

    def test_phone_with_multiple_plus_signs(self):
        """Phone with multiple + signs (only first + is kept)."""
        result = normalize_phone("+38+050+123+45+67")
        assert result == "+380501234567"

    def test_unicode_digits(self):
        """Unicode digits should be cleaned."""
        result = normalize_phone("050①②③④⑤⑥⑦")
        assert result is None  # Unicode digits removed, too short

    def test_phone_all_zeros(self):
        """Phone number with all zeros."""
        result = normalize_phone("0000000000")
        assert result == "+380000000000"

    def test_phone_all_nines(self):
        """Phone number with all nines."""
        result = normalize_phone("9999999999")
        assert result == "+389999999999"

    def test_leading_plus_already_present(self):
        """Leading + already present."""
        result = normalize_phone("+0501234567")
        assert result == "+380501234567"

    def test_multiple_spaces_between_digits(self):
        """Multiple spaces between digits."""
        result = normalize_phone("050    123    45    67")
        assert result == "+380501234567"

    def test_tabs_and_newlines(self):
        """Tabs and newlines in phone number."""
        result = normalize_phone("050\t123\n45\r67")
        assert result == "+380501234567"


# ==================== PARAMETRIZED TESTS FOR EFFICIENCY ====================

class TestParametrizedScenarios:
    """Parametrized tests for comprehensive coverage."""

    @pytest.mark.parametrize("phone_input,expected", [
        ("0501234567", "+380501234567"),
        ("380501234567", "+380501234567"),
        ("+380501234567", "+380501234567"),
        ("(050) 123-45-67", "+380501234567"),
        ("050 123 45 67", "+380501234567"),
        ("050-123-45-67", "+380501234567"),
        ("050.123.45.67", "+380501234567"),
        ("+38 (050) 123-45-67", "+380501234567"),
        ("  0501234567  ", "+380501234567"),
    ])
    def test_various_valid_formats(self, phone_input, expected):
        """Test various valid phone formats."""
        result = normalize_phone(phone_input)
        assert result == expected

    @pytest.mark.parametrize("invalid_input", [
        None,
        123,
        12.34,
        [],
        {},
        True,
        False,
        ("050", "123"),
    ])
    def test_invalid_phone_types(self, invalid_input):
        """Test invalid types for phone_number."""
        result = normalize_phone(invalid_input)
        assert result is None

    @pytest.mark.parametrize("invalid_code", [
        None,
        "38",        # String (should be int)
        38.5,        # Float
        [],
        {},
        True,        # Boolean
        False,       # Boolean
        0,           # Zero
        -1,          # Negative
        -38,         # Negative
    ])
    def test_invalid_country_codes(self, invalid_code):
        """Test invalid country codes."""
        result = normalize_phone("0501234567", country_code=invalid_code)
        assert result is None

    @pytest.mark.parametrize("short_number", [
        "",
        "1",
        "12",
        "123",
        "1234",
        "12345",
        "123456",
        "1234567",
        "12345678",  # 8 digits (needs at least 9 after country code)
    ])
    def test_too_short_numbers(self, short_number):
        """Test phone numbers that are too short."""
        result = normalize_phone(short_number)
        assert result is None

    @pytest.mark.parametrize("phone,country,expected", [
        ("5012345678", 1, "+15012345678"),      # US
        ("7911123456", 44, "+447911123456"),    # UK
        ("112345678", 49, "+49112345678"),      # Germany
        ("912345678", 33, "+33912345678"),      # France
        ("3123456789", 39, "+393123456789"),    # Italy
    ])
    def test_different_country_codes(self, phone, country, expected):
        """Test various country codes."""
        result = normalize_phone(phone, country_code=country)
        assert result == expected

    @pytest.mark.parametrize("formatted_phone", [
        "(050) 123 45 67",
        "050-123-45-67",
        "050.123.45.67",
        "050 123 45 67",
        "+38 050 123 45 67",
        "+38(050)123-45-67",
        "+38-050-123-45-67",
    ])
    def test_various_formatting_styles(self, formatted_phone):
        """Test various formatting styles all normalize to same result."""
        result = normalize_phone(formatted_phone)
        assert result == "+380501234567"
