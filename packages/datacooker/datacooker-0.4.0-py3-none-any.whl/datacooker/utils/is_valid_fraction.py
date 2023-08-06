"""
is_valid_fraction function module
"""

from numbers import Number


def is_valid_fraction(fraction: float) -> bool:
    """Check if a fraction is a number and is in range [0,1)

    Args:
        fraction (float): value to be validated

    Returns:
        bool: if fraction is valid or not
    """
    if isinstance(fraction, Number) and (0 <= fraction < 1):
        return True

    return False
