# https://projecteuler.net/problem=6
# Reference for solution: https://en.wikipedia.org/wiki/Square_pyramidal_number
#                       : https://en.wikipedia.org/wiki/Arithmetic_progression#Sum

def sum_of_n_square(n: int) -> int:
    return int((n**3 / 3) + (n**2 / 2) + (n/6))

def square_of_n_sum(n: int) -> int:
    n_sum = n * (n + 1) // 2
    return n_sum*n_sum

def difference(n: int) -> int:
    return square_of_n_sum(n) - sum_of_n_square(n)

print(difference(10))
print(difference(100))