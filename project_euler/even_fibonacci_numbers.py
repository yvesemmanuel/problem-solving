# https://projecteuler.net/problem=2
# Reference for solution: https://en.wikipedia.org/wiki/Fibonacci_sequence#Combinatorial_proofs

def fibonacci_even_sum(upper_bound: int):
    sequence = [1, 2]
    even_sum = 2
    while sequence[-1] < upper_bound:
        next_ = sequence[-1] + sequence[-2]
        sequence.append(next_)
        if next_ % 2 == 0:
            even_sum += next_

    return even_sum

print(fibonacci_even_sum(4_000_000))