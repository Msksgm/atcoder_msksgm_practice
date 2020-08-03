import numpy as np


def main():
    n, d = map(int, input().split())
    ans = 0
    for i in range(n):
        x, y = map(int, input().split())
        dis = np.sqrt(x**2 + y**2)
        if dis <= d:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
