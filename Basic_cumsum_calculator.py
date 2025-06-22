import matplotlib.pyplot as plt

# Input array function

def get_user_input() -> list[float]:
    """
    Prompts the user to input a list of numeric values separated by spaces.

    Returns:
        list[float]: A list of floating-point numbers entered by the user.

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
            return numbers
        except ValueError:
            print("Invalid input detected. Please enter only numbers.")

# Calculation function

def cumsum(n: list[float]) -> list[float]:
    """
    Calculates the cumulative sum of a list of numbers.

    Args:
        n (list[float]): List of numbers.

    Returns:
        list[float]: Cumulative sum list.
    """
    c_n = []
    t = 0
    for i in n:
        t += i
        c_n.append(t)
    return c_n

def cumsum_plot(c_n: list[float]) -> None:
    """
    Plots the cumulative sum using matplotlib.

    Args:
        c_n (list[float]): The cumulative sum list.
    """
    x = list(range(1, len(c_n) + 1))  # X-axis: index (1-based position)
    
    plt.plot(x, c_n, marker='o', linestyle='-', linewidth=2)
    plt.xlabel("Index")
    plt.ylabel("Cumulative Sum")
    plt.title("Cumulative Sum Plot")
    plt.grid(True)
    plt.show()

# Execution

cumsum_result = cumsum(get_user_input())
print(f"Cumulative Sum List: {cumsum_result}")
print(f"Total Sum: {cumsum_result[-1]}")
cumsum_plot(cumsum_result)
