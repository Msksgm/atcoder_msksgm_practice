from copy import deepcopy
from collections import deque
import numpy as np


def dfs(hs, ws, island_copy):
    visited = [[0 for _ in range(10)] for _ in range(10)]
    stack = deque([[hs, ws]])
    for i in range(10):
        for j in range(10):
            if island_copy[i][j] == "x":
                visited[i][j] = 0
            else:
                visited[i][j] = -1
    while stack:
        h_now, w_now = stack.pop()
        visited[h_now][w_now] = 0
        if np.sum(np.array(visited)) == 0:
            return True
        for i, j in ([1, 0], [0, 1], [-1, 0], [0, -1]):
            h_new, w_new = h_now+i, w_now+j
            if h_new < 0 or w_new < 0 or h_new >= 10 or w_new >= 10:
                continue
            elif island_copy[h_new][w_new] != "x" and visited[h_new][w_new] == -1:
                stack.append([h_new, w_new])
                visited[h_new][w_new] = 0


def main():
    island = [list(input()) for _ in range(10)]
    # print(island)
    for i in range(10):
        for j in range(10):
            if island[i][j] == "o":
                continue
            island_copy = deepcopy(island)
            island_copy[i][j] = "o"
            for k in range(10):
                if "o" in island_copy[k]:
                    hs, ws = k, island_copy[k].index("o")
                    # print(hs, ws)
                    break
            if dfs(hs, ws, island_copy):
                print("YES")
                exit()
    print("NO")


if __name__ == "__main__":
    main()
