# https://projecteuler.net/problem=5
# Reference for solution: https://en.wikipedia.org/wiki/Greatest_common_divisor#Euclidean_algorithm
#                         https://en.wikipedia.org/wiki/Least_common_multiple#Using_prime_factorization

from typing import List
from functools import reduce

def gcd(x: int, y: int) -> int:
    while y != 0:
        x, y = y, x % y

    return x

def lcm(x: int, y: int) -> int:
   lcm = (x*y) // gcd(x,y)
   return lcm

def lcm_list(v: List[int]) -> int:
    return reduce(lcm, v)

print(lcm_list(list(range(1, 10))))
print(lcm_list(list(range(1, 20))))