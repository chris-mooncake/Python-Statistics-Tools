# Input function

def get_user_input() -> tuple[list[float], list[float]]:
    """
    Prompts the user to input two lists of numbers (X and Y) via the terminal.

    The function checks that both lists are non-empty, contain only numeric values,
    and are of the same length. It continues prompting the user until valid input
    is provided.

    Returns:
        tuple(list[float], list[float]): A tuple containing two lists of floats.
    """
    print("Enter the same number of values for each variable (X and Y) to calculate Pearson’s correlation coefficient.")
    
    while True:
        user_input_x = input("Enter the X values, separated by spaces (e.g., 1 2 3 4): ").split()
        user_input_y = input("Enter the Y values, separated by spaces (e.g., 2 4 6 8): ").split()
        try:
            floats_x = [float(i) for i in user_input_x]
            floats_y = [float(i) for i in user_input_y]
            if not floats_x or not floats_y:
                print("No numbers entered. Please try again.")
                continue
            elif len(user_input_x) != len(user_input_y):
                print("The lists you entered have different lengths. Please enter the same number of values for both X and Y.")
                continue
            return (floats_x, floats_y)
        except ValueError:
            print("Invalid input detected. Please enter only numbers.")

# Calculation function
def pearsons_correlation(x: list[float], y: list[float]) -> float:
    """
    Calculates the Pearson correlation coefficient between two lists of numeric values.

    Args:
        x (list[float]): The first list of numerical values (X).
        y (list[float]): The second list of numerical values (Y).

    Returns:
        float: The Pearson correlation coefficient (r) between the two datasets.

    Raises:
        ValueError: If the input lists are not of the same length.
    """

    length_of_x = len(x)
    length_of_y = len(y)

    mean_of_x = sum(x) / length_of_x
    mean_of_y = sum(y) / length_of_y

    deviation_x = [i - mean_of_x for i in x]
    deviation_y = [i - mean_of_y for i in y]

    product_of_deviation = [dx * dy for dx, dy in zip(deviation_x, deviation_y)]

    covariance_numerator = sum(product_of_deviation)

    variance_x = [i ** 2 for i in deviation_x]
    variance_y = [i ** 2 for i in deviation_y]

    denominator_x = sum(variance_x) ** 0.5
    denominator_y = sum(variance_y) ** 0.5
    denominator_xy = denominator_x * denominator_y

    if denominator_xy == 0:
        raise ValueError("Standard deviation is zero; correlation is undefined.")

    r_correlation = covariance_numerator / denominator_xy

    return r_correlation

# Execution

x, y = get_user_input()
print(f"Correlation coefficient (Pearson’s r): {pearsons_correlation(x, y):.6f}")
