# https://projecteuler.net/problem=20

def sum_of_digits(n: int) -> int:
    sum = 0
    while n != 0:
        last = n % 10
        sum += last
        n //= 10
    return sum

def factorial(n: int) -> int:
    if n == 1:
        return 1
    return n*factorial(n-1)

print(sum_of_digits(factorial(100)))