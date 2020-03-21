"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

import datetime
import multiprocessing as mp


def collatzGen(n):
    yield n
    while n != 1:
        if n % 2 == 0:
            n = int(n / 2)
        else:
            n = 3 * n + 1
        yield n


def findLongest(r):
    longest = 0
    startNum = 1
    for k in r:
        l = len(list(collatzGen(k)))
        if l > longest:
            longest = l
            startNum = k
    return startNum, longest


def rangeGen(n):
    n += 1
    c = 0
    while c < 62500:
        yield n
        n += 1
        c += 1


if __name__ == '__main__':
    num_cores = int(mp.cpu_count())
    print("本地计算机有: " + str(num_cores) + " 核心")
    pool = mp.Pool(num_cores)

    start_t = datetime.datetime.now()

    results = [pool.apply_async(findLongest, [list(rangeGen(param))]) for param in range(0, 1000000, 62500)]
    results = [p.get() for p in results]
    theMax = max(x[1] for x in results)
    print(list(x[0] for x in results if x[1] == theMax)[0])

    end_t = datetime.datetime.now()

    elapsed_sec = (end_t - start_t).total_seconds()
    print("多进程计算 共消耗: " + "{:.2f}".format(elapsed_sec) + " 秒")
