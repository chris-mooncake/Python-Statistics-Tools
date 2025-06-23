# Input function

def get_user_input() -> list[float]:
    """
    Prompts the user to input a list of positive numeric values separated by spaces.

    Returns:
        list[float]: A list of positive floating-point numbers entered by the user.
    """
    while True:
        user_input = input('Please input your numbers separated by spaces: ')
        try:
            numbers = [float(i) for i in user_input.split()]
            if not numbers:
                print("No numbers entered. Please try again.")
                continue
            if any(x <= 0 for x in numbers):
                print("Negative values or zero are not suitable for calculating geometric mean.")
                continue
            return numbers
        except ValueError:
            print("Invalid input detected. Please enter only numbers.")

# Calculation function

def geometric_mean(n: list[float]) -> float:
    """
    Calculates the geometric mean of a list of positive numbers.

    Args:
        n (list[float]): List of positive numbers.

    Returns:
        float: Geometric mean.
    """
    product = 1
    for num in n:
        product *= num
    result = product ** (1 / len(n))
    return result


# Execution

g_mean = geometric_mean(get_user_input())
print(f"Geometric Mean: {g_mean:.4f}")
