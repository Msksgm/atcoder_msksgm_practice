from collections import deque
from itertools import permutations


def dfs(n, node, prev, visited, graph):
    visited.append(node)
    if len(visited) == n:
        return 1

    res = 0
    for edge in graph[node]:
        if edge == prev:
            continue
        if edge in visited:
            continue
        res += dfs(n, edge, prev, visited[:], graph)

    return res


def main():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    print(n, m)
    # print(graph)
    ans = dfs(n, 0, -1, [], graph)
    print(ans)


if __name__ == "__main__":
    main()
