import numpy as np


def main():
    n, t = map(int, input().split())
    ts = list(map(int, input().split()))
    ans = t
    for i in range(n-1):
        now = ts[i+1] - ts[i]
        ans += min(now, t)
    print(ans)


if __name__ == "__main__":
    main()
