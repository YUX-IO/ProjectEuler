"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""


def test(n):
    for k in range(1, 21):
        if n % k != 0:
            return False
    return True


n = 2520
while True:
    if test(n):
        print(n)
        break
    n += 2520
