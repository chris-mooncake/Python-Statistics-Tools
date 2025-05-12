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

def percentile(numbers: list[float]) -> list[float]:
    def compute_percentile(data: list[float], percent: float) -> float:
        n = len(data)
        if n == 0:
            raise ValueError("Empty list has no percentiles.")
        k = (n - 1) * (percent / 100)
        f = int(k)
        c = f + 1
        if c >= n:
            return data[f]
        else:
            d0 = data[f]
            d1 = data[c]
            return d0 + (d1 - d0) * (k - f)
    return [
        compute_percentile(numbers, 75),
        compute_percentile(numbers, 95),
        compute_percentile(numbers, 99)
    ]
    
# Execution

p75, p95, p99 = percentile(get_arr_input())
print("75th percentile: {}\n95th percentile: {}\n99th percentile: {}\n".format(p75, p95, p99))
