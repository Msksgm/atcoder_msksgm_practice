def bfs(n, m, graph, node, prev, visited):
    visited.append(node)
    res = 0
    if len(visited) == n:
        return 1

    for edge in graph[node]:
        if edge in visited:
            continue
        if edge == prev:
            continue
        res += bfs(n, m, graph, edge, node, visited[:])

    return res


def main():
    n, m = map(int, input().split())
    # print(n)
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        i, j = map(int, input().split())
        graph[i].append(j)
        graph[j].append(i)
    visited = []
    ans = bfs(n, m, graph, 1, 0, visited)
    print(ans)


if __name__ == "__main__":
    main()
