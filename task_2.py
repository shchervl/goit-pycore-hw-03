import random
from typing import List


def get_numbers_ticket(min: int, max: int, quantity: int) -> List[int]:
    """Generate a sorted list of unique random numbers for a lottery ticket.

    Selects a specified quantity of unique random numbers within a given range
    and returns them in sorted order. Useful for lottery number generation.

    Args:
        min: The minimum value in the range (must be >= 1).
        max: The maximum value in the range (must be > min and <= 1000).
        quantity: The number of random numbers to select (must be >= 1
                  and <= available range size).

    Returns:
        A sorted list of unique random integers. Returns an empty list
        if validation fails.

    Validation Rules:
        - min must be >= 1
        - max must be > min
        - max should be reasonable (e.g., <= 1000 for lottery)
        - quantity must be >= 1
        - quantity must be <= (max - min + 1) to ensure uniqueness
        - All parameters must be integers

    """
    # Validate input types (reject booleans even though they're subclass of int)
    if any(isinstance(param, bool) for param in [min, max, quantity]):
        print("Error: Boolean parameters are not allowed.")
        return []

    if not all(isinstance(param, int) for param in [min, max, quantity]):
        print("Error: All parameters must be integers.")
        return []

    # Validate minimum value
    if min < 1:
        print("Error: Parameter 'min' must be >= 1.")
        return []

    # Validate maximum value
    if max > 1000:
        print("Error: Parameter 'max' should be <= 1000 for practical lottery use.")
        return []

    # Validate max > min
    if max <= min:
        print("Error: Parameter 'max' must be > parameter 'min'.")
        return []

    # Validate quantity
    if quantity < 1:
        print("Error: Parameter 'quantity' must be >= 1.")
        return []

    # Validate quantity doesn't exceed available range
    available_numbers = max - min + 1
    if quantity > available_numbers:
        print(
            f"Error: Quantity ({quantity}) must be <= available range "
            f"({available_numbers} numbers from {min} to {max})."
        )
        return []

    # Generate random selection
    variants = list(range(min, max + 1))
    selection = random.sample(variants, quantity)
    selection.sort()
    return selection
