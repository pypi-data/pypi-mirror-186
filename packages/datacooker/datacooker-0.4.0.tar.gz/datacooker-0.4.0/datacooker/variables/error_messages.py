"""Error messages module"""

from scipy.stats import rv_continuous, rv_discrete


def invalid_missing_values_fraction_msg(fraction: float, label: str) -> str:
    """
    Builds error message for invalid missing values fractions assigned to a variable

    Args:
        missing_values_fraction (float): missing values fraction.
        label (str): variable label.

    Returns:
        str: error message
    """

    return f"""
        missing_values_fraction argument for variable {label} must be a number in [0,1) range. Value used: {fraction}, type: {type(fraction)}
    """


def invalid_distribution_type_msg(
        distribution: rv_continuous | rv_discrete,
        expected: rv_continuous | rv_discrete,
        label: str) -> str:
    """Builds error message for invalid distrubtion assigned to a variable

    Args:
        distribution (rv_continuous | rv_discrete): assigned distribution type.
        expected (rv_continuous | rv_discrete): expected distribution type.
        label (str): variable label.

    Returns:
        str: error message
    """

    return f"""
        invalid distribution assigned to variable {label}. Expected distribution type: {type(expected)}, assigned distribution type: {type(distribution)}.
    """
