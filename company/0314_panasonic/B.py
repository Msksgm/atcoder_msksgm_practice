import sys
import numpy as np


def main():
    h, w = map(int, input().split())
    if w == 1 or h == 1:
        print(1)
        sys.exit(0)

    if w % 2 == 0:
        a = w // 2
        b = a

    else:
        a = int(np.ceil(w / 2))
        b = a - 1

    if h % 2 == 0:
        ans = (h//2)*(a+b)
    else:
        ans = (h//2)*(a+b)+a

    print(ans)


if __name__ == "__main__":
    main()
