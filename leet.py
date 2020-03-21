import multiprocessing as mp


def cal(x, n):
    return x ** n


def myPow(x: float, n: int) -> float:
    param_dict = {n // 4: x, 2 * n // 4: x, 3 * n // 4: x, n -: x}
    pool = mp.Pool(int(mp.cpu_count()))
    results = [pool.apply_async(cal, args=(x, n)) for n, x in param_dict.items()]
    results = [p.get() for p in results]
    print(results)
    return cal(x, n)


if __name__ == '__main__':
    print(myPow(2, 3))
