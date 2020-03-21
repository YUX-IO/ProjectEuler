"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""


def div(n):
    divs = []
    divsR = [1]
    for k in range(2, 1 + int(n ** 0.5)):
        if n % k == 0:
            divs.append(k)
    for k in divs:
        divsR.append(int(n / k))
    divsR = list(set(divsR + divs))
    return sum(divsR)


def isAmicable(n):
    if n == div(div(n)) and n != div(n):
        return True
    else:
        return False


print(sum(x for x in range(10000) if isAmicable(x)))
