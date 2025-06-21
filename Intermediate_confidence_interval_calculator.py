from scipy.stats import t

# Input array function

def get_user_input() -> tuple[list[float], float]:
    """
    Prompts the user to input a list of numeric values and a confidence level.

    Returns:
        tuple[list[float], float]: A list of sample values and the confidence level (as a percentage).
    """
    while True:
        user_input = input("Please input your numbers separated by spaces: ")
        confidence_interval = input("Enter the confidence level (e.g., 90, 95, or 99): ")

        try:
            numbers = [float(i) for i in user_input.split()]
            conf = float(confidence_interval)

            if not numbers:
                print("No numbers entered. Please try again.")
                continue

            if len(numbers) < 2:
                print("Sample size must be at least 2. Please enter more values.")
                continue

            if not (0 < conf < 100):
                print("Invalid confidence level. Please enter a value between 0 and 100.")
                continue

            return numbers, conf

        except ValueError:
            print("Invalid input detected. Please enter only numeric values.")


# Standard deviation function

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


# Confidence interval function

def cfi_mean(data: list[float], confidence_percent: float) -> tuple[float, float]:
    """
    Calculates the confidence interval for the mean of a sample.

    Args:
        data (list[float]): Sample data
        confidence_percent (float): Confidence level (e.g., 95 for 95%)

    Returns:
        tuple[float, float]: Lower and upper bounds of the confidence interval
    """
    n = len(data)
    mean = sum(data) / n
    std = standarddeviation(data)
    confidence = confidence_percent / 100
    alpha = 1 - confidence
    df = n - 1

    t_value = t.ppf(1 - alpha / 2, df)
    margin = t_value * (std / (n ** 0.5))

    return (mean - margin, mean + margin)


# Execution

user_numbers, user_conf = get_user_input()
ci_lower, ci_upper = cfi_mean(user_numbers, user_conf)
print(f"\nConfidence Interval for the Mean ({user_conf}%):")
print(f"Lower Bound: {ci_lower:.4f}")
print(f"Upper Bound: {ci_upper:.4f}")
