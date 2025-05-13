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

def variance(numbers) -> float:
    length = len(numbers)
    if length == 0:
        raise ValueError("No numbers provided.")
    if length == 1:
        print("Sample variance is undefined for a sample size of 1.")
        return 0.0
    
    mean = sum(numbers) / length
    squared_diffs = [(i - mean) ** 2 for i in numbers]
    
    while True:
        pop_sam = input("Is your data a population or sample? (type 'population' or 'sample' [p/s]): ").lower()
        if pop_sam in ["population", "p"]:
            return sum(squared_diffs) / length
        elif pop_sam in ["sample", "s"]:
            return sum(squared_diffs) / (length - 1)
        else:
            print("Invalid input. Please enter 'population', 'sample', 'p' or 's'.")
    
# Execution

print(f"Variance = {variance(get_arr_input()):.4f}")
