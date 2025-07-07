# https://projecteuler.net/problem=48
def self_powers(n: int) -> int:
    
    sum_ = 0
    for i in range(1, n+1):
        sum_ += i**i
    
    return sum_

power = self_powers(1000)
print(str(power)[-10:])