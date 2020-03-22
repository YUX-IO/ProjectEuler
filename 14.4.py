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


def findLongest(l):
    r = rangeGen(l[0], l[1], l[2])
    longest = 0
    startNum = 1
    for k in r:
        l = len(list(collatzGen(k)))
        if l > longest:
            longest = l
            startNum = k
    return startNum, longest


def rangeGen(ran, upperLimit, num_cores):
    ran += 1
    c = 0
    while c < int(upperLimit / num_cores):
        yield ran
        ran += 1
        c += 1


if __name__ == '__main__':
    upperLimit = int(input("请输入上限(正整数):"))
    num_cores = int(mp.cpu_count())
    print("本地计算机有: " + str(num_cores) + " 核心")
    pool = mp.Pool(num_cores)

    start_t = datetime.datetime.now()

    results = [pool.apply_async(findLongest, [[ran, upperLimit, num_cores]]) for ran in
               range(0, upperLimit, int(upperLimit / num_cores))]
    results = [result.get() for result in results]
    theMax = max(result[1] for result in results)
    print(list(x[0] for x in results if x[1] == theMax)[0])
    pool.close()
    pool.join()
    end_t = datetime.datetime.now()

    elapsed_sec = (end_t - start_t).total_seconds()
    print("多进程计算 共消耗: " + "{:.2f}".format(elapsed_sec) + " 秒")
