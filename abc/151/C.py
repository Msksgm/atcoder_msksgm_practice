def main():
    from sys import stdin
    input = stdin.readline
    N, M = map(int, input().split())
    SP = [list(input().split()) for i in range(M)]
    was = [0] * N
    acs = [0] * N
    penaltyCount = 0
    for sp in SP:
        if acs[int(sp[0])-1] == 1:
            continue
        if acs[int(sp[0])-1] == 0 and sp[1] == "WA":
            was[int(sp[0])-1] += 1
        elif acs[int(sp[0])-1] == 0 and sp[1] == "AC":
            acs[int(sp[0])-1] = 1
            penaltyCount += was[int(sp[0])-1]

    print(sum(acs), penaltyCount)


if __name__ == "__main__":
    main()
