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

def mode(numbers) -> str | float | list[float]:
    """
    Returns the mode of a list of numbers.
    - If there's one mode, returns it.
    - If multiple modes, returns a list.
    - If all values appear equally, returns a message.
    """
    count_dic = {}
    for number in numbers:
        count_dic[number] = count_dic.get(number, 0) + 1
    
    max_count = max(count_dic.values())
    modes = sorted([num for num, count in count_dic.items() if count == max_count])

    if len(modes) == len(count_dic):
        return "No mode (all values appear with the same frequency)"
    elif len(modes) == 1:
        return modes[0]
    else:
        return f"Multimodal: {modes}"
    
# Execution

print(f"Mode = {mode(get_arr_input())}")
