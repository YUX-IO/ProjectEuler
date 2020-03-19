"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers
is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


def isPalindromic(n):
    return list(str(n)) == list(reversed(list(str(n))))


palList = []
for k in range(999, 99, -1):
    for i in range(k, 99, -1):
        if isPalindromic(k * i):
            palList.append(k * i)
print(max(palList))
