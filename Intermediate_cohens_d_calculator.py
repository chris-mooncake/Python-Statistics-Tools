# Input function

def get_user_input() -> tuple[list[float], list[float]]:
    """
    Prompts the user to enter two samples of numerical data, separated by spaces.

    Returns:
        tuple[list[float], list[float]]: Two lists of floats representing the two samples.
    """
    while True:
        user_input_x = input("Enter the first sample values, separated by spaces (e.g., 1 2 3 4): ").split()
        user_input_y = input("Enter the second sample values, separated by spaces (e.g., 2 4 6 8): ").split()
        try:
            floats_x = [float(i) for i in user_input_x]
            floats_y = [float(i) for i in user_input_y]

            if not floats_x or not floats_y:
                print("No numbers entered. Please try again.")
                continue
            elif len(floats_x) != len(floats_y):
                print("The lists you entered have different lengths. Please enter the same number of values for both samples.")
                continue

            return floats_x, floats_y

        except ValueError:
            print("Invalid input detected. Please enter only numeric values.")

# Calculation functions

def standarddeviation(numbers: list[float]) -> float:
    """
    Calculates the sample standard deviation of a list of numbers.

    Args:
        numbers (list[float]): The sample data.

    Returns:
        float: The sample standard deviation.
    """
    length = len(numbers)
    if length < 2:
        raise ValueError("Standard deviation is undefined for fewer than 2 data points.")

    mean = sum(numbers) / length
    squared_diffs = [(i - mean) ** 2 for i in numbers]
    return (sum(squared_diffs) / (length - 1)) ** 0.5

def cohensd(first: list[float], second: list[float]) -> float:
    """
    Computes Cohen's d effect size between two samples.

    Args:
        first (list[float]): The first sample.
        second (list[float]): The second sample.

    Returns:
        float: Cohen’s d value.
    """
    mean_first = sum(first) / len(first)
    mean_second = sum(second) / len(second)
    s1 = standarddeviation(first)
    s2 = standarddeviation(second)
    pooled_std = ((s1 ** 2 + s2 ** 2) / 2) ** 0.5
    if pooled_std == 0:
        raise ValueError("Pooled standard deviation is zero — Cohen’s d is undefined.")
    return (mean_first - mean_second) / pooled_std

# Execution
input_1, input_2 = get_user_input()
result = cohensd(input_1, input_2)
print(f"\nCohen’s d: {result:.4f}")
