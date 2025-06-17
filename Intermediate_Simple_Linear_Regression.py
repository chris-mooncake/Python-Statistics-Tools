import matplotlib.pyplot as plt

# Input function

def get_user_input() -> tuple[list[float], list[float]]:
    """
    Prompts the user to input two equal-length sets of numerical values representing 
    the independent variable (X) and the dependent variable (Y) for linear regression.

    Returns:
        tuple[list[float], list[float]]: A tuple containing two lists:
            - X values (independent variable)
            - Y values (dependent variable)
    """
    print("Enter the same number of values for each variable (X and Y) to calculate Linear Regression.")

    while True:
        user_input_x = input("Enter the X values (independent), separated by spaces (e.g., 1 2 3 4): ").split()
        user_input_y = input("Enter the Y values (dependent), separated by spaces (e.g., 2 4 6 8): ").split()
        try:
            floats_x = [float(i) for i in user_input_x]
            floats_y = [float(i) for i in user_input_y]

            if not floats_x or not floats_y:
                print("No numbers entered. Please try again.")
                continue
            elif len(floats_x) != len(floats_y):
                print("The lists you entered have different lengths. Please enter the same number of values for both X and Y.")
                continue

            return floats_x, floats_y

        except ValueError:
            print("Invalid input detected. Please enter only numeric values.")

# Calculation function

def simple_regression(x: list[float], y: list[float]) -> tuple[float, float]:
    """
    Calculates the slope and intercept of the best-fit line using the formula for 
    simple linear regression (y = mx + b).

    Args:
        x (list[float]): List of independent variable values.
        y (list[float]): List of dependent variable values.

    Returns:
        tuple[float, float]: A tuple containing:
            - m: The slope of the regression line.
            - b: The y-intercept of the regression line.
    """
    length = len(x)
    mean_x = sum(x) / length
    mean_y = sum(y) / length

    difference_x = [i - mean_x for i in x]
    difference_y = [i - mean_y for i in y]

    # Numerator: sum of product of differences
    sum_product = sum(dx * dy for dx, dy in zip(difference_x, difference_y))

    # Denominator: sum of squared differences in X
    sum_square_diff_x = sum(dx ** 2 for dx in difference_x)

    m = sum_product / sum_square_diff_x
    b = mean_y - m * mean_x

    return m, b

# Plotting

def plot_regression(x: list[float], y: list[float], m: float, b: float) -> None:
    """
    Plots the scatter plot of the data and overlays the regression line.

    Args:
        x (list[float]): Independent variable values.
        y (list[float]): Dependent variable values.
        m (float): Slope of the regression line.
        b (float): Intercept of the regression line.
    """
    plt.figure(figsize=(8, 5))
    
    # Scatter plot
    plt.scatter(x, y, color='blue', label='Data Points')

    # Regression line
    x_values = sorted(x)
    y_predicted = [m * xi + b for xi in x_values]
    plt.plot(x_values, y_predicted, color='red', label=f'Regression Line: ŷ = {b:.2f} + {m:.2f}x')

    plt.title("Linear Regression Plot")
    plt.xlabel("X (Independent Variable)")
    plt.ylabel("Y (Dependent Variable)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Execution

x, y = get_user_input()
m, b = simple_regression(x, y)
print(f"Linear regression equation for your data: ŷ = {b:.3f} + {m:.3f}x")
plot_regression(x, y, m, b)
