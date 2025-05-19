# Input array functions

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

def get_str_input() -> str:
    methods = "A. Struges' Rule\nB. Square-root Choice\nC. Freedman-Diaconis Rule\n"

    while True:
        user_input = input(f"Please select which method do you want to use:\n{methods}").upper()
        if user_input in ["A", "B", "C"]:
            return user_input
        else:
            print("Invalid indput. Please try again.")
    
# Calculation functions

def bins_histogram(k, numbers):
    min_val = numbers[0]
    max_val = numbers[-1]

    bin_width = (max_val - min_val) / k

    bins = []
    for i in range(k + 1):
        bins.append(min_val + i * bin_width)

    histogram = [0] * k

    for num in numbers:
        placed = False
        for i in range(k):
            if bins[i] <= num < bins[i + 1]:
                histogram[i] += 1
                placed = True
                break
        if not placed and num == bins[-1]:
            histogram[-1] += 1
    return bins, histogram

def struges(numbers):
    original_n = len(numbers)
    x = original_n

    count = 0
    while x > 1:
        x /= 2
        count += 1
    log2n = count + (x - 1)

    k_raw = log2n + 1
    k = int(k_raw) if k_raw == int(k_raw) else int(k_raw) + 1

    return bins_histogram(k, numbers)

def square_root_choice(numbers):
    k = len(numbers) ** 0.5
    k = int(k) if k == int(k) else int(k) + 1

    return bins_histogram(k, numbers)

def median(data):
    n = len(data)
    mid = n // 2
    if n % 2 == 0:
        return (data[mid - 1] + data[mid]) / 2
    else:
        return data[mid]

def freedman(numbers):
    if len(numbers) < 4:
        print("To use Freedman-Diaconis Rule the minimum number of values is 4.")
        exit()
    
    n = len(numbers)
    mid = n // 2

    lower_half = numbers[:mid]
    upper_half = upper_half = numbers[mid:] if n % 2 == 0 else numbers[mid + 1:]

    q1 = median(lower_half)
    q3 = median(upper_half)

    iqr = q3 - q1

    bin_width = 2 * iqr / (n ** (1/3))

    if bin_width == 0:
        print("Bin width is zero due to zero IQR. Try a different method.")
        exit()
    
    min_val = numbers[0]
    max_val = numbers[-1]
    k = (max_val - min_val) / bin_width
    k = int(k) if k == int(k) else int(k) + 1

    bins = []
    for i in range(k + 1):
        bins.append(min_val + i * bin_width)

    histogram = [0] * k
    for num in numbers:
        placed = False
        for i in range(k):
            if bins[i] <= num < bins[i + 1]:
                histogram[i] += 1
                placed = True
                break
        if not placed and num == bins[-1]:
            histogram[-1] += 1

    return bins, histogram

def draw_histogram(bins, histogram, bar_char='█'):
    max_count = max(histogram)
    scale = 40 / max_count if max_count > 0 else 1

    for i in range(len(histogram)):
        left = round(bins[i], 2)
        right = round(bins[i + 1], 2)
        count = histogram[i]
        bar = bar_char * int(count * scale)
        print(f"[{left:6} - {right:6}) | {bar} ({count})")

# Executon

numbers = get_arr_input()
method = get_str_input()

if method == "A":
    bins, hist = struges(numbers)
elif method == "B":
    bins, hist = square_root_choice(numbers)
else:
    bins, hist = freedman(numbers)

print("Bin edges: ", bins)
print("Frequencies: ", hist)

draw_histogram(bins, hist)
