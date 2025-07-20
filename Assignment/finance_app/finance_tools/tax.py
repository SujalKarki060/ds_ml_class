def calculate_tax(income: float, tax_rate: float = 0.15) -> float:
    """
    Calculate tax based on income and tax rate.
    Default tax rate is 15%.
    """
    if income < 0:
        raise ValueError("Income cannot be negative.")
    return income * tax_rate
