from itertools import permutations as permu
import numpy as np


def main():
    n = int(input())
    ps = np.array(list(map(int, input().split())))
    qs = np.array(list(map(int, input().split())))

    nums = [i for i in range(1, n+1)]
    nums_array = np.array(list(permu(nums, n)))
    a = np.where(np.all(nums_array == ps, axis=1))[0][0]
    b = np.where(np.all(nums_array == qs, axis=1))[0][0]
    ans = abs(a - b)
    print(ans)


if __name__ == "__main__":
    main()
