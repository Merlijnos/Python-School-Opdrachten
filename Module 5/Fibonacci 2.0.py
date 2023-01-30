def calculate_fibonacci(n):
    fibonacci_numbers = [0, 1]
    for i in range(2, n):
        next_fib = fibonacci_numbers[i-1] + fibonacci_numbers[i-2]
        fibonacci_numbers.append(next_fib)
    return fibonacci_numbers

def calculate_golden_ratio(fibonacci_numbers):
    last_2_fib = fibonacci_numbers[-1], fibonacci_numbers[-2]
    golden_ratio = last_2_fib[0] / last_2_fib[1]
    return golden_ratio

n = int(input("Enter the number of Fibonacci numbers to calculate: "))
fibonacci_numbers = calculate_fibonacci(n)
print("Fibonacci Numbers:", fibonacci_numbers)