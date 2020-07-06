import math
import numpy as np


def comb(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


def main():
    h, w, k = map(int, input().split())
    css = np.array([list(input()) for _ in range(h)])

    ans = 0
    for paint_h in range(2 ** h):
        for paint_w in range(2 ** w):
            cnt = 0
            for i in range(h):
                for j in range(w):
                    if (paint_h >> i) & 1 == 0 and (paint_w >> j) & 1 == 0:
                        if css[i][j] == '#':
                            cnt += 1
            if cnt == k:
                ans += 1
    print(ans)


if __name__ == "__main__":
    main()
