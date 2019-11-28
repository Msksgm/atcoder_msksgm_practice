from collections import deque


def dfs(H, W, cs, hs, ws, visited):
    stack = deque([[hs, ws]])
    visited[hs][ws] = 1

    while stack:
        h_now, w_now = stack.pop()
        if cs[h_now][w_now] == "g":
            return print("Yes")
        for i, j in ([1, 0], [0, 1], [-1, 0], [0, -1]):
            h_new, w_new = h_now+i, w_now+j
            if h_new >= H or w_new >= W or h_new < 0 or w_new < 0:
                continue
            elif cs[h_new][w_new] != "#" and visited[h_new][w_new] == 0:
                visited[h_new][w_new] = 1
                stack.append([h_new, w_new])

    return print("No")


def main():
    H, W = map(int, input().split())
    cs = [input() for _ in range(H)]

    for i in range(H):
        if "s" in cs[i]:
            hs = i
            ws = cs[i].index("s")

    visited = [[0 for _ in range(W)] for _ in range(H)]
    dfs(H, W, cs, hs, ws, visited)


if __name__ == "__main__":
    main()
