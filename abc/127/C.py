def main():
    N, M = map(int, input().split())

    L = []
    R = []
    for i in range(M):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)

    Lout = max(L)
    Rout = min(R)
    ans = Rout - Lout+1
    if ans < 0:
        print(0)
    else:
        print(ans)


if __name__ == "__main__":
    main()
