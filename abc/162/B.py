import numpy as np


def main():
    n = int(input())
    ns = np.array(list(range(1, n+1)))
    ans = np.sum(ns[np.where((ns % 3 != 0) & (ns % 5 != 0))])
    print(ans)


if __name__ == "__main__":
    main()
