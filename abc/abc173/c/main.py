import numpy as np


def main():
    h, w, k = map(int, input().split())
    cs = np.array([list(input()) for _ in range(h)])

    ans = 0
    for paint_h in range(2 ** h):
        for paint_w in range(2 ** w):
            cnt = 0
            for j in range(h):
                for l in range(w):
                    if ((paint_h >> j) & 1) == 0 and ((paint_w >> l) & 1) == 0:
                        if cs[j][l] == '#':
                            cnt += 1
            if cnt == k:
                ans += 1

    print(ans)


if __name__ == "__main__":
    main()
