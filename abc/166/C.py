import numpy as np


def main():
    n, m = map(int, input().split())
    hs = list(map(int, input().split()))
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    hs.insert(0, 0)
    hs_arr = np.array(hs)
    ans = 0
    for i, node in enumerate(graph[1:], start=1):
        if np.all(hs[i] > hs_arr[node]):
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
