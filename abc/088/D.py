from collections import deque


def bfs(h, w, visited, ss):
    visited[0][0] = 0
    queue = deque([])
    queue.append([0, 0])
    while queue:
        y, x = queue.popleft()
        if y == h-1 and x == w-1:
            return visited[y][x]
        for i, j in ([1, 0], [0, 1], [-1, 0], [0, -1]):
            xn, yn = x+i, y+j
            if xn < 0 or yn < 0 or xn >= w or yn >= h:
                continue
            if visited[yn][xn] == -1 and ss[yn][xn] != "#":
                visited[yn][xn] = visited[y][x] + 1
                queue.append([yn, xn])
    return -1


def main():
    h, w = map(int, input().split())
    ss = [input() for _ in range(h)]
    visited = [[-1 for _ in range(w)] for _ in range(h)]
    c = 0
    for s in ss:
        c += s.count("#")

    min_route = bfs(h, w, visited, ss)
    if min_route == -1:
        print(min_route)
    else:
        print(h*w - c - min_route - 1)


if __name__ == "__main__":
    main()
