# Input array function

def get_arr_input() -> list[float]:
    while True:
        user_input = input("Please input your numbers separated by spaces: ").split()
        try:
            numbers = [float(i) for i in user_input]
            if not numbers:
                print("No numbers entered. Please try again.")
                continue
            return sorted(numbers)
        except ValueError:
            print("Invalid input detected. Please enter only numbers.")

# Calculation functions

def standarddeviation(numbers):
    length = len(numbers)
    if length == 0:
        raise ValueError("No numbers provided.")
    if length == 1:
        print("Standard deviation is undefined for a sample size of 1.")
        return 0.0
    
    mean = sum(numbers) / length
    squared_diffs = [(i - mean) ** 2 for i in numbers]
    
    while True:
        pop_sam = input("Is your data a population or sample? (type 'population' or 'sample' [p/s]): ").lower()
        if pop_sam in ["population", "p"]:
            return (sum(squared_diffs) / length) ** 0.5, pop_sam
        elif pop_sam in ["sample", "s"]:
            return (sum(squared_diffs) / (length - 1)) ** 0.5, pop_sam
        else:
            print("Invalid input. Please enter 'population', 'sample', 'p' or 's'.")

def skewness(numbers) -> float:
    array_length = len(numbers)
    sum_of_array = sum(numbers)
    mean = sum_of_array / array_length
    sd, pop_type = standarddeviation(numbers)

    if array_length < 3 and pop_type in ["s", "sample"]:
        print("Sample skewness requires at least 3 values.")
        return 0.0
    
    if sd == 0:
        print("Standard deviation is 0, skewness is undefined.")
        return 0.0

    if pop_type in ["population", "p"]:
        third_central_moment = sum((i - mean) ** 3 for i in numbers) / array_length
        return third_central_moment / (sd ** 3)
    elif pop_type in ["sample", "s"]:
        correction_factor = array_length / ((array_length - 1) * (array_length - 2))
        standardized_cubed = [((i - mean) / sd) ** 3 for i in numbers]
        sum_cubed = sum(standardized_cubed)
        return correction_factor * sum_cubed

# Execution

print(f"Skewness: {skewness(get_arr_input())}")
