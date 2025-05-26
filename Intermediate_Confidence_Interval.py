from scipy.stats import t

# Input function

def get_user_input():
    """
    Prompts the user to enter sample data and a confidence level for confidence interval calculation.

    Returns:
        tuple: A tuple containing a list of floats (sample values) and a float (confidence level).
    """
    while True:
        print("Enter the numbers of your sample and confidence level to calculate the confidence interval.")
        sample_values = input("Please input your sample numbers separated by spaces (e.g., 1 2 3 4): ").split()
        confidence_level = input("Please input your confidence level (e.g., 0.95 for 95%): ")
        
        try:
            floats_sample_values = [float(i) for i in sample_values]
            float_confidence_level = float(confidence_level)

            if not floats_sample_values:
                print("No sample values entered. Please try again.")
                continue

            return (floats_sample_values, float_confidence_level)

        except ValueError:
            print("Invalid input detected. Please enter only numbers.")

# Confidence interval calculation function

def confidence_interval(sample, confidence):
    """
    Calculates the confidence interval for the mean of a sample.

    Args:
        sample (list of float): The sample data.
        confidence (float): The confidence level (e.g., 0.95 for 95%).

    Returns:
        tuple: A tuple containing the lower and upper bounds of the confidence interval.
    """
    sample_size = len(sample)

    if sample_size == 1:
        print("Standard deviation is undefined for a sample size of 1.")
        return None

    sample_mean = sum(sample) / sample_size

    squared_diffs = [(i - sample_mean) ** 2 for i in sample]
    sd = (sum(squared_diffs) / (sample_size - 1)) ** 0.5

    sem = sd / (sample_size ** 0.5)

    alpha = 1 - confidence
    df = sample_size - 1
    t_score = t.ppf(1 - alpha / 2, df)

    me = sem * t_score

    lower_bound = sample_mean - me
    upper_bound = sample_mean + me

    return (lower_bound, upper_bound)

# Execution

s, c = get_user_input()
result = confidence_interval(s, c)

if result:
    lb, ub = result
    print(f"Confidence Interval: ({lb:.4f}, {ub:.4f})")
