"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""


def isPrime(n):
    for k in range(int(n ** 0.5), 1, -1):
        if n % k == 0:
            return False
    return True


def nPrime(x):
    count = 0
    n = 2
    while True:
        if isPrime(n):
            count += 1
            if count == x:
                return n
        n += 1


print(nPrime(10001))
