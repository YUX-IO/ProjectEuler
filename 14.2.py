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


def findLongest(name, r):
    longest = 0
    startNum = 1
    for k in r:
        l = len(list(collatzGen(k)))
        if l > longest:
            longest = l
            startNum = k
    return name, startNum, longest


if __name__ == '__main__':
    num_cores = int(mp.cpu_count())
    print("本地计算机有: " + str(num_cores) + " 核心")
    pool = mp.Pool(num_cores)
    param_dict = {'task1': range(1, 62500),
                  'task2': range(62500, 12500),
                  'task3': range(12500, 187500),
                  'task4': range(187500, 250000),
                  'task5': range(250000, 312500),
                  'task6': range(312500, 375000),
                  'task7': range(375000, 437500),
                  'task8': range(437500, 500000),
                  'task9': range(500000, 562500),
                  'task10': range(562500, 625000),
                  'task11': range(625000, 687500),
                  'task12': range(687500, 750000),
                  'task13': range(750000, 812500),
                  'task14': range(812500, 875000),
                  'task15': range(875000, 937500),
                  'task16': range(937500, 1000000)}

    start_t = datetime.datetime.now()
    results = [pool.apply_async(findLongest, args=(name, param)) for name, param in param_dict.items()]
    results = [p.get() for p in results]
    print(results)
    theMax = max(x[2] for x in results)
    print(list(x[1] for x in results if x[2] == theMax)[0])
    end_t = datetime.datetime.now()
    elapsed_sec = (end_t - start_t).total_seconds()
    print("多进程计算 共消耗: " + "{:.2f}".format(elapsed_sec) + " 秒")

    print(list((name, param) for name, param in param_dict.items()))
    print(param_dict.items())
    print(param_dict)
