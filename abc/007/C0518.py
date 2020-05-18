from collections import deque


def bfs(maze, sy, sx, gy, gx, maze_copy):
    q = deque()
    q.append([sy-1, sx-1])
    maze_copy[sy-1][sx-1] = 0

    while q:
        ny, nx = q.popleft()
        for i, j in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            if maze[ny+i][nx+j] == '#' or maze_copy[ny+i][nx+j] != -1:
                continue
            else:
                maze_copy[ny+i][nx+j] = maze_copy[ny][nx] + 1
                q.append([ny+i, nx+j])
    return maze_copy


def main():
    r, c = map(int, input().split())
    sy, sx = map(int, input().split())
    gy, gx = map(int, input().split())
    maze = [list(input()) for _ in range(r)]
    maze_copy = [[-1]*c for _ in range(r)]
    maze_copy = bfs(maze, sy, sx, gy, gx, maze_copy)
    ans = maze_copy[gy-1][gx-1]
    print(ans)


if __name__ == "__main__":
    main()
