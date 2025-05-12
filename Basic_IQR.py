# Input array function

def get_arr_input():
    while True:
        numbers = []
        user_input = input("Please input your numbers separeted by spaces: ").split()
        for i in user_input:
            try:
                number = float(i)
                numbers.append(number)
            except:
                print(f"Value error. '{i}'. Please input your values again.")
                break

        if len(numbers) == len(user_input):
            return sorted(numbers)

# Calculation functions

def median(array):
    array_length = len(array)
    mid = array_length // 2
    if array_length % 2 == 0:
        return (array[mid - 1] + array[mid]) / 2
    else:
        return array[mid]

def IQR_calculation(numbers):
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
