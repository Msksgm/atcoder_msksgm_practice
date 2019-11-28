import sys
# import numpy as np
from copy import deepcopy
input = sys.stdin.readline


def main():
    N = int(input())
    # A = np.array([int(input()) for _ in range(N)])
    A = [int(input()) for _ in range(N)]
    # print(A)

    for j in range(N):
        B = deepcopy(A)
        del B[j]
        print(max(B))
        # if j != A.index(max(A)):
        #     print(max(A))
        # else:
        #     ans = [x for i, x in enumerate(A) if i != j]
        #     print(max(ans))


if __name__ == "__main__":
    main()
