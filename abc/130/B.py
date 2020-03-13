import numpy as np


def main():
    n, x = map(int, input().split())
    ls = np.array(list(map(int, input().split())))
    ans = 1
    h = 0
    for l in ls:
        h += l
        if h <= x:
            ans += 1
        else:
            break
    print(ans)


if __name__ == "__main__":
    main()
