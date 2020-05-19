import numpy as np


def main():
    a, b, n = map(int, input().split())

    ans = int(np.floor(a*n/b)) - int(a*np.floor(n/b))
    print(ans)


if __name__ == "__main__":
    main()
