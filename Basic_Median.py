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

def median(numbers) -> float:
    length_numbers = len(numbers)
    if length_numbers % 2 == 0:
        return (numbers[length_numbers // 2 - 1] + numbers[length_numbers // 2]) / 2
    else:
        return numbers[length_numbers // 2]

# Execution

print(f"Median = {median(get_arr_input())}")
