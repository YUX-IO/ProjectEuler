"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""


def f():
    for a in range(1, 1000):
        for b in range(1, 1000 - a):
            c = 1000 - a - b
            l = sorted([a, b, c])
            if l[0] ** 2 + l[1] ** 2 == l[2] ** 2:
                return a * b * c


print(f())
