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

def median(array) -> float:
    array_length = len(array)
    mid = array_length // 2
    if array_length % 2 == 0:
        return (array[mid - 1] + array[mid]) / 2
    else:
        return array[mid]

def IQR_calculation(numbers) -> float:
    numbers_length = len(numbers)
    mid = numbers_length // 2
    if numbers_length % 2 == 0:
        lower_half = numbers[:mid]
        upper_half = numbers[mid:]
    else:
        lower_half = numbers[:mid]
        upper_half = numbers[mid+1:]

    return median(upper_half) - median(lower_half)
    

# Execution

print(f"IQR = {IQR_calculation(get_arr_input())}")
