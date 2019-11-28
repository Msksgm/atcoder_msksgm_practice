def main():
    n = int(input())
    s = list(map(int, input().split()))
    t = list(map(int, input().split()))

    itv = []
    for i in range(n):
        itv.append([t[i], s[i]])
    print(itv)
    itv.sort()
    print(itv)

    ass = 0
    tt = 0
    for i in range(n):
        if tt < itv[i][1]:
            ass += 1
            tt = itv[i][0]
            print(itv[i])
    print(ass)


if __name__ == "__main__":
    main()
