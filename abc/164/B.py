import numpy as np


def main():
    a, b, c, d = map(int, input().split())
    cb = np.ceil(c / b)
    da = np.ceil(a / d)
    if cb <= da:
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    main()
