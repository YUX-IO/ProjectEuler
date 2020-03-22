import datetime

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


if __name__ == '__main__':
    upperLimit = int(input("请输入上限(正整数):"))
    start_t = datetime.datetime.now()

    print(max(collatzLen(n) for n in range(1, upperLimit, 2)))

    end_t = datetime.datetime.now()
    elapsed_sec = (end_t - start_t).total_seconds()
    print("多进程计算 共消耗: " + "{:.2f}".format(elapsed_sec) + " 秒")
