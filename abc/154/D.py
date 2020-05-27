import numpy as np


def main():
    n, k = map(int, input().split())
    ps = (np.array(list(map(int, input().split()))) + 1) / 2

    ans = -float("inf")
    for i in range(n-k+1):
        ans = max(ans, sum(ps[i:i+k]))
    print(ans)


if __name__ == "__main__":
    main()
