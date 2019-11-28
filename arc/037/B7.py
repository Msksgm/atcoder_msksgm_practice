from collections import deque


def dfs(i, graph, visited):
    visited[i] = 1
    stack = deque([])

    for j in graph[i]:
        stack.append([i, j])

    print(stack)
    while stack:
        x, y = stack.pop()
        visited[y] = 1
        print(x, y)
        for k in graph[y]:
            if visited[y] == 1 and k != x:
                return False
            elif visited[y] == 0:
                stack.append([y, k])
    return True


def main():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]

    for _ in range(m):
        i, j = map(int, input().split())
        graph[i].append(j)
        graph[j].append(i)

    print(graph)
    visited = [0 for _ in range(n+1)]
    ans = 0

    for i in range(1, n+1):
        if visited == 1:
            continue
        if dfs(i, graph, visited):
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
