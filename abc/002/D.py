def main():
    n, m = map(int, input().split())
    xy = [list(map(int, input().split())) for _ in range(m)]

    p = [i for i in range(1, n+1)]
    ans = 0
    for i in range(1, 2**n):
        f = []
        for j in range(n):
            if (i >> j) & 1:
                f.append(p[j])
        # print(f)
        flag = True
        # for kl in combinations(f, 2):
        #     if [kl[0], kl[1]] not in xy:
        #         flag = False
        for k in range(len(f)):
            for l in range(k+1, len(f)):
                if [f[k], f[l]] not in xy:
                    flag = False
        if flag:
            ans = max(ans, len(f))
    print(ans)


if __name__ == "__main__":
    main()
