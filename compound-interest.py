def compound_interest(principal, interest_rate, compounding_frequency, years):
    """
    Calculate the final amount using the compound interest formula.

    Args:
        principal (float): The principal amount.
        interest_rate (float): The annual interest rate.
        compounding_frequency (int): Number of times interest is compounded per year.
        years (int): Number of years.

    Returns:
        float: The final amount after compound interest.
    """
    # Validate input parameters
    if not isinstance(principal, (int, float)) or principal < 0:
        raise ValueError("Principal amount must be a non-negative number.")

    if not isinstance(interest_rate, (int, float)) or interest_rate < 0:
        raise ValueError("Interest rate must be a non-negative number.")

    if not isinstance(compounding_frequency, int) or compounding_frequency <= 0:
        raise ValueError("Compounding frequency must be a positive integer.")

    if not isinstance(years, int) or years < 0:
        raise ValueError("Number of years must be a non-negative integer.")

    # Calculating the final amount using the compound interest formula
    final_amount = principal * (1 + interest_rate / compounding_frequency)**(compounding_frequency * years)

    return final_amount

# Example usage:
P = 10000
r = 0.08
n = 12
t = int(input("Enter the number of years: "))

try:
    result = compound_interest(P, r, n, t)
    print(f"The final amount after {t} years is: {result:.2f}")
except ValueError as e:
    print(f"Error: {e}")
