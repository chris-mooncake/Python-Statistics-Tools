# Input array function

def get_arr_input() -> list[float]:
    while True:
        user_input = input("Please input your numbers separated by spaces: ").split()
        try:
            numbers = [float(i) for i in user_input]
            if not numbers:
                print("No numbers entered. Please try again.")
                continue
            return numbers
        except ValueError:
            print("Invalid input detected. Please enter only numbers.")

# Calculation function

def kurtosis(numbers) -> float:
    n = len(numbers)
    if n < 4:
        print("At least 4 data points are required to compute kurtosis.")
        exit()

    mean = sum(numbers) / n
    m2 = sum((x - mean) ** 2 for x in numbers)
    m4 = sum((x - mean) ** 4 for x in numbers)

    s2 = m2 / (n - 1)
    s4 = s2 ** 2

    numerator = n * (n + 1) * m4
    denominator = (n - 1) * (n - 2) * (n - 3) * s4
    correction = 3 * ((n - 1) ** 2) / ((n - 2) * (n - 3))

    excess_kurt = (numerator / denominator) - correction
    regular_kurt = excess_kurt + 3

    return regular_kurt, excess_kurt

# Execution
re, ex = kurtosis(get_arr_input())
print(f"Regular kurtosis: {re:.4f}")
print(f"Sample kurtosis: {ex:.4f}")
