from collections import deque


def bfs(r, c, sy, sx, gy, gx, cs, visited):
    queue = deque([])
    queue.append([sy, sx])
    visited[sy][sx] = 0
    while queue:
        y, x = queue.popleft()
        if x == gx and y == gy:
            return visited[y][x]
        for i, j in ([1, 0], [0, 1], [-1, 0], [0, -1]):
            nx, ny = x+i, y+j
            if nx >= c or ny >= c or nx < 0 or ny < 0:
                continue
            if visited[ny][nx] == -1 and cs[ny][nx] != "#":
                queue.append([ny, nx])
                visited[ny][nx] = visited[y][x] + 1


def main():
    r, c = map(int, input().split())
    sy, sx = map(int, input().split())
    gy, gx = map(int, input().split())
    cs = [input() for _ in range(r)]
    visited = [[-1 for _ in range(c)] for __ in range(r)]
    sy, sx, gy, gx = sy-1, sx-1, gy-1, gx-1

    ans = bfs(r, c, sy, sx, gy, gx, cs, visited)
    print(ans)


if __name__ == "__main__":
    main()
