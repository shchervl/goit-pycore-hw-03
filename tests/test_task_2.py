"""
Comprehensive test suite for get_numbers_ticket function.

Test Coverage:
- Boundary values (min=1, max limits, quantity limits)
- Negative scenarios (invalid types, out-of-range values)
- Property-based testing (sorted, unique, in-range)
- Randomness validation
"""

from tasks.task_2 import get_numbers_ticket


class TestGetNumbersTicket:
    """Test suite for get_numbers_ticket function."""

    # ==================== BOUNDARY VALUES ====================

    def test_minimum_min_value(self):
        """Minimum allowed min value (1)."""
        result = get_numbers_ticket(1, 3, 3)
        assert len(result) == 3
        assert min(result) >= 1

    def test_maximum_max_value(self):
        """Maximum allowed max value (1000)."""
        result = get_numbers_ticket(995, 1000, 5)
        assert len(result) == 5
        assert max(result) <= 1000

    def test_single_number_selection(self):
        """Boundary: quantity = 1."""
        result = get_numbers_ticket(1, 100, 1)
        assert len(result) == 1
        assert 1 <= result[0] <= 100

    def test_two_number_range(self):
        """Boundary: smallest possible range (2 numbers)."""
        result = get_numbers_ticket(5, 6, 1)
        assert len(result) == 1
        assert result[0] in [5, 6]

    def test_two_number_range_select_both(self):
        """Boundary: select both numbers from 2-number range."""
        result = get_numbers_ticket(5, 6, 2)
        assert len(result) == 2
        assert result == [5, 6]

    # ==================== PROPERTY TESTING ====================

    def test_result_is_always_sorted(self):
        """Result must always be sorted in ascending order."""
        for _ in range(10):  # Test multiple times due to randomness
            result = get_numbers_ticket(1, 100, 10)
            assert result == sorted(result)

    def test_all_numbers_are_unique(self):
        """All numbers in result must be unique."""
        for _ in range(10):
            result = get_numbers_ticket(1, 100, 20)
            assert len(result) == len(set(result))

    # ==================== NEGATIVE SCENARIOS: INVALID TYPES ====================

    def test_min_as_float_returns_empty(self):
        """Float min parameter should return empty list."""
        result = get_numbers_ticket(1.5, 10, 5)
        assert result == []

    def test_max_as_float_returns_empty(self):
        """Float max parameter should return empty list."""
        result = get_numbers_ticket(1, 10.5, 5)
        assert result == []

    def test_quantity_as_float_returns_empty(self):
        """Float quantity parameter should return empty list."""
        result = get_numbers_ticket(1, 10, 5.5)
        assert result == []

    def test_min_as_string_returns_empty(self):
        """String min parameter should return empty list."""
        result = get_numbers_ticket("1", 10, 5)
        assert result == []

    def test_max_as_string_returns_empty(self):
        """String max parameter should return empty list."""
        result = get_numbers_ticket(1, "10", 5)
        assert result == []

    def test_quantity_as_string_returns_empty(self):
        """String quantity parameter should return empty list."""
        result = get_numbers_ticket(1, 10, "5")
        assert result == []

    def test_none_parameters_return_empty(self):
        """None parameters should return empty list."""
        assert get_numbers_ticket(None, 10, 5) == []
        assert get_numbers_ticket(1, None, 5) == []
        assert get_numbers_ticket(1, 10, None) == []

    def test_list_parameters_return_empty(self):
        """List parameters should return empty list."""
        result = get_numbers_ticket([1], 10, 5)
        assert result == []

    def test_boolean_parameters_return_empty(self):
        """Boolean parameters should return empty list."""
        result = get_numbers_ticket(True, 10, 5)
        assert result == []

    # ==================== NEGATIVE SCENARIOS: INVALID VALUES ====================

    def test_min_zero_returns_empty(self):
        """min = 0 should return empty list."""
        result = get_numbers_ticket(0, 10, 5)
        assert result == []

    def test_min_negative_returns_empty(self):
        """Negative min should return empty list."""
        result = get_numbers_ticket(-5, 10, 5)
        assert result == []

    def test_max_less_than_min_returns_empty(self):
        """max < min should return empty list."""
        result = get_numbers_ticket(10, 5, 3)
        assert result == []

    def test_max_equal_to_min_returns_empty(self):
        """max = min should return empty list (need range)."""
        result = get_numbers_ticket(5, 5, 1)
        assert result == []

    def test_max_exceeds_limit_returns_empty(self):
        """max > 1000 should return empty list."""
        result = get_numbers_ticket(1, 1001, 10)
        assert result == []

    def test_max_far_exceeds_limit_returns_empty(self):
        """max >> 1000 should return empty list."""
        result = get_numbers_ticket(1, 10000, 10)
        assert result == []

    def test_quantity_zero_returns_empty(self):
        """quantity = 0 should return empty list."""
        result = get_numbers_ticket(1, 10, 0)
        assert result == []

    def test_quantity_negative_returns_empty(self):
        """Negative quantity should return empty list."""
        result = get_numbers_ticket(1, 10, -5)
        assert result == []

    def test_quantity_exceeds_range_returns_empty(self):
        """quantity > available range should return empty list."""
        result = get_numbers_ticket(1, 10, 11)  # Only 10 numbers available
        assert result == []

    def test_quantity_much_larger_than_range_returns_empty(self):
        """quantity >> range should return empty list."""
        result = get_numbers_ticket(1, 10, 100)
        assert result == []

    # ==================== EDGE CASES ====================

    def test_consecutive_numbers_small_range(self):
        """Selecting from very small consecutive range."""
        result = get_numbers_ticket(98, 100, 2)
        assert len(result) == 2
        assert all(98 <= n <= 100 for n in result)
        assert len(set(result)) == 2

    def test_large_min_value(self):
        """Large min value (close to max limit)."""
        result = get_numbers_ticket(950, 1000, 10)
        assert len(result) == 10
        assert all(950 <= n <= 1000 for n in result)

    def test_single_number_from_large_range(self):
        """Selecting just 1 number from large range."""
        result = get_numbers_ticket(1, 1000, 1)
        assert len(result) == 1
        assert 1 <= result[0] <= 1000

    def test_almost_full_range_selection(self):
        """Selecting almost all numbers from range."""
        result = get_numbers_ticket(1, 20, 19)
        assert len(result) == 19
        assert len(set(result)) == 19
        missing_number = set(range(1, 21)) - set(result)
        assert len(missing_number) == 1  # Exactly one number not selected