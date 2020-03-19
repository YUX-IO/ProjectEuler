"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""


def isPrime(n):
    for k in range(int(n ** 0.5), 1, -1):
        if n % k == 0:
            return False
    return True


def primeGen(n):
    for k in range(2, n):
        if isPrime(k):
            yield k


for i in primeGen(600851475143):
    print(i)
