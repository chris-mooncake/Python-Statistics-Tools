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

def mad(numbers: list[float]) -> float:
    average = sum(numbers) / len(numbers)
    return sum(abs(x - average) for x in numbers) / len(numbers)

# Execution

print(f"MAD = {mad(get_arr_input())}")
