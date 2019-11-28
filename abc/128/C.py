def main():
    N, M = map(int, input().split())
    ks = [list(map(int, input().split())) for i in range(M)]
    p = list(map(int, input().split()))

    print(N, M)
    print(ks)
    print(p)

    nn = 1
    for i in range(N):
        nn *= 2

    print(nn)

    x = 0
    for i in range(nn):
        y = 1
        for im in range(M):
            rslt = 1 + p[im]
            tmp = 1
            for iii in range(N):
                if tmp & 1 == 1:
                    for ik in range(1, p[im][0] + 1):
                        if ((ks[im][ik] - 1) == iii):
                            rslt += 1
                tmp >>= 1
            y *= (rslt % 2)
        x += y
    
    print(x)


if __name__ == "__main__":
    main()
