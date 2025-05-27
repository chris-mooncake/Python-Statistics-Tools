import math

# User input function

def get_user_input() -> tuple[float, float, float]:
    """
    Prompts the user to input:
        - The value at which the PDF should be evaluated (x),
        - The mean (μ) of the normal distribution,
        - The standard deviation (σ) of the distribution.

    Returns:
        tuple(float, float, float): A tuple containing:
            - x (float): The point at which to evaluate the PDF.
            - mu (float): The mean of the distribution.
            - sigma (float): The standard deviation of the distribution (must be > 0).
    """
    while True:
        print("Please enter the value at which you want to evaluate the PDF, " \
              "the mean of the distribution, and the standard deviation.")
        value = input("Please input the value at which you want to evaluate (e.g., 0.5): ")
        mean = input("Please enter the mean (e.g., 1.5): ")
        sigma = input("Please enter the standard deviation (e.g., 0.5): ")

        try:
            value, mean, sigma = float(value), float(mean), float(sigma)
            if sigma <= 0:
                print("Standard deviation must be greater than zero.")
                continue
            return (value, mean, sigma)
        except ValueError:
            print("Invalid input detected. Please enter only numeric values.")

# Calculation function

def pdf(v: float, m: float, s: float) -> float:
    """
    Calculates the value of the Probability Density Function (PDF) of a normal 
    distribution at a given point.

    Args:
        v (float): The value at which to evaluate the PDF.
        m (float): The mean (μ) of the normal distribution.
        s (float): The standard deviation (σ) of the distribution (must be > 0).

    Returns:
        float: The calculated PDF value at point v.
    """
    top = (v - m) ** 2
    bottom = 2 * s ** 2
    exponent = -1 * (top / bottom)
    exp_result = math.exp(exponent)
    coefficient = 1 / (s * math.sqrt(2 * math.pi))
    f_x = exp_result * coefficient
    return f_x

# Execution

x, mu, sigma = get_user_input()
result = pdf(x, mu, sigma)
print(f"PDF: {result}")
