# https://projecteuler.net/problem=1
# Reference for solution: https://en.wikipedia.org/wiki/Summation#Powers_and_logarithm_of_arithmetic_progressions

from typing import List
from math import lcm as math_lcm

def sum_multiples_below_n(mult: List[int], n: int) -> int:
    def sum_divisible_by(m: int, n: int) -> int:
        # Number of multiples of m below n
        count = (n - 1) // m
        # Sum of arithmetic series: m + 2m + ... + count*m
        total = (m * count * (count + 1)) // 2
        return total

    result = 0
    k = len(mult)

    for i in range(1, 1 << k):
        lcm = 1
        count = 0
        selected_nums = []
        for j in range(k):
            if i & (1 << j):
                selected_nums.append(mult[j])
                count += 1
                lcm = math_lcm(lcm, mult[j])

        sign = 1 if count % 2 == 1 else -1
        subset_sum = sum_divisible_by(lcm, n)
        result += sign * subset_sum

    return result

print(sum_multiples_below_n([3, 5], 10))
print(sum_multiples_below_n([3, 5], 1000))