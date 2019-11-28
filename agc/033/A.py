from collections import deque


def bfs(h, w, board, visited):
    queue = deque([])
    for i in range(h):
        for j in range(w):
            if board[i][j] == "#":
                queue.append([i, j])
                visited[i][j] = 0
    ans = 0
    while queue:
        y, x = queue.popleft()
        for i, j in ([1, 0], [0, 1], [-1, 0], [0, -1]):
            yn, xn = y+i, x+j
            if yn >= h or xn >= w or yn < 0 or xn < 0:
                continue
            if visited[yn][xn] == -1 and board[yn][xn] == ".":
                visited[yn][xn] = visited[y][x] + 1
                queue.append([yn, xn])
                ans = max(ans, visited[yn][xn])

    return ans


def main():
    h, w = map(int, input().split())
    board = [input() for _ in range(h)]
    visited = [[-1 for _ in range(w)] for _ in range(h)]
    print(bfs(h, w, board, visited))


if __name__ == "__main__":
    main()
