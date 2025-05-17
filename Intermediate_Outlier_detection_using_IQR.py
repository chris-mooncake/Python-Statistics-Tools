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

# Execution functions

def median(array) -> float:
    array_length = len(array)
    mid = array_length // 2
    if array_length % 2 == 0:
        return (array[mid - 1] + array[mid]) / 2
    else:
        return array[mid]

def outlier_detection(numbers):
    if len(numbers) < 4:
        print("Not enough data to perform outlier detection (need at least 4 numbers).")
        return numbers, []

    array_length = len(numbers)
    
    mid = array_length // 2
    if array_length % 2 == 0:
        lower_half = numbers[:mid]
        upper_half = numbers[mid:]
    else:
        lower_half = numbers[:mid]
        upper_half = numbers[mid+1:]

    q1_m = median(lower_half)
    q3_m = median(upper_half)
    iqr = q3_m - q1_m

    without_outliers = []
    outliers = []
    o_1 = q1_m - 1.5 * iqr
    o_3 = q3_m + 1.5 * iqr
    for i in numbers:
        if i < o_1 or i > o_3:
            outliers.append(i)
        else:
            without_outliers.append(i)
    
    return without_outliers, outliers

# Execution
no_out, out = outlier_detection(get_arr_input())
print(f"Data set without outliers: {no_out}")
print(f"Outliers: {out if len(out) > 0 else None}")
