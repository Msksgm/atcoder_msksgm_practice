from collections import deque


def dfs(i, visited, graph):
    visited[i] = 1
    stack = deque([])

    for j in graph[i]:
        stack.append([i, j])

    while stack:
        x, y = stack.pop()
        visited[y] = 1
        for k in graph[y]:
            if visited[k] == 1 and k != x:
                return False
            if visited[k] == 0:
                stack.append([y, k])

    return True


def main():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]

    for _ in range(m):
        i, j = map(int, input().split())
        graph[i].append(j)
        graph[j].append(i)

    visited = [0 for _ in range(n+1)]
    ans = 0

    for i in range(1, n+1):
        if visited[i] == 1:
            continue
        if dfs(i, visited, graph):
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
