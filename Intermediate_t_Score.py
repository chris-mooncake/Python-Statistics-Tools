# Input function

def get_user_input():
    """
    Prompts the user to enter sample data and a population mean for t-score calculation.

    Returns:
        tuple(list[float], float): A tuple containing the sample values and the population mean.
    """
    while True:
        print("Enter the numbers of your sample and your population mean to calculate t-Score.")
        sample_values = input("Please input your sample numbers separated by spaces (e.g., 1 2 3 4): ").split()
        population_mean = input("Please input your population mean (e.g., 1.23): ")
        try:
            floats_sample_values = [float(i) for i in sample_values]
            float_population_mean = float(population_mean)

            if not floats_sample_values:
                print("No sample values entered. Please try again.")
                continue

            return (floats_sample_values, float_population_mean)

        except ValueError:
            print("Invalid input detected. Please enter only numbers.")


# Calculation function

def t_score(sample, mean):
    """
    Calculates the t-score comparing the sample mean to a known population mean.

    Args:
        sample (list[float]): List of sample observations.
        mean (float): The population mean.

    Returns:
        float: The t-score value.
    """
    n = len(sample)

    if n == 1:
        print("Standard deviation is undefined for a sample size of 1.")
        return None

    sample_mean = sum(sample) / n
    squared_diff = [(i - sample_mean) ** 2 for i in sample]
    sample_std_dev = (sum(squared_diff) / (n - 1)) ** 0.5

    se = sample_std_dev / n ** 0.5 

    if se == 0:
        print("Standard error is zero — all sample values are identical.")
        return 0.0

    t = (sample_mean - mean) / se

    return t


# Execution

s, m = get_user_input()
t = t_score(s, m)
if t is not None:
    print(f"t-Score: {t:.4f}")
else:
    print("t-Score could not be calculated due to insufficient data.")
