def bfs(n, m, graph, prev, node, visited):
    visited.append(node)
    res = 0
    if len(visited) == n:
        return 1

    for edge in graph[node]:
        if edge in visited:
            continue
        if edge == node:
            continue
        res += bfs(n, m, graph, node, edge, visited[:])


def main():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        i, j = map(int, input().split())
        graph[i].append(j)
        graph[j].append(i)
    visited = []
    ans = bfs(n, m, graph, 0, 1, visited[:])
    print(ans)


if __name__ == "__main__":
    main()
