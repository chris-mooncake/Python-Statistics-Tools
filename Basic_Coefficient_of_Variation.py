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



def coefficient_of_variation(numbers: list[float]) -> float:
    length = len(numbers)
    if length == 0:
        raise ValueError("No numbers provided.")
    if length == 1:
        print("Coefficient of Variation is undefined for a sample size of 1.")
        return 0.0
    
    mean = sum(numbers) / length

    if mean == 0:
        print("Mean is zero, Coefficient of Variation is undefined.")
        return 0.0

    squared_diffs = [(i - mean) ** 2 for i in numbers]
    
    while True:
        pop_sam = input("Is your data a population or sample? (type 'population' or 'sample' [p/s]): ").lower()
        if pop_sam in ["population", "p"]:
            break
        elif pop_sam in ["sample", "s"]:
            length -= 1
            break
        else:
            print("Invalid input. Please enter 'population', 'sample', 'p' or 's'.")

    standard_deviation = (sum(squared_diffs) / length) ** 0.5

    return standard_deviation / mean

# Execution

print(f"Coefficient of Variation = {coefficient_of_variation(get_arr_input()):.4f}")
