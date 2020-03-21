import math
import multiprocessing as mp


def train_on_parameter(name, param):
    result = 0
    for num in param:
        result += math.sqrt(num * math.tanh(num) / math.log2(num) / math.log10(num))
    return {name: result}


num_cores = int(mp.cpu_count())
print("本地计算机有: " + str(num_cores) + " 核心")

print(train_on_parameter('aname', [20, 30]))
