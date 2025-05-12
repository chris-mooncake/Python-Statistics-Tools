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
        
# Calculation function

def minmax(numbers) -> list[float]:
    return [min(numbers), max(numbers)]
    
# Execution

min_val, max_val = minmax(get_arr_input())
print("Min = {}\nMax = {}".format(min_val, max_val))
