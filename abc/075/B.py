import numpy as np


def main():
    h, w = map(int, input().split())
    ss = np.array([list(input()) for _ in range(h)])
    ans = np.zeros((h, w))
    xs, ys = np.where(ss == '#')
    for x, y in zip(xs, ys):
        coord = np.array([[x, y]])
        surround = np.array([[-1, -1], [-1, 0], [-1, +1], [0, -1], [0, +1], [+1, -1], [+1, 0], [+1, +1]])
        mines = np.tile(coord, (8, 1)) - surround
        for mx, my in mines:
            if mx < 0 or my < 0 or mx >= h or my >= w:
                continue
            ans[mx, my] += 1
    ans = ans.astype(np.int16).tolist()
    for x, y in zip(xs, ys):
        ans[x][y] = '#'

    for line in ans:
        print(*line, sep='')


if __name__ == "__main__":
    main()
