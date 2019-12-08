def graph(N, tree, ans):
    visited = [0 for _ in range(N+1)]
    for i, node in enumerate(tree):
        for n in node:
            if visited[n] == 0:
                visited[n] = 1
            if visited[n] == 1 and visited[i] == 1:
                ans += 1
    print(visited)
    return ans


def main():
    N = int(input())
    pos = [[] for _ in range(N+1)]
    neg = [[] for _ in range(N+1)]
    for i in range(1, N+1):
        A = int(input())
        for j in range(A):
            x, y = map(int, input().split())
            if y == 1:
                pos[i].append(x)
            else:
                neg[i].append(x)
    ans = 0
    ans = graph(N, pos, ans)
    ans = graph(N, neg, ans)
    print(ans)


if __name__ == "__main__":
    main()
