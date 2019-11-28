from collections import deque


def dfs(hs, ws, cs, visited):
    stack = deque([[hs, ws]])
    visited[hs][ws] = 1
    print(stack)
    # import pdb; pdb.set_trace()
    while stack:
        h_now, w_now = stack.pop()
        print(h_now, w_now)
        if cs[h_now][w_now] == "g":
            return "Yes"
        for i, j in ([1, 0], [0, 1], [-1, 0], [0, -1]):
            new_h, new_w = h_now+i, w_now+j
            print(new_h, new_w)
            if new_w < 0 or new_h < 0 or new_h >= h or new_w >= w:
                continue
            elif cs[new_h][new_w] != "#" and visited[new_h][new_w] == 0:
                visited[new_h][new_w] = 1
                stack.append([new_h, new_w])

    return "No"


def main():

    # print(h, w)
    # print(cs)
    visited = [[0 for _ in range(h)] for _ in range(h)]
    for i in range(h):
        if "s" in cs[i]:
            hs = i
            ws = cs[i].index("s")

    print(dfs(hs, ws, cs, visited))
    # print(hs, ws)

if __name__ == "__main__":
    h, w = map(int, input().split())
    cs = [input() for _ in range(h)]
    main()
