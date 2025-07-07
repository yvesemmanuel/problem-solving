# https://projecteuler.net/problem=25
import math


def get_digit_count(n: int) -> int:
    # Reference: https://stackoverflow.com/questions/2189800/how-to-find-length-of-digits-in-an-integer
    if n <= 999999999999997:
        return int(math.log10(n)) + 1
    else:
        return len(str(n))


def find_fibonacci_index_with_digits(target_digits: int) -> int:
    if target_digits < 1:
        raise ValueError("Target digits must be positive")

    fib = [1, 1]
    index = 2

    while get_digit_count(fib[-1]) < target_digits:
        fib.append(fib[-1] + fib[-2])
        index += 1

    return index

target_digits_count = 1000
result = find_fibonacci_index_with_digits(target_digits_count)
print(result)
