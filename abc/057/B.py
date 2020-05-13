def main():
    n, m = map(int, input().split())
    ABs = [list(map(int, input().split())) for _ in range(n)]
    CDs = [list(map(int, input().split())) for _ in range(m)]

    for AB in ABs:
        thresh = float('inf')
        for i, CD in enumerate(CDs, start=1):
            thresh_temp = abs(AB[0]-CD[0])+abs(AB[1]-CD[1])
            if thresh == thresh_temp:
                continue
            if thresh_temp < thresh:
                ans = i
                thresh = thresh_temp
        print(ans)


if __name__ == "__main__":
    main()
