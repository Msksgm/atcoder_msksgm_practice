def main():
    n, q = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n-1)]
    pq = [list(map(int, input().split())) for _ in range(q)]
    tree = [[] for _ in range(n+1)]
    ans = [0 for _ in range(n+1)]
    for a, b in ab:
        tree[a].append(b)
        tree[b].append(a)

    for i in range(len(pq)):
        # print(pq[i][0], pq[i][1])
        ans[pq[i][0]] += pq[i][1]
        for j in tree[pq[i][0]]:
            print(j)
            if j > pq[i][0]:
                ans[j] += pq[i][1]

    print(ans)


if __name__ == "__main__":
    main()
