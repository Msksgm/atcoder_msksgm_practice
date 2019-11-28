from collections import deque


def dfs(sh, sw, cs, visited):
    visited[sh][sw] = 1
    stack = deque([[sh, sw]])
    # print(h, w)
    while stack:
        sh, sw = stack.pop()
        if cs[sh][sw] == "g":
            return "Yes"
        for i, j in ([1, 0], [-1, 0], [0, 1], [0, -1]):
            now_h, now_w = sh+i, sw+j
            # print(now_h, now_w)
            if now_h < 0 or now_w < 0 or now_h >= h or now_w >= w:
                continue
            elif cs[now_h][now_w] != "#" and visited[now_h][now_w] == 0:
                # print(now_h, now_w)
                visited[now_h][now_w] = 1
                stack.append([now_h, now_w])

    return "No"


if __name__ == "__main__":
    h, w = map(int, input().split())
    cs = [input() for _ in range(h)]
    # print(h, w)
    # print(cs)
    for i in range(h):
        # print(cs[i])
        if "s" in cs[i]:
            sh = i
            sw = cs[i].index("s")

    visited = [[0 for _ in range(w)] for _ in range(h)]
    # print(sh, sw)
    # print(visited)
    print(dfs(sh, sw, cs, visited))
