"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""


def isPrime(n):
    for k in range(int(n ** 0.5), 1, -1):
        if n % k == 0:
            return False
    return True


for k in range(int(600851475143 ** 0.5), 1, -1):
    if 600851475143 % k == 0 and isPrime(k):
        print(k)
        break
