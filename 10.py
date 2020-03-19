"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""


def isPrime(n):
    for k in range(int(n ** 0.5), 1, -1):
        if n % k == 0:
            return False
    return True


def primeNumbers(x):
    n = 1
    while n < x:
        n += 1
        if isPrime(n):
            yield n


s = 0
for k in primeNumbers(2000000):
    s += k
print(s)
