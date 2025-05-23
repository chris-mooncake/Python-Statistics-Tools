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
            elif len(floats_x) != len(floats_y):
                print("The lists you entered have different lengths. Please enter the same number of values for both X and Y.")
                continue
            return (floats_x, floats_y)
        except ValueError:
            print("Invalid input detected. Please enter only numbers.")

# Calculation function
def covariance(x: list[float], y: list[float]) -> float:
    """
    Calculates covariance between two lists of numeric values.

    Args:
        x (list[float]): The first list of numerical values (X).
        y (list[float]): The second list of numerical values (Y).

    Returns:
        float: The covariance between the two datasets.
    """

    length_of_x, length_of_y = len(x), len(y)
    mean_of_x, mean_of_y = sum(x) / length_of_x, sum(y) / length_of_y
    
    deviation_x = [i - mean_of_x for i in x]
    deviation_y = [i - mean_of_y for i in y]

    product_of_deviation = [dx * dy for dx, dy in zip(deviation_x, deviation_y)]

    sum_of_deviation = sum(product_of_deviation)

    while True:
        user_input = input("Is your data population or a sample? Type p or s: ").lower()
        if user_input in ["p", "s"]:
            break
        else:
            print("Invalid input.")
            continue
    
    if user_input == "s":
        length_of_x -= 1

    cov = sum_of_deviation / length_of_x

    return cov

# Execution

x, y = get_user_input()
print(f"Covariance: {covariance(x, y):.4f}")
