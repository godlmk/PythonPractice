import numpy as np


if __name__ == '__main__':
    a = np.random.rand(100, 100)
    chengji = []
    for line in a:
        cj = 1
        for j in line:
            cj *= j
        chengji.append(cj)
    chengji.sort(reverse=True)
    print(chengji)