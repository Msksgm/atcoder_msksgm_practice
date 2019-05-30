def main():
    N = int(input())
    # S = {}
    slist = []
    # P = {}
    plist = []

    for i in range(1, N+1):
        s, p = input().split()
        slist.append(s)
        plist.append(int(p))

    print(sorted(slist))
    print(sorted(plist))

    for j, s in enumerate(sorted(slist)):
        


if __name__ == "__main__":
    main()
