def calculate_emi(principal: float, annual_rate: float, years: int) -> float:
    """
    Calculate the EMI (Equated Monthly Installment) for a loan.
    Formula:
        EMI = P * r * (1 + r)^n / ((1 + r)^n - 1)
    """
    if principal <= 0 or annual_rate <= 0 or years <= 0:
        raise ValueError("Principal, rate, and years must be positive.")

    monthly_rate = annual_rate / (12 * 100)
    num_payments = years * 12

    emi = principal * monthly_rate * (1 + monthly_rate) ** num_payments / ((1 + monthly_rate) ** num_payments - 1)
    return round(emi, 2)
