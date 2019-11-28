from collections import deque


def bfs(h, w, ys, xs, yg, xg, cs, visited):
    queue = deque([(ys, xs, 0)])
    visited[ys][xs] = 0
    while queue:
        y, x, cnt = queue.popleft()
        # print(y, x, cnt)
        if [y, x] == [yg, xg]:
            return cnt
        for i, j in ([1, 0], [0, 1], [-1, 0], [0, -1]):
            yn, xn = y+i, x+j
            if yn < 0 or xn < 0 or yn >= h or xn >= w:
                continue
            if visited[yn][xn] == -1 and cs[yn][xn] != "#":
                queue.appendleft((yn, xn, cnt))
                visited[yn][xn] = cnt
            elif visited[yn][xn] < cnt and cs[yn][xn] == "#":
                queue.append((yn, xn, cnt+1))
                visited[yn][xn] = cnt + 1
        # import numpy as np; print(np.array(visited))
        # import pdb; pdb.set_trace()


def main():
    h, w = map(int, input().split())
    cs = [input() for _ in range(h)]
    for i in range(h):
        if "s" in cs[i]:
            ys = i
            xs = cs[i].index("s")
        if "g" in cs[i]:
            yg = i
            xg = cs[i].index("g")
    visited = [[-1]*w for _ in range(h)]
    ans = bfs(h, w, ys, xs, yg, xg, cs, visited)
    print("YES" if ans <= 2 else "NO")


if __name__ == "__main__":
    main()
