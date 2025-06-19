import matplotlib.pyplot as plt

# Input array function

def get_user_input() -> list[float]:
    """
    Prompts the user to input a list of numeric values separated by spaces.

    Returns:
        list[float]: A sorted list of floating-point numbers entered by the user.

    Input Example:
        4 2 5.5 1 3
    """
    while True:
        user_input = input('Please input your numbers separated by spaces: ')
        try:
            numbers = [float(i) for i in user_input.split()]
            if not numbers:
                print("No numbers entered. Please try again.")
                continue
            return sorted(numbers)
        except ValueError:
            print("Invalid input detected. Please enter only numbers.")

# Calculation function

def ecdf(n):
    """
    Calculates the Empirical Cumulative Distribution Function (ECDF) for a dataset.

    Args:
        data (list[float]): A sorted list of numerical data.

    Returns:
        list[tuple[float, float]]: A list of tuples where:
            - The first element is the data value,
            - The second is the cumulative probability (i / n).
    """
    result = []
    sample_size = len(n)
    for i in range(sample_size):
        r = (i + 1) / sample_size
        result.append((n[i], r))
    return result

def plot_ecdf(data: list[float], ecdf_values: list[tuple[float, float]]) -> None:
    """
    Plots the ECDF using a step plot.

    Args:
        data (list[float]): Sorted input data.
        ecdf_values (list[tuple[float, float]]): Output from ecdf() function.
    """
    x = [point[0] for point in ecdf_values]
    y = [point[1] for point in ecdf_values]

    plt.step(x, y, where="post", label="ECDF", linewidth=2)
    plt.xlabel("Data values")
    plt.ylabel("Cumulative Probability")
    plt.title("Empirical Cumulative Distribution Function")
    plt.grid(True)
    plt.legend()
    plt.show()

# Execution

data = get_user_input()
ecdf_values = ecdf(data)
print(f"Empirical Cumulative Distribution Function (ECDF): {ecdf_values}")
plot_ecdf(data, ecdf_values)
