"""
root@instance-1:~# python3 main.py
请输入上限(正整数):10000000
本地计算机有: 160 核心
(686, 8400511)
多进程计算 共消耗: 2.38 秒
root@instance-1:~# python3 main.py
请输入上限(正整数):100000000
本地计算机有: 160 核心
(950, 63728127)
多进程计算 共消耗: 21.20 秒
root@instance-1:~# python3 main.py
请输入上限(正整数):1000000000
本地计算机有: 160 核心
(987, 670617279)
多进程计算 共消耗: 214.49 秒
"""
import datetime
import multiprocessing as mp

ansDict = {}


def collatzLen(n):
    if n not in ansDict:
        if n == 1:
            ansDict[n] = 1
        elif not n % 2:
            ansDict[n] = collatzLen(n / 2)[0] + 1
        else:
            ansDict[n] = collatzLen(n * 3 + 1)[0] + 1
    return ansDict[n], n


def findMax(starter, upperLimit, num_cores):
    return max(collatzLen(n) for n in range(starter, starter + int(upperLimit / num_cores), 2))


if __name__ == '__main__':
    upperLimit = int(input("请输入上限(正整数):"))
    num_cores = int(mp.cpu_count())
    print("本地计算机有: " + str(num_cores) + " 核心")
    pool = mp.Pool(num_cores)
    start_t = datetime.datetime.now()

    results = [pool.apply_async(findMax, args=(starter, upperLimit, num_cores)) for starter in
               range(1, upperLimit, int(upperLimit / num_cores))]

    print(max(result.get() for result in results))

    end_t = datetime.datetime.now()
    elapsed_sec = (end_t - start_t).total_seconds()
    print("多进程计算 共消耗: " + "{:.2f}".format(elapsed_sec) + " 秒")
